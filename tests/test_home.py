from base_test import BaseTest
from api import app

class TestHome(BaseTest):
    def test_home(self):
        with self.app as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
