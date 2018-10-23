from pageobjects.luntan_search_pagehome import Search_page
from pageobjects.base import BasePage
from pageobjects.luntan_login_pagehome import login_page
from framework.logger import Logger
import time

logger = Logger(logger="search_haotest_page").getlog()
class search_haotest_page(BasePage):

    def search(self,search_message):

        search_haotest = login_page(self.driver)
        self.sendkeys(search_message, *search_haotest.login_page_search_loc)
        self.click(*search_haotest.login_page_search_submit_loc)

    def name_luntan(self):
        name_luntan = Search_page(self.driver)
        self.click(*name_luntan.search_page_post_username_loc)

    def judge(self):

        name_luntan1 = Search_page(self.driver)
        post_name = name_luntan1.search_page_luntan_name_loc
        try:
            assert 'haotest' in self.driver.title
            logger.info('Test Pass.')
        except Exception as e:
            logger.error('Test Fail.', format(e))




