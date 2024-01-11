import datetime
import os

import requests

from groq.cloud.core.exceptions import AuthenticationError, AuthTokenError


class Auth:
    _grpc_channel = None
    _grpc_channel_async = None
    _auth_token = ""
    _auth_expiry_time = ""
    _API_URL = "api.groq.com:443"
    AUTH_URL = "https://api.groq.com/v1/auth/get_token"

    def __init__(self):
        return

    def get_token(self, renew=False):
        groq_access_key = os.environ.get("GROQ_SECRET_ACCESS_KEY")

        if self._auth_token != "" and renew is False:
            return self._auth_token

        if groq_access_key is None or groq_access_key == "":
            raise AuthTokenError

        Headers = {
            "Authorization": "Bearer " + groq_access_key,
        }
        try:
            auth_resp = requests.post(url=self.AUTH_URL, headers=Headers)
            self._auth_token = auth_resp.json()["access_token"]
            self._auth_expiry_time = auth_resp.json()["expiry"]
        except requests.exceptions.JSONDecodeError as e:
            raise AuthenticationError

        # stopgap
        return self._auth_token, self._auth_expiry_time

    # def _is_past_expiry(self):
    #     return datetime.now() >= datetime.strptime(
    #         self._auth_expiry_time, "%Y-%m-%dT%H:%M:%SZ"
    #     )
