import pytest
from pages.home_page import PaulCamperHomePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Task 1
@pytest.fixture
def browser():
    # Initiate driver
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    service_obj = Service("/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)

    # Implicit wait for the elements before attempting interactions
    driver.implicitly_wait(10)

    # Maximize the window
    driver.maximize_window()

    # Return the driver object at the end of setup
    yield driver

    # Quit the driver
    driver.quit()


def test_select_select_all_checkbox(browser):
    home_page = PaulCamperHomePage(browser)
    home_page.load()
    home_page.select_all_vehicles()
    assert browser.find_element(*home_page.select_checkbox).is_selected() is True


def test_deselect_select_all_checkbox(browser):
    home_page = PaulCamperHomePage(browser)
    home_page.load()
    home_page.select_all_vehicles()
    home_page.deselect_all_vehicles()
    assert browser.find_element(*home_page.select_checkbox).is_selected() is False


# Task 3
def test_map_toggle(browser):
    home_page = PaulCamperHomePage(browser)
    home_page.load()
    browser.find_element(*home_page.accept_all_button).click()
    assert browser.find_element(*home_page.map_off).is_displayed() is True
    browser.find_element(*home_page.toggle_map).click()
    assert browser.find_element(*home_page.map_on).is_displayed() is True
