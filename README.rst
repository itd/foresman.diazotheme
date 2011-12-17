===============================================
foresman.diazotheme
===============================================

.. contents:: Table of Contents
   :depth: 2

Overview
--------

foresman.diazotheme is an installable Plone theme that's
in theory "responsive" that uses the **theming** and **packaging**
features available in `plone.app.theming`_.

It's a terrible hack. I'm sure there are better ways to do this. I override
a bunch of plone-isms in the css. Shoot me. I'm lazy.


Requirements
------------

    * Plone 4.1.x (http://plone.org/products/plone)

    * plone.app.theming (*will be installed as a dependency of this package*)

Screenshots
------------

Layout of the site when viewed in a computer resolution:

.. image:: https://

Layout of the site when viewed with a tablet resolution:

.. image:: https://

Installation
------------

Getting the theme
~~~~~~~~~~~~~~~~~~~~

Zip file
++++++++++

If you are an end user, you might enjoy installation via zip file import.

    1. Download a `zip file <https://github.com/itd/foresman.diazotheme>`_

    2. Import the theme from the Diazo theme control panel.

Buildout
++++++++++

If you are a developer, you might enjoy installing it via buildout.

Add ``foresman.diazotheme`` to your ``plone.recipe.zope2instance`` section's
*eggs* parameter e.g.::

    [instance]
    eggs =
        Plone
        ...
        foresman.diazotheme

Or, you can add it as a dependency on your own product *setup.py*::

    install_requires=[
        ...
        'foresman.diazotheme',
    ],


Enabling the theme
~~~~~~~~~~~~~~~~~~~~

    Select and enable the theme from the Diazo control panel. That's it!


Credits
-------
    * Kurt Bendl (kurt at tool dot net) - Foresmanification

.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Plone 4.1`: http://pypi.python.org/pypi/Plone/4.1.2

