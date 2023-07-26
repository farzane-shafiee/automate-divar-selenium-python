from selenium.webdriver import ActionChains, Keys
from src.config.conftest import BasePage
from src.apps.divar.page.filter_page.filter_page_locators import FilterPageLocators
from selenium.webdriver.common.by import By
from src.logs_config.test_logger import logger


class FilterPage(BasePage):

    def __init__(self, driver):
        self.locator = FilterPageLocators()
        super().__init__(driver)

    def search_in_search_box(self, search_input):
        actions = ActionChains(self.driver)

        element = self.driver.find_element(By.XPATH, self.locator['search_box'])
        element.send_keys(search_input)

        actions.move_to_element(element)
        actions.send_keys(Keys.ENTER).perform()

    def get_text_element_search_box_result(self):
        text_element = self.driver.find_element(By.XPATH, self.locator['assert_search_box']).text
        return text_element

    def click_vehicles_btn(self):
        self.driver.find_element(By.XPATH, self.locator['vehicles_btn']).click()

    def click_auto_btn(self):
        self.driver.find_element(By.XPATH, self.locator['auto_btn']).click()

    def click_car_btn(self):
        self.driver.find_element(By.XPATH, self.locator['car_btn']).click()

    def click_color_btn(self):
        self.driver.find_element(By.ID, self.locator['color_btn']).click()

    def click_color_checkbox(self):
        self.driver.find_element(By.XPATH, self.locator['color_checkbox']).click()

    def get_text_element_delete_color(self):
        text_element_color_box = self.driver.find_element(By.XPATH, self.locator['assert_delete_color_checkbox']).text
        return text_element_color_box

    def click_price_btn(self):
        self.driver.find_element(By.ID, self.locator['price_btn']).click()

    def click_price_max_btn(self):
        self.driver.find_element(By.XPATH, self.locator['price_max_btn']).click()

    def insert_search_input(self, input_data):
        self.driver.find_element(By.XPATH, self.locator['search_input']).send_keys(input_data)

    def click_search_result_list(self, input_data):
        elements = self.driver.find_elements(By.XPATH, self.locator['result_list_filter'])

        for element in elements:
            if input_data in element.text:
                element.click()
            else:
                logger.warning('*** Input data not found ***')
                assert True

    def get_text_element_delete_price(self):
        text_element_price_box = self.driver.find_element(By.XPATH, self.locator['assert_delete_price_box']).text
        return text_element_price_box

    def click_immediate_btn(self):
        self.driver.find_element(By.XPATH, self.locator['immediate_btn']).click()

    def click_kilometers_btn(self):
        self.driver.find_element(By.ID, self.locator['kilometers_btn']).click()

    def click_kilometers_max_btn(self):
        self.driver.find_element(By.XPATH, self.locator['kilometers_max_btn']).click()

    def scroll_(self):
        self.driver.execute_script("window.scrollTo(0,3500)")

    def get_search_result_list(self):
        elements = self.driver.find_elements(By.XPATH, self.locator['result_list_search'])
        return elements

    def get_text_element_delete_kilometers(self):
        text_element_price_box = self.driver.find_element(By.XPATH, self.locator['assert_delete_kilometers_box']).text
        return text_element_price_box

    def assert_select_one_item(self):
        element = self.driver.find_element(By.XPATH, self.locator['assert_select_one_item']).text
        return element
