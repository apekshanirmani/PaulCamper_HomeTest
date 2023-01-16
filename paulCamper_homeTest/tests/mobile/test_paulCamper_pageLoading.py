from appium import webdriver
from pages.home_page import PaulCamperHomePage
from resources.helpers import desired_capabilities, appium_server
import pytest


# Task 2
@pytest.fixture
def browser():
    driver = webdriver.Remote(desired_capabilities= desired_capabilities, command_executor=appium_server)

    # Wait for the elements
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # Quit driver
    driver.quit()


def test_home_page_android(browser):
    home_page = PaulCamperHomePage(browser)
    home_page.load()
    browser.find_element(*PaulCamperHomePage.accept_app).click()
    assert browser.find_element(*home_page.location_app).is_displayed() is True
