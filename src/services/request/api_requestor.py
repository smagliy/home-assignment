import requests


class ApiRequestor:
    def __init__(self, base_url: str, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def get_json(self, params=None):
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {}
