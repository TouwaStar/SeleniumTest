from selenium import webdriver
import pytest

from identifiers import (GETTING_STARTED_BASIC_PLAN_SUBSCRIBE, GETTING_STARTED_ADVANCED_PLAN_SUBSCRIBE,
                         GETTING_STARTED_REQUEST_A_QUOTE, LOGGING_IN_PASSWORD_TEXT_FIELD,
                         LOGGING_IN_USERNAME_TEXT_FIELD, LOGGING_IN_SIGN_IN_BUTTON)

GETTING_STARTED_PAGE_URI = "https://app.scrapinghub.com/o/366068/crawlera/getting-started"
AUTH_PAGE = "https://app.scrapinghub.com/account/login/"

TEST_USERNAME = "TestUsername"
TEST_PASSWORD = "TestPassword"


@pytest.fixture
def log_in():
    def _log_in(driver: webdriver.Chrome):
        driver.get(AUTH_PAGE)

        username_field = driver.find_element_by_xpath(LOGGING_IN_USERNAME_TEXT_FIELD)
        username_field.send_keys(TEST_USERNAME)

        password_field = driver.find_element_by_xpath(LOGGING_IN_PASSWORD_TEXT_FIELD)
        password_field.send_keys(TEST_PASSWORD)

        sign_in_button = driver.find_element_by_xpath(LOGGING_IN_SIGN_IN_BUTTON)
        sign_in_button.click()

    return _log_in


@pytest.mark.parametrize("driver", [  # webdriver.Firefox(), webdriver.Chrome(), webdriver.Safari(),
    # webdriver.Opera(), webdriver.Edge(), webdriver.Ie()])
    webdriver.Chrome()])
def test_button_presence_getting_started(driver, log_in):
    """Assert existence of subscribe/request a quote button for every plan."""
    log_in(driver)

    driver.get(GETTING_STARTED_PAGE_URI)
    driver.implicitly_wait(5)

    assert driver.find_element_by_xpath(GETTING_STARTED_BASIC_PLAN_SUBSCRIBE)
    assert driver.find_element_by_xpath(GETTING_STARTED_ADVANCED_PLAN_SUBSCRIBE)
    assert driver.find_element_by_xpath(GETTING_STARTED_REQUEST_A_QUOTE)

