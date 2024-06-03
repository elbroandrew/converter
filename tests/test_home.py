# from base_test import BaseTest
from api import app
import pytest

@pytest.mark.usefixtures("init_client", "hello")
class TestHome():

    # add fixture 'init_cleint' for every test inside this class
    @pytest.fixture(autouse=True)
    def client(self, init_client):
        self.client = init_client

    def test_home(self):
        resp = self.client.get("/")
        assert resp.status_code ==200

    def test_a(self):
        pass
