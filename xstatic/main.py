# Copyright: 2011-2014 by the XStatic authors, see AUTHORS.txt for details.
# License: MIT license, see LICENSE.txt for details.

"""
XStatic - main package with minimal support code to work with static file packages
"""

class XStatic(object):
    """
    minimal support code to access resources from xstatic.pkg.* files
    or CDN locations.
    """
    def __init__(self, module, root_url='/xstatic', provider='local', protocol='http'):
        """
        :arg module: xstatic resource package/module, has metadata as attributes
        :arg root_url: the common root url path for all local xstatic
                       resources
        :arg provider: 'local' to get it from local server or
                       a name of another source (e.g. CDN)
        :arg protocol: 'http' (default) or 'https'
        """
        self.__dict__.update([(name.lower(), getattr(module, name))
                              for name in dir(module)
                              if name.isupper()
                             ])
        self.provider = provider
        if provider == 'local':
            self.base_url = "%s/%s" % (root_url, self.name)
        else:
            self.base_url = self.locations[(provider, protocol)]

    def get_mapping(self):
        """
        query the mapping url -> directory, use this to setup
        your own static file serving.
        """
        if self.provider == 'local':
            return self.base_url, self.base_dir

    def url_for(self, path):
        """
        compute the url for some resource.

        :arg path: a relative path into the data
        """
        loc = self.base_url
        if isinstance(loc, str):
            loc = "%s/%s" % (loc, path)
        elif isinstance(loc, dict):
            loc = loc[path]
        return loc

