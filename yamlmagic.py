# -*- coding: ascii -*-
from __future__ import print_function

import re

from IPython import (
    display,
    get_ipython,
)
from IPython.core.magic import (
    register_cell_magic,
    Magics,
    magics_class,
    cell_magic,
)
from IPython.core.magic_arguments import (
    argument,
    magic_arguments,
    parse_argstring,
)

import yaml

arg_re = re.compile(r'(?P<var_name>[a-z][\da-z_]*)?', flags=re.I)


@magics_class
class YAMLMagics(Magics):
    '''
    Write and load YAML in the IPython Notebook

    Example:

        %%yaml
        foo:
            bar: baz
    '''

    def __init__(self, shell):
        super(YAMLMagics, self).__init__(shell)

    @cell_magic
    def yaml(self, line, cell):
        line = line.strip()
        opts = None

        display.display(display.Javascript(
            """
            require(["codemirror/mode/yaml/yaml"], function(){
                console.log("yaml mode", element)
                IPython.notebook.get_cells()
                    .filter(function(c){return c.element.has(element).length; })[0]
                    .code_mirror.setOption("mode", "yaml");
            });
            """,
            ))

        if line:
            opts = re.match(arg_re, line)
            if opts:
                opts = opts.groupdict()

        try:
            val = yaml.safe_load(cell)
        except yaml.parser.ParserError as err:
            print(err)
            return

        if opts and opts["var_name"]:
            get_ipython().user_ns[opts["var_name"]] = val
        else:
            return val

def load_ipython_extension(ip):
    ip = get_ipython()
    ip.register_magics(YAMLMagics)
