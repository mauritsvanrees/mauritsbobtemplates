===================
mauritsbobtemplates
===================

``mauritsbobtemplates`` provides `mr.bob <http://mrbob.readthedocs.org/en/latest/>`_ templates to generate packages for Plone projects.
This package was originally based on `bobtemplates.plone <https://github.com/plone/bobtemplates.plone>`_.
Also, tests are setup using `collective/tox-action <https://github.com/collective/tox-action>`_.

.. note::

   With the `plonecli <https://pypi.python.org/pypi/plonecli>`_, we have a nice command line client for mauritsbobtemplates.
   We highly recommend to use the plonecli, because it adds auto completion and some nice helpers to mauritsbobtemplates.

Features
========

Package created with ``mauritsbobtemplates`` use my (Maurits van Rees) personal preferences  when creating an add-on. It also support's GIT by default, to keep track of changes one is doing with the bobtemplates.
It should be mostly the same as what you get with ``bobtemplates.plone``, but in a stripped down version.

Provided templates
------------------

- maurits_addon
- maurits_buildout

Compatibility
=============

Add-on's created with ``mauritsbobtemplates`` are tested to work in **Plone >= 5.2** and **Python >= 3.8**.

Installation
============

Just pip/pipx install it.

Usage
-----

As mauritsbobtemplates is a template for mr.bob_, we use mrbob to run the templates.

If you are using pipx or have mauritsbobtemplates globally installed, you can just use mrbob directly.

.. code-block:: console

    mrbob mauritsbobtemplates:maurits_addon -O collective.foo

Or with ``plonecli``:

.. code-block:: console

    plonecli create maurits_addon collective.foo

Configuration
=============

You can set all `mr.bob configuration <http://mrbob.readthedocs.io/en/latest/userguide.html#configuration>`_ parameters in your ~/.mrbob file.

Here is an example:

.. code-block:: bash

    [variables]
    author.name = Maurits van Rees
    author.email = maurits@vanrees.org
    author.github.user = mauritsvanrees

Contribute
==========

You should probably create your own copy based on ``bobtemplates.plone``.
But sure, feedback is welcome:

- Issue Tracker: https://github.com/mauritsvanrees/mauritsbobtemplates/issues
- Source Code: https://github.com/mauritsvanrees/mauritsbobtemplates
