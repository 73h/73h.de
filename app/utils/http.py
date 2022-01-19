from urllib.parse import urlparse

from flask import request


class Http:
    def __init__(self):
        host_components = urlparse(request.host_url)
        self.protocol = host_components.scheme
        self.hostname = host_components.netloc
        self.url = self.protocol + "://" + self.hostname
