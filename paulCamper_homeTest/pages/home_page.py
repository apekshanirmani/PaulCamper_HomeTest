from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from resources.helpers import page_url


class PaulCamperHomePage:

    accept_all_button = (By.ID, 'onetrust-accept-btn-handler')
    select_checkbox = (By.XPATH, '//div[contains(.,"Select all")]/preceding-sibling::div//input[@type="checkbox"]')
    vehicle_filter = (By.XPATH, '//span[@data-test-id="FilterCamperType"]')
    select_all_checkbox = (
        By.XPATH, '//div[contains(.,"Select all")]/preceding-sibling::div//span[contains(@class,"checkbox")]')

    location_search = '[data-test-id=search-location-field]'

    toggle_map = (By.CSS_SELECTOR, '[data-test-id=map-toggle]')
    map_off = (By.XPATH, '//div[@class="searchContainer"]')
    map_on = (By.XPATH, '//div[@class="searchContainer searchContainerMapActive"]')

    accept_app = (AppiumBy.CSS_SELECTOR, '[id=onetrust-accept-btn-handler]')
    location_app = (AppiumBy.XPATH, '(//span[text()="Camping equipment"])[2]')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(page_url)

    def select_all_vehicles(self):
        self.driver.find_element(*self.accept_all_button).click()
        self.driver.find_element(*self.vehicle_filter).click()
        self.driver.find_element(*self.select_all_checkbox).click()

    def deselect_all_vehicles(self):
        self.driver.find_element(*self.select_all_checkbox).click()
