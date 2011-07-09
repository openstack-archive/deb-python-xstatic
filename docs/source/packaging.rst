Packaging for XStatic
=====================

It's easy, no rocket-scientist needed.

We suggest you just take XStatic-jQuery package as a template and do these
steps:

* Copy XStatic-jQuery to XStatic-FooBar (replace "FooBar" by the official name
  [display_name] of the project you are packaging).
* Rename xstatic/pkg/jquery package directory to xstatic/pkg/foobar (use
  simple all-lowercase name, only a..z - this must be a valid python package
  name [name]).
* Remove xstatic/pkg/foobar/data/* and place FooBar project's static files
  there.
* Edit xstatic/pkg/foobar/__init__.py and update all information there
  appropriately (see the comments there and also the hints below).
  Most stuff from there will get reused by setup.py.
* Edit setup.py:

  - You need to change the "from xstatic.pkg import ... as xs" appropriately
    to import your package.
  - Review the rest of it, but most stuff should be fine as it just reuses
    stuff from XStatic metadata.
* Edit MANIFEST.in and change the recursive-include statement there to refer
  to your files (xstatic/pkg/foobar), so that your static files will be
  included in the package created later.
* Edit README.txt and replace references to jQuery with FooBar.
  This file's content will also be shown as long description on PyPi.
  Please note that this file is written in reST markup, so that PyPi can
  generate your project's page from it.
* If you use Mercurial, update .hgignore so it ignores:
  ^XStatic_FooBar.egg-info/
* Review all the stuff you did, make sure you did not forget anything, make
  sure there is no jquery reference left.
* Run python setup.py sdist.
* Look into build/... - there should be your XStatic-FooBar package now.
* Test it locally:

  - E.g. use pip install XStatic-FooBar-1.0.0.tar.gz to install it.
  - Use it from your project, does it work?
* If you are happy with it and you think the package is also useful for many
  other Pythonistas, register and upload it to PyPi:
  python setup.py sdist register upload

Misc. Hints
===========

Names
-----
There are 2 names involved and you should follow these rules:

* package name (== metadata NAME): simple, all lowercase name. E.g. foobar or
  jquery. If you would have to use "-": please replace it by "_". Minus is not
  valid in Python package names, so use underscore so that you can use same
  name for your package directory / package name.
* DISPLAY_NAME (metadata): the name as the upstream project itself spells it,
  e.g. jQuery or FooBar. No spaces.

Note: if you are not packaging original files, but modified files, then you
must use a name that makes this fact obvious.

Version Numbers
---------------
VERSION - as you are just repackaging another project, you should use the
upstream version number (or at least something closely related to it).

Some projects do not have good version numbers, make the best of it:

E.g. upstream version: 2010-12-31, XStatic-FooBar version: 2010.12.31

BUILD - as you maybe do not get packaging right on the first try, you'll
want to enumerate your builds: 0, 1, 2, ...

PACKAGE_VERSION - is automatically computed from VERSION . BUILD.

Which files to put into your package?
-------------------------------------
It is suggested that you only package files that are useful for Python
projects, because XStatic packages will be only used by them. No need for PHP,
ASP, Java, etc. related files.

If you package files that are somehow "compiled/compressed" versions, we
suggest you only package the files needed for production usage, not the source
code.

If the original download archive has the files needed for production in some
subdirectory, we suggest you strip the directory hierarchy and just put the
production files/directories into xstatic/pkg/foobar/data/.

CDN locations
-------------
If your files are available via a public CDN (Content Distribution Network),
you can give the URLs via the locations metadata.

If you do not have a CDN for the files, just use locations = {}.

Licensing
---------
You should put your XStatic-FooBar package under same license as the upstream
FooBar package. This avoids licensing complications and is also appropriate
because you only added a little metadata anyway.


Notes for Linux (or other OS) Package Maintainers
=================================================
If you are maintaining packages for some other packaging system, like .deb
or .rpm, this section is for you.

When designing XStatic stuff, we had YOU in mind! :)

But not only you, we also had in mind that there is no packaging system on
Windows and that developers or virtualenv users rather like setuptools,
distribute and pip.

Because of this, we did not want to rely on any mechanism that might be not
available in some scenario - thus, after files are installed, we only use
Python features (like importing from a installed python package, using
__file__ to find out the path/filename, etc.).

You, as a package maintainer are interested in avoiding duplication, so that
if you need to do a security update, you only need to fix in one place.

XStatic-* packages support this. If you do not want to heavily patch some
Python software that uses XStatic ressource packages, you can alternatively
just package the XStatic resource packages for your package system.

In case that would add duplication (because you already have a package that
provides the same static files), you can simply remove the static files below
data/ from the XStatic ressource package and adjust the path/filename so it
points to the files provided by that other package.

E.g. for the XStatic-jQuery package, change::

    BASE_DIR = join(dirname(__file__), 'data')

To::

    BASE_DIR = '/usr/share/javascript/jquery'

Of course you need to make sure that the files at the location you point to
are the same as the ones the XStatic ressource package provides below the
data/ directory.

In your package dependencies for your repackaged XStatic ressource package
you would then just require (depend on) the package providing these files.

