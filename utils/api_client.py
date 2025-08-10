import requests
import yaml
import os
from typing import Optional

class APIClient:
    def __init__(self, config_path: Optional[str] = None):
        if config_path is None:
            # assume repo root config/config.yaml relative to this file
            config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
        with open(config_path, 'r', encoding='utf-8') as fh:
            cfg = yaml.safe_load(fh)
        self.base_url = cfg.get('base_url').rstrip('/')
        self.timeout = cfg.get('timeout', 10)
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

    def _url(self, endpoint: str) -> str:
        if not endpoint.startswith('/'):
            endpoint = '/' + endpoint
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint: str, params: dict = None, **kwargs) -> requests.Response:
        return self.session.get(self._url(endpoint), params=params, timeout=self.timeout, **kwargs)

    def post(self, endpoint: str, json: dict = None, **kwargs) -> requests.Response:
        return self.session.post(self._url(endpoint), json=json, timeout=self.timeout, **kwargs)

    def put(self, endpoint: str, json: dict = None, **kwargs) -> requests.Response:
        return self.session.put(self._url(endpoint), json=json, timeout=self.timeout, **kwargs)

    def patch(self, endpoint: str, json: dict = None, **kwargs) -> requests.Response:
        return self.session.patch(self._url(endpoint), json=json, timeout=self.timeout, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.delete(self._url(endpoint), timeout=self.timeout, **kwargs)
