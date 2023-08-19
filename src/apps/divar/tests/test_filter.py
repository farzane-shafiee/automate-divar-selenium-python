import time
from selenium.webdriver.support import expected_conditions as EC
from src.config.conftest import BaseTest
from src.logs_config.test_logger import logger
from src.apps.divar.page.filter_page.filter_page import FilterPage


class TestFilter(BaseTest):

    def test_01_search_box(self):

        logger.info('********************** Start Testing ************************')
        filter_page = FilterPage(self.driver)

        self.wait.until(
            EC.url_contains('https://divar.ir/s/tehran')
        )  # Wait for the URL.

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_page']
        )

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_page_label']
        )  # Wait for visibility elements in page.

        filter_page.search_in_search_box(self.read_data_device()['search_input'])
        logger.info('*** Search Box is Clicking ***')

        self.wait.until(
            EC.url_contains(f"https://divar.ir/s/tehran?q={self.read_data_device()['search_input']}")
        )  # Wait for the URL.

        assert f"https://divar.ir/s/tehran?q={self.read_data_device()['search_input']}" == \
            filter_page.find_current_url()
        assert self.read_data_device()['search_input'] == filter_page.get_text_element_search_box_result()
        time.sleep(2)

    def test_02_category_clicking(self):
        filter_page = FilterPage(self.driver)
        logger.info('*** Select Category ***')

        filter_page.click_vehicles_btn()
        logger.info('*** Vehicles button is clicking ***')

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['auto_btn']
        )  # Wait for visibility auto_btn element in page.

        filter_page.click_auto_btn()
        filter_page.click_car_btn()

        self.wait.until(
            EC.url_contains(f"https://divar.ir/s/tehran/car?q={self.read_data_device()['search_input']}")
        )  # Wait for the URL.

        assert f"https://divar.ir/s/tehran/car?q={self.read_data_device()['search_input']}" == \
            filter_page.find_current_url()
        logger.info('*** Auto button is clicking ***')

    def test_03_color_clicking(self):
        filter_page = FilterPage(self.driver)

        filter_page.click_color_btn()
        logger.info('*** Color button is clicking ***')

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['color_checkbox']
        )  # Wait for visibility elements in page.
        time.sleep(1)
        filter_page.click_color_checkbox()
        logger.info('*** Color checkbox is clicking ***')

        assert filter_page.get_text_element_delete_color() == "حذف"

    def test_04_price_clicking(self):

        filter_page = FilterPage(self.driver)

        filter_page.click_price_btn()
        logger.info('*** price button is clicking ***')

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_price_input']
        )  # Wait for visibility assert_price_input element in page.

        filter_page.click_price_max_btn()
        logger.info('*** Max price is clicking ***')

        filter_page.insert_search_input(self.read_data_device()['price'])  # Insert search input price
        logger.info('*** Insert price in search box is success ***')

        filter_page.click_search_result_list(self.read_data_device()['price'])

        assert filter_page.get_text_element_delete_price() == "حذف"
        logger.info('*** Search result is clicking ***')

    def test_05_kilometers_clicking(self):
        filter_page = FilterPage(self.driver)

        filter_page.scroll_by_id_locator(filter_page.locator['kilometers_btn'])  # Scroll to element
        logger.info('*** Scroll to Kilometers Filter ***')

        filter_page.click_kilometers_btn()
        logger.info('*** Clicking Kilometers Filter ***')

        filter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, filter_page.locator['assert_kilometers_input']
        )

        filter_page.click_kilometers_max_btn()
        logger.info('*** Max kilometers is clicking ***')

        filter_page.insert_search_input(self.read_data_device()['kilometers'])  # Insert search input kilometers
        logger.info('*** Insert kilometers in search box is success ***')

        filter_page.click_search_result_list(self.read_data_device()['kilometers'])

        assert filter_page.get_text_element_delete_kilometers() == "حذف"
        logger.info('*** Search result is clicking ***')

    def test_06_immediate_filter_clicking(self):

        filter_page = FilterPage(self.driver)

        assert 'https://divar.ir/s/tehran/car?color=' in filter_page.find_current_url()

        filter_page.click_immediate_btn()
        logger.info('*** Clicking Immediate ***')

    def test_07_select_one_result(self):
        filter_page = FilterPage(self.driver)
        time.sleep(1)

        elements = filter_page.get_search_result_list()  # Get search result list
        if elements is not None:
            for element in elements:
                if "پیشنهاد جستجوی جدید" not in element.text:
                    element.click()
                    logger.info('*** Select One result is clicking ***')
                    assert filter_page.assert_select_one_item() == "اطلاعات تماس"
                else:
                    logger.warning('*** There is no card in the search result ***')
                    assert True
        else:
            logger.warning('*** There is no card in the search result ***')
            assert True

        logger.info('********************** End Testing ************************')