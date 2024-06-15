from api import app
import pytest
import logging

@pytest.mark.usefixtures("init_client", "hello")
class TestHome():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("Testing Home Page")

    # add fixture 'init_client' for every test inside this class
    @pytest.fixture(autouse=True)
    def client(self, init_client):
        self.client = init_client

    def test_home_page_returns_status_code_200(self):
        resp = self.client.get("/")
        try:
            assert resp.status_code == 200
            self.LOGGER.info(f"Assert status code 200 == {resp.status_code}")
        except AssertionError as err:
            self.LOGGER.error(err)
            raise AssertionError

    def test_a(self):
        pass
