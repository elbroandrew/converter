# from base_test import BaseTest
from api import app

def test_home(client):
    resp = client.get("/")
    assert resp.status_code ==200
