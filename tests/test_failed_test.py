import logging


def test_failed_test_for_logging_example():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("Testing fail message in the logger.")
    try:
        assert True == False
    except AssertionError as err:
        LOGGER.error(err)
        raise AssertionError