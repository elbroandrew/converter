import pytest
from api import app


@pytest.fixture(scope="class")
def init_client():
    with app.test_client() as client:
        app.config.update({
            "TESTING": True,
        })
        print("\nCreating a client.")
        assert app.debug == False
        yield client
        print("\nShutting down the client.")


@pytest.fixture(scope="function")
def hello():
    print("\nHELLO")
    yield
    print("\nBYE")


