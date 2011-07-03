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
  Do not forget to use some appropriate class name.
* Edit setup.py:

  - You need to change the "from xstatic.pkg..." appropriately to import your
    class.
  - Review the rest of it, but most stuff should be fine as it just reuses
    stuff from XStatic metadata.
* Edit MANIFEST.in and change the recursive-include statement there to refer
  to your files (xstatic/pkg/foobar), so that your static files will be
  included in the package created later.
* Edit README.txt and replace references to jQuery with FooBar.
  This file's content will also be shown as long description on PyPi.
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
There are 3 names involved and you should follow these rules:

* XStatic subclass name: choose something starting with a uppercase letter
  to follow PEP8 naming convention. E.g. FooBar or JQuery, not foobar nor
  jQuery.
* name (metadata): simple, all lowercase name. E.g. foobar or jquery.
  If you would have to use "-": please replace it by "_". Minus is not valid
  in Python package names, so use underscore so that you can use same name
  for your package directory / package name.
* display_name (metadata): the name as the upstream project itself spells it,
  e.g. jQuery or FooBar. No spaces.

Version Numbers
---------------
As you are just repackaging another project, you should use the upstream
version number (or at least something closely related to it).

As you maybe do not get packaging right on the first try, we suggest appending
a build number, like:

* Upstream version: 1.2.3, XStatic-FooBar version: 1.2.3.0 (initial package)
* Upstream version: 1.2.3, XStatic-FooBar version: 1.2.3.1 (fixed package)
* Upstream version: 1.2.4, XStatic-FooBar version: 1.2.4.0 (initial package)

Some projects do not have such version numbers, make the best of it:

* Upstream version: 2010-12-31, XStatic-FooBar version: 2011.12.31.0

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


