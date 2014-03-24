Using XStatic
=============

The XStatic package does only offer the most fundamental functions for
dealing with static files (and this is very much the point of XStatic:
being low-fat).

The only bit of code is in XStatic.main, class XStatic.

When you instantiate an object of this class, it'll read the uppercase
attributes from the xstatic module you give to it and make them available
as lowercase instance attributes.

E.g. (we use the xstatic-jquery package as example, see also the code
example below):

* xstatic.pkg.jquery.NAME -> xs.name
* xstatic.pkg.jquery.BASE_DIR -> xs.base_dir

Thus, you have all the metadata that came with the xstatic-jquery package
easily available.

Example code to setup local file serving
----------------------------------------

::

    from xstatic.main import XStatic
    # names below must be package names
    mod_names = [
        'jquery', 'bootstrap', 'font_awesome',
    ]
    pkg = __import__('xstatic.pkg', fromlist=mod_names)
    for mod_name in mod_names:
        mod = getattr(pkg, mod_name)
        xs = XStatic(mod, root_url='/static', provider='local', protocol='http')
        serve_files.update([(xs.name, xs.base_dir)])

    # now, serve_files has the mapping name -> base_dir for all the xstatic
    # packages you want to use. you can use it in your python code to set
    # up the static file serving.


In this example, we wanted to use the local static files we got within the
xstatic-* packages.

For some packages there is also a CDN available, you can use it by giving the
appropriate provider (not 'local') and protocol (see the xstatic-* package metadata about which cdnnames and protocols are available for the package):

::
    xs = XStatic(mod, provider='cdnname', protocol='https')
    print xs.base_url

Note: base_url is often a str (as you maybe have expected). But it also can
be a dict (which maps relative pathes to full urls) - we needed that for some
CDNs where one can not just compute the full url from base url + relative path.

The Xstatic class also has a simple url_for(relative_path) method which
computes the full url - for local URLs as well as for CDN URLs.

