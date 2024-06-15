import logging
import pytest

@pytest.mark.skip(reason="Тест для проверки сообщения об ошибке в логе.")  # убрать для проверки сообщения в логе
def test_failed_test_for_logging_example():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("Testing fail message in the logger.")
    try:
        assert True == False
    except AssertionError as err:
        LOGGER.error(err)
        raise AssertionError