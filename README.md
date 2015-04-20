
# yamlmagic
> an [IPython](http://ipython.org/) [magic](https://ipython.org/ipython-doc/dev/interactive/tutorial.html) for capturing data in [YAML](http://yaml.org/) into a running IPython kernel.

[![Build Status][svg]][status]
![pypi][]

[svg]: https://travis-ci.org/bollwyvl/yamlmagic.svg?branch=master
[status]: https://travis-ci.org/bollwyvl/yamlmagic
[pypi]: https://pypip.in/version/yamlmagic/badge.svg?style=flat

## Install
From the command line (or with `!` in a notebook cell):
```bash
pip install yamlmagic
```

## Enable
### Ad-hoc
In the notebook, you can use the `%load_ext` or `%reload_ext` line magic.


    %load_ext yamlmagic

### Configuration
In your profile's `ipython_kernel_config.py`, you can add the following line to automatically load `yamlmagic` into all your running kernels:

```python
c.InteractiveShellApp.extensions = ['yaml_magic']
```

## Use
The `%%yaml` cell magic will either act as simple parser:


    %%yaml
    a_toplevel_key: 1


    <IPython.core.display.Javascript object>





    {'a_toplevel_key': 1}



which can be accessed by the special last result variable `_`:


    _




    {'a_toplevel_key': 1}



Or will update a named variable with the parsed document:


    %%yaml x
    - a: 1
      b: 2


    <IPython.core.display.Javascript object>



    x




    [{'a': 1, 'b': 2}]



## Contribute
[Issues](https://github.com/bollwyvl/yamlmagic/issues) and [pull requests](https://github.com/bollwyvl/yamlmagic/pulls) welcome!

## License
`yamlmagic` is released as free software under the [BSD 3-Clause license](./LICENSE).

## Thank
- [@tonyfast](http://robclewley.github.io) for asking for this
- [@robclewley](http://robclewley.github.io) for documentation-shaming a gist into a module 
