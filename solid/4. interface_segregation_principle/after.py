class CloudHostingProvider:
    def create_server(self, region):
        raise NotImplementedError

    def list_servers(self, region):
        raise NotImplementedError


class CDNProvider:
    def get_cdn_address(self):
        raise NotImplementedError


class CloudStorageProvider:
    def store_file(self, name):
        raise NotImplementedError

    def get_file(self, name):
        raise NotImplementedError


class Amazon(CloudHostingProvider, CDNProvider, CloudStorageProvider):
    def store_file(self, name):
        # ... payload
        pass

    def get_file(self, name):
        # ... payload
        pass

    def create_server(self, region):
        # ... payload
        pass

    def list_servers(self, region):
        # ... payload
        pass

    def get_cdn_address(self):
        # ... payload
        pass


class DropBox(CloudStorageProvider):
    def store_file(self, name):
        # ... payload
        pass

    def get_file(self, name):
        # ... payload
        pass
