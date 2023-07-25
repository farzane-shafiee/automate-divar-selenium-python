import time
from selenium.webdriver.support import expected_conditions as EC
from src.config.conftest import BaseTest
from src.logs_config.test_logger import logger
from src.apps.divar.page.filter_page.filter_page import FilterPage


class TestFilter(BaseTest):
    """

    """

    def test_01_search_box(self):

        logger.info('********************** Start Testing ************************')
        filter_page = FilterPage(self.driver)

        self.wait.until(
            EC.url_contains('https://divar.ir/s/tehran')
        )

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_page']
        )

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_page_label']
        )

        filter_page.click_search_box(self.read_data_device()['search_input'])
        logger.info('*** Search Box is Clicking ***')

    def test_02_category_clicking(self):
        filter_page = FilterPage(self.driver)

        logger.info('*** Select Category ***')

        filter_page.click_vehicles_btn()
        logger.info('*** Vehicles button is clicking ***')

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['auto_btn']
        )

        filter_page.click_auto_btn()

        self.wait.until(
            EC.url_contains('https://divar.ir/s/tehran/auto')
        )

        assert filter_page.find_current_url() == 'https://divar.ir/s/tehran/auto'
        logger.info('*** Auto button is clicking ***')

    def test_03_price_clicking(self):

        filter_page = FilterPage(self.driver)

        filter_page.click_price_btn()
        logger.info('*** price button is clicking ***')

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_price_input']
        )

        filter_page.click_price_max_btn()
        logger.info('*** Max price is clicking ***')

        filter_page.insert_search_input(self.read_data_device()['price'])
        logger.info('*** Insert price in search box is success ***')

        filter_page.click_search_result_list(self.read_data_device()['price'])
        logger.info('*** Search result is clicking ***')

    def test_04_immediate_filter_clicking(self):

        filter_page = FilterPage(self.driver)

        self.wait.until(
            EC.url_contains('https://divar.ir/s/tehran/auto?price=-200000000')
        )

        assert filter_page.find_current_url() == 'https://divar.ir/s/tehran/auto?price=-200000000'

        filter_page.click_immediate_btn()
        logger.info('*** Clicking Immediate ***')

    def test_05_kilometers_clicking(self):
        filter_page = FilterPage(self.driver)

        filter_page.scroll_by_id_locator(filter_page.locator['kilometers_btn'])
        logger.info('*** Scroll to Kilometers Filter ***')

        filter_page.click_kilometers_btn()
        logger.info('*** Clicking Kilometers Filter ***')

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_kilometers_input']
        )

        filter_page.click_kilometers_max_btn()
        logger.info('*** Max kilometers is clicking ***')

        filter_page.insert_search_input(self.read_data_device()['kilometers'])
        logger.info('*** Insert kilometers in search box is success ***')

        filter_page.click_search_result_list(self.read_data_device()['kilometers'])
        logger.info('*** Search result is clicking ***')

    def test_06_select_one_result(self):
        filter_page = FilterPage(self.driver)
        time.sleep(1)

        filter_page.select_one_result()
        logger.info('*** Select One result is clicking ***')

        time.sleep(5)
        logger.info('********************** End Testing ************************')