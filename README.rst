
yamlmagic
=========

    an `IPython <http://ipython.org/>`__
    `magic <https://ipython.org/ipython-doc/dev/interactive/tutorial.html>`__
    for capturing data in `YAML <http://yaml.org/>`__ into a running
    IPython kernel.

|Build Status| |pypi|

.. |Build Status| image:: https://travis-ci.org/bollwyvl/yamlmagic.svg?branch=master
   :target: https://travis-ci.org/bollwyvl/yamlmagic
.. |pypi| image:: https://pypip.in/version/yamlmagic/badge.svg?style=flat

Install
-------

From the command line (or with ``!`` in a notebook cell):

.. code:: bash

    pip install yamlmagic

Enable
------

Ad-hoc
~~~~~~

In the notebook, you can use the ``%load_ext`` or ``%reload_ext`` line
magic.

.. code:: python

    %reload_ext yamlmagic

Configuration
~~~~~~~~~~~~~

In your profile's ``ipython_kernel_config.py``, you can add the
following line to automatically load ``yamlmagic`` into all your running
kernels:

.. code:: python

    c.InteractiveShellApp.extensions = ['yaml_magic']

Use
---

The ``%%yaml`` cell magic will either act as simple parser:

.. code:: python

    %%yaml
    a_toplevel_key: 1



.. parsed-literal::

    <IPython.core.display.Javascript object>




.. parsed-literal::

    {'a_toplevel_key': 1}



which can be accessed by the special last result variable ``_``:

.. code:: python

    _




.. parsed-literal::

    {'a_toplevel_key': 1}



Or will update a named variable with the parsed document:

.. code:: python

    %%yaml x
    - a: 1
      b: 2



.. parsed-literal::

    <IPython.core.display.Javascript object>


.. code:: python

    x




.. parsed-literal::

    [{'a': 1, 'b': 2}]



By default, ``yaml.SafeLoader`` will be used, which won't allow the
`powerful but
dangerous <http://pyyaml.org/wiki/PyYAMLDocumentation#LoadingYAML>`__
(and unportable) ```!python/``
tags <http://pyyaml.org/wiki/PyYAMLDocumentation#YAMLtagsandPythontypes>`__.
If you'd like to use them, provide the ``-l`` (or ``--loader``) argument
with a ``BaseLoader`` subclass available via a local variable...

.. code:: python

    from yaml import Loader
    class FooLoader(Loader):
        # some special things you have built
        pass

.. code:: python

    %%yaml --loader FooLoader
    !!python/float 0



.. parsed-literal::

    <IPython.core.display.Javascript object>




.. parsed-literal::

    0.0



...or dotted-notation path to a loader:

.. code:: python

    %%yaml --loader yaml.Loader
    !!python/float 0



.. parsed-literal::

    <IPython.core.display.Javascript object>




.. parsed-literal::

    0.0



Contribute
----------

`Issues <https://github.com/bollwyvl/yamlmagic/issues>`__ and `pull
requests <https://github.com/bollwyvl/yamlmagic/pulls>`__ welcome!

License
-------

``yamlmagic`` is released as free software under the `BSD 3-Clause
license <./LICENSE>`__.

Thank
-----

-  [@tonyfast](http://robclewley.github.io) for asking for this
-  [@robclewley](http://robclewley.github.io) for documentation-shaming
   a gist into a module
