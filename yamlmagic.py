# -*- coding: utf-8 -*-
from __future__ import print_function

import json

from jinja2 import Environment

from IPython import get_ipython
from IPython.display import (
    display,
    Javascript,
)
from IPython.core import magic_arguments
from IPython.core.magic import (
    Magics,
    magics_class,
    cell_magic,
)
from IPython.utils.importstring import import_item


import yaml

__version__ = "0.2.1"


@magics_class
class YAMLMagics(Magics):
    """
    Write and load YAML in the IPython Notebook. Uses SafeLoader by default.

    Example:

        %%yaml x -lyaml.Loader
        foo:
            bar: baz

    """
    def __init__(self, shell):
        self.env = Environment()
        super(YAMLMagics, self).__init__(shell)

    js_tmpl_set = """
        (
            window._yaml ? window._yaml : window._yaml = {}
        )["{{ var_name }}"] = {{ value }};
        """
    js_nb_meta_set = """
        (window.Jupyter &&
            (window.Jupyter.notebook.metadata["{{ var_name }}"] = {{ value }})
        );
        """
    js_nb_cell_meta_set = """
        this.wrapper && (this.wrapper.parent().data()
            .cell.metadata["{{ var_name }}"] = {{ value }}
        );
        """

    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        "var_name",
        default=None,
        nargs="?",
        help="""Name of local variable to set to parsed value"""
    )
    @magic_arguments.argument(
        "-l", "--loader",
        default="yaml.SafeLoader",
        help="""Dotted-notation class to use for loading"""
    )
    @magic_arguments.argument(
        "-j", "--javascript",
        default=False,
        action="store_true",
        help="""set variable in window._yaml"""
    )
    @magic_arguments.argument(
        "--javascript-tmpl",
        default="",
        type=str,
        help="""set variable in window._yaml"""
    )
    @magic_arguments.argument(
        "-m", "--meta",
        default=False,
        action="store_true",
        help="""set variable in IPython.notebook.metadata"""
    )
    @magic_arguments.argument(
        "-c", "--cell-meta",
        default=False,
        action="store_true",
        help="""set variable in IPython.notebook.cells[current].metadata"""
    )
    def yaml(self, line, cell):
        line = line.strip()
        args = magic_arguments.parse_argstring(self.yaml, line)

        display(Javascript(
            """
            require(
                [
                    "notebook/js/codecell",
                    "codemirror/mode/yaml/yaml"
                ],
                function(cc){
                    cc.CodeCell.options_default.highlight_modes.magic_yaml = {
                        reg: ["^%%yaml"]
                    }
                }
            );
            """))

        loader = get_ipython().user_global_ns.get(args.loader, None)
        if loader is None:
            loader = import_item(args.loader)

        try:
            val = yaml.load(cell, Loader=loader)
        except yaml.YAMLError as err:
            print(err)
            return

        ctx = dict(
            var_name=args.var_name,
            value=json.dumps(val)
        )

        if None not in [args.javascript, args.javascript_tmpl]:
            tmpl = args.javascript_tmpl or self.js_tmpl_set
            tmpl = tmpl.strip()
            if tmpl[0] in """"'""":
                tmpl = tmpl[1:-1]
            # argparse steals some braces
            tmpl = tmpl.replace("{{{", "{{").replace("}}}", "}}")
            tmpl = self.env.from_string(tmpl)
            js = tmpl.render(**ctx)
            display(Javascript(js))

        if args.meta:
            js = self.env.from_string(self.js_nb_meta_set).render(
                **ctx
            )
            display(Javascript(js))

        if args.cell_meta:
            js = self.env.from_string(self.js_nb_cell_meta_set).render(
                **ctx
            )
            display(Javascript(js))

        if args.var_name is not None:
            get_ipython().user_ns[args.var_name] = val
        else:
            return val


def load_ipython_extension(ip):
    ip = get_ipython()
    ip.register_magics(YAMLMagics)
