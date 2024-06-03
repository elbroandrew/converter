from unittest import TestCase
from api import app

class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
