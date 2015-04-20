# -*- coding: utf-8 -*-
from __future__ import print_function

import re

from IPython import get_ipython
from IPython.display import (
    display,
    Javascript,
)
from IPython.core.magic import (
    Magics,
    magics_class,
    cell_magic,
)

import yaml


ARG_RE = re.compile(r"(?P<var_name>[a-z][\da-z_]*)?", flags=re.I)

__version__ = "0.1.0"


@magics_class
class YAMLMagics(Magics):
    """
    Write and load YAML in the IPython Notebook

    Example:

        %%yaml
        foo:
            bar: baz
    """

    def __init__(self, shell):
        super(YAMLMagics, self).__init__(shell)

    @cell_magic
    def yaml(self, line, cell):
        line = line.strip()
        opts = None

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

        if line:
            opts = re.match(ARG_RE, line)
            if opts:
                opts = opts.groupdict()

        try:
            val = yaml.safe_load(cell)
        except yaml.YAMLError as err:
            print(err)
            return

        if opts and opts["var_name"]:
            get_ipython().user_ns[opts["var_name"]] = val
        else:
            return val


def load_ipython_extension(ip):
    ip = get_ipython()
    ip.register_magics(YAMLMagics)
