# from base_test import BaseTest
from api import app
import pytest

@pytest.mark.usefixtures("init_client", "hello")
class TestHome():
    def test_home(self, init_client):
        resp = init_client.get("/")
        assert resp.status_code ==200

    def test_a(self):
        pass
