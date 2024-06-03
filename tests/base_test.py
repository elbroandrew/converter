from unittest import TestCase
from api import app
import pytest


@pytest.mark.usefixtures("init_client")
class BaseTest(TestCase):

    pass