import requests


class FinalRequest:
    def __init__(self, url, method="GET", **kwargs):
        self.url = url
        self.method = method
        self.kwargs = kwargs

    def finalize(self):
        requests.request(self.method, self.url, **self.kwargs)
