import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir+'/tools/chromedriver.exe'
    #ie_driver_path = dir+'/tools/IEDriverServer.exe'

    def open_browser(self):
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer","URL")
        logger.info("The test server url is :%s" % url)

        if browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Staring chrome browser.")
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Staring Firefox browser.")

        driver.get(url)
        logger.info("Open url : %s" % url)
        driver.maximize_window()
        logger.info("Maxmize the current window")
        driver.implicitly_wait(5)
        logger.info("Set implicitly wait 5 seconds")
        return driver
    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
