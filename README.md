
# yamlmagic
> an [IPython](http://ipython.org/) magic for capturing data as YAML into a running IPython kernel.

[![Build Status][svg]][status]
![pypi][]

[svg]: https://travis-ci.org/bollwyvl/yamlmagic.svg?branch=master
[status]: https://travis-ci.org/bollwyvl/yamlmagic
[pypi]: https://pypip.in/version/yamlmagic/badge.svg?style=flat

## Usage
The `%%yaml` cell magic will turn


    %%yaml x
    a_toplevel_key: 1


    <IPython.core.display.Javascript object>


## Install
From the command line (or with `!` in a notebook cell):
```bash
pip install yamlmagic
```

## Enable
### Ad-hoc
In the notebook, you can use the `%load_ext` or `%reload_ext` line magic.


    %reload_ext yamlmagic

### Configuration
In your profile's `ipython_kernel_config.py`, you can add the following line to automatically load `yamlmagic` into all your running notebook kernels:

```python
c.InteractiveShellApp.extensions = ['yaml_magic']
```

## Contributing
[Issues](https://github.com/bollwyvl/yamlmagic/issues) and [pull requests](https://github.com/bollwyvl/yamlmagic/pulls) welcome!

## License
`yamlmagic` is released as free software under the [BSD 3-Clause license](./LICENSE).

## Thanks
- [@tonyfast](http://robclewley.github.io) for asking for this
- [@robclewley](http://robclewley.github.io) for documentation-shaming a gist into a module 
