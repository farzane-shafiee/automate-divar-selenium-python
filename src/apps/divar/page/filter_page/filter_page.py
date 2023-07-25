import time

from selenium.webdriver import ActionChains, Keys
from src.config.conftest import BasePage
from src.apps.divar.page.filter_page.filter_page_locators import FilterPageLocators
from selenium.webdriver.common.by import By


class FilterPage(BasePage):

    def __init__(self, driver):
        self.locator = FilterPageLocators()
        super().__init__(driver)

    def click_search_box(self, search_input):
        actions = ActionChains(self.driver)

        element = self.driver.find_element(By.XPATH, self.locator['search_box'])
        element.send_keys(search_input)

        actions.move_to_element(element)
        actions.send_keys(Keys.ENTER).perform()

    def click_vehicles_btn(self):
        self.driver.find_element(By.XPATH, self.locator['vehicles_btn']).click()

    def click_auto_btn(self):
        self.driver.find_element(By.XPATH, self.locator['auto_btn']).click()

    def click_price_btn(self):
        self.driver.find_element(By.ID, self.locator['price_btn']).click()

    def click_price_max_btn(self):
        self.driver.find_element(By.XPATH, self.locator['price_max_btn']).click()

    def insert_search_input(self, input_data):
        self.driver.find_element(By.XPATH, self.locator['search_input']).send_keys(input_data)

    def click_search_result_list(self, input_data):
        elements = self.driver.find_elements(By.XPATH, self.locator['result_list_filter'])

        for element in elements:
            # persian_price = digits.en_to_fa(price)
            # price_number = unidecode(element.text)
            if input_data in element.text:
                element.click()
            else:
                assert False

    def click_immediate_btn(self):
        self.driver.find_element(By.XPATH, self.locator['immediate_btn']).click()

    def click_kilometers_btn(self):
        self.driver.find_element(By.ID, self.locator['kilometers_btn']).click()

    def click_kilometers_max_btn(self):
        self.driver.find_element(By.XPATH, self.locator['kilometers_max_btn']).click()

    def scroll_(self):
        self.driver.execute_script("window.scrollTo(0,3500)")

    def select_one_result(self):
        elements = self.driver.find_elements(By.XPATH, self.locator['result_list_search'])
        if elements is not None:
            print(f"list: {elements}")
            for element in elements:
                element.click()
                break
        else:
            assert False
