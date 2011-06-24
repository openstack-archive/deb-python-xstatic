The Idea
========

XStatic is a packaging standard to package external (often 3rd party) static
files as a python package, so they are easily usable on all operating systems,
with any package management system or even without one.

Many python projects need to use some specific data files, like javascript,
css, java applets, images, etc.

Sometimes these files belong to YOUR project (then you may want to package
them separately, but you could also just put them into your main package).

But in many other cases, those files are maintained by someone else (like
jQuery javascript library or even much bigger js libraries or applications)
and you definitely do not really want to merge them into your project.

So, you want to have static file packages, but you don't want to get lots of
stuff you do not want. Thus, stuff required by XStatic file packages (especially
the main, toplevel XStatic package) tries to obey to be a MINIMAL, no-fat thing.

We won't "sell" you any web framework or other stuff you don't want.
Maybe there will be optional XStatic extensions for all sorts of stuff, but
they won't be required if you just want the files.

By having static files in packages, it is also easier to build virtual envs,
support linux/bsd/... distribution package maintainers and even windows installs
using the same mechanisms.

Pros
====
* can be put on PyPI (Python Package Index) and can get discovered there
* can be fetched and installed from PyPI automatically by just requiring it
  in your main project's setup
* you do not need to add 3rd party files to your repository or your distribution
  archives
* less work for linux distribution package maintainers, you already have split
  your stuff into separate packages, so they don't need to
* outsource some work to other people. there are lots of people needing these
  static packages, so you don't need to maintain them all yourself.
* additionally to the files, you'll get some more-or-less metadata (like
  version info, name, CDN URLs (if any).
* we can use version number of the package to reflect the version of the packaged
  static stuff and use the packaging system to require some specific version,
  or some specific minimum version.
* security updates are easier, the static file packages can be updated separately
  from your main package.

Cons
====
* it creates a little management overhead for the developer, especially if the
  xstatic file package you need does not exist yet - but packaging is very easy.


