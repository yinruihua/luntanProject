from testsuits.base_testcase import BaseTestCase
from pageobjects.login_luntan import Login
from pageobjects.search_haotest_luntan import search_haotest_page
from pageobjects.reply_luntan import replyMessage_page
import time

class testSearchLuntan(BaseTestCase):

    def test_luntan_search(self):
        login_page= Login(self.driver)
        login_page.login('admin','haotest')#登录

        time.sleep(3)

        search = search_haotest_page(self.driver)
        search.search("haotest")

        self.driver.switch_to.window(self.driver.window_handles[1])

        search.name_luntan()

        self.driver.switch_to.window(self.driver.window_handles[2])

        search.judge()

        quit_page = Login(self.driver)
        quit_page.quit()



