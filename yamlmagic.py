# -*- coding: utf-8 -*-
from __future__ import print_function

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

__version__ = "0.2.0"


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
        super(YAMLMagics, self).__init__(shell)

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

        if args.var_name is not None:
            get_ipython().user_ns[args.var_name] = val
        else:
            return val


def load_ipython_extension(ip):
    ip = get_ipython()
    ip.register_magics(YAMLMagics)
