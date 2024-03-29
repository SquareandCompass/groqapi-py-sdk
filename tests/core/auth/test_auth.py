from groq.cloud.core.auth import Auth
from groq.cloud.core.exceptions import AuthenticationError, AuthTokenError


class TestCoreAuth:
    def test_no_key(self, monkeypatch):
        with monkeypatch.context() as mp:
            mp.delenv("GROQ_SECRET_ACCESS_KEY")
            auth_client = Auth()
            try:
                _ = auth_client.get_token()
            except Exception as e:
                assert type(e) is AuthTokenError
                return
            assert False

    def test_blank_key(self, monkeypatch):
        with monkeypatch.context() as mp:
            mp.setenv("GROQ_SECRET_ACCESS_KEY", "")
            auth_client = Auth()
            try:
                _ = auth_client.get_token()
            except Exception as e:
                assert type(e) is AuthTokenError
                return
            assert False

    def test_wrong_key(self, monkeypatch):
        with monkeypatch.context() as mp:
            mp.setenv("GROQ_SECRET_ACCESS_KEY", "sfsdfsdfsdfs")
            auth_client = Auth()
            try:
                _ = auth_client.get_token()
            except Exception as e:
                assert type(e) is AuthTokenError
                return
            assert False

    def test_correct_key(self):
        auth_client = Auth()
        try:
            _ = auth_client.get_token()
        except Exception:
            assert False
        assert True
