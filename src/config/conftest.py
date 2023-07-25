import yaml
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BaseTest:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    BASE_URL = "https://divar.ir/s/tehran"
    wait = WebDriverWait(driver, 30)

    @classmethod
    def setup_class(cls):
        """
        Remote and connect to device_data.
        """
        cls.driver.get(cls.BASE_URL)
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        cls.driver.close()

    @classmethod
    def read_data_device(cls):
        """
        Read data from YAML file and return a Json.
        """
        # cwd = os.getcwd()  # Get the current working directory (cwd)
        # files = os.listdir(cwd)  # Get all the files in that directory
        # print("Files in %r: %s" % (cwd, files))

        # os.chdir(r'/home/farzaneh/project/test-UIJet/src/pages/login_page/')
        with open('data/input_data.yml') as file:
            yaml_file = yaml.safe_load(file)
            return yaml_file


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def wait_visibility_of_element_located_by_id(wait, element):
        """
        Wait for the element to be visible by ID attribute
        :param wait: WebDriverWait
        :param element: Locator element
        :return: Time sleep
        """
        return wait.until(
            EC.visibility_of_element_located(
                (By.ID, element)
            )
        )

    @staticmethod
    def wait_visibility_of_element_located_by_xpath(wait, element):
        """
        Wait for the element to be visible by XPATH attribute
        :param wait: WebDriverWait
        :param element: Locator element
        :return: Time sleep
        """
        return wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, element)
            )
        )

    @staticmethod
    def wait_element_to_be_clickable_by_id(wait, element):
        """
        Wait for the element to be clickable by ID attribute
        :param wait: WebDriverWait
        :param element: Locator element
        :return: Time sleep
        """
        return wait.until(
            EC.element_to_be_clickable(
                (By.ID, element)
            )
        )

    def find_current_url(self):
        return self.driver.current_url

    def scroll_by_id_locator(self, locator):

        try:
            actions = ActionChains(self.driver)
            element = self.driver.find_element(By.ID, locator)

            actions.move_to_element(element)
            actions.send_keys(Keys.END).perform()
            time.sleep(1)
        except NoSuchElementException as e:
            raise e
