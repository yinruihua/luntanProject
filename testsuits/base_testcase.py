from selenium import webdriver
from framework.browser_engine import BrowserEngine
import unittest
import time

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.open_browser()
        # self.driver = webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.implicitly_wait(5)
        # self.driver.get("http://192.101.1.26/upload/forum.php")

    def tearDown(self):
        time.sleep(7)
        self.driver.quit()
