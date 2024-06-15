from html.parser import HTMLParser
import pytest
import logging

class MyHTML_Parser(HTMLParser):

    def __init__(self, *, convert_charrefs: bool = True) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.html_tag = ""

    def handle_starttag(self, tag, attrs):
        if tag == 'html':
            self.html_tag = tag
    
    def handle_endtag(self, tag):
        return tag
    
    def get_html_tag(self):
        return self.html_tag


@pytest.mark.usefixtures("init_client")
class TestHTMLtags():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("Testing HTML tag")

    @pytest.fixture(autouse=True)
    def client(self, init_client):
        self.client = init_client
    
    def test_html_start_tag(self):
        resp = self.client.get("/")
        parser = MyHTML_Parser()
        parser.feed(resp.text)
        try:
            assert parser.get_html_tag() == 'html'
            self.LOGGER.info(f"'html' tag is present in the DOM.")
        except AssertionError as err:
            self.LOGGER.error(err)
            raise AssertionError
        
