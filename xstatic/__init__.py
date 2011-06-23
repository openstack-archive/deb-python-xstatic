# http://remote_base/path
# http://local_base/path

class XStatic(object):
    """
    minimal support code to access resources from xstatic.pkg.* files
    or CDN locations.
    """
    name = None  # lowercase short name
    base_dir = None  # fs path to the files
    locations = {}  # CDN/remote locations

    def __init__(self, root_url='/xstatic', provider='local', protocol='http'):
        """
        :arg root_url: the common root url path for all local xstatic
                       resources
        :arg provider: 'local' to get it from local server or
                       a name of another source (e.g. CDN)
        :arg protocol: 'http' (default) or 'https'
        """
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

