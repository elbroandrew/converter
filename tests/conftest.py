import pytest
from api import app


@pytest.fixture(scope="class")
def init_client():
    with app.test_client() as client:
        app.config.update({
            "TESTING": True,
        })
        print("\nCreating a client.")
        yield client
        print("\nShutting down the client.")
