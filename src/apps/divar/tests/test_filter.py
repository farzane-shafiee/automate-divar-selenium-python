import time
from selenium.webdriver.support import expected_conditions as EC
from src.config.conftest import BaseTest
from src.logs_config.test_logger import logger
from src.apps.divar.page.filter_page.filter_page import FilterPage


class TestFilter(BaseTest):
    """

    """

    def test_01_category_clicking(self):
        filter_page = FilterPage(self.driver)

        logger.info('********************** Start login ************************')

        self.wait.until(
            EC.url_contains('https://divar.ir/s/tehran')
        )

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_page']
        )

        logger.info('*** Select Category ***')

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_page_label']
        )

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

    def test_02_price_clicking(self):

        filter_page = FilterPage(self.driver)

        filter_page.click_price_btn()
        logger.info('*** price button is clicking ***')

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_price_input']
        )

        filter_page.click_price_max_btn()
        logger.info('*** Max price is clicking ***')

        filter_page.insert_search_input("۲۰۰")
        logger.info('*** Insert price in search box is success ***')

        filter_page.click_search_result_list("۲۰۰")
        logger.info('*** Search result is clicking ***')

    def test_03_immediate_filter_clicking(self):

        filter_page = FilterPage(self.driver)

        self.wait.until(
            EC.url_contains('https://divar.ir/s/tehran/auto?price=-200000000')
        )

        assert filter_page.find_current_url() == 'https://divar.ir/s/tehran/auto?price=-200000000'

        filter_page.click_immediate_btn()
        logger.info('*** Clicking Immediate ***')

    def test_04_kilometers_clicking(self):
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

        filter_page.insert_search_input("۵۰")
        logger.info('*** Insert kilometers in search box is success ***')

        filter_page.click_search_result_list("۵۰")
        logger.info('*** Search result is clicking ***')

        time.sleep(5)
        logger.info('********************** End login ************************')