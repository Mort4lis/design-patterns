class CloudProvider:
    def store_file(self, name):
        raise NotImplementedError

    def get_file(self, name):
        raise NotImplementedError

    def create_server(self, region):
        raise NotImplementedError

    def list_servers(self, region):
        raise NotImplementedError

    def get_cdn_address(self):
        raise NotImplementedError


class Amazon(CloudProvider):
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


class DropBox(CloudProvider):
    def store_file(self, name):
        # ... payload
        pass

    def get_file(self, name):
        # ... payload
        pass

    def create_server(self, region):
        # ... нет реализации
        pass

    def list_servers(self, region):
        # ... нет реализации
        pass

    def get_cdn_address(self):
        # ... нет реализации
        pass
