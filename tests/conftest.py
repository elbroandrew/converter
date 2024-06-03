import pytest
from api import app


@pytest.fixture
def client():
    with app.test_client() as client:
        app.config.update({
            "TESTING": True,
        })
        print("Creating a client.")
        yield client
        print("Shutting down the client.")
