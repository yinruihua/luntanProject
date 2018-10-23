from testsuits.base_testcase import BaseTestCase
from pageobjects.login_luntan import Login
from pageobjects.post_luntan import postMessage_page
from pageobjects.reply_luntan import replyMessage_page
import time

class testLoginLuntan(BaseTestCase):

    def test_luntan_login(self):
        login_page= Login(self.driver)
        login_page.login('huahua','huahua')#登录

        time.sleep(3)
        common_post_page = postMessage_page(self.driver)
        common_post_page.default_submit()
        common_post_page.post("woo", "I am very happy")  # 发表

        time.sleep(3)
        common_reply_page = replyMessage_page(self.driver)
        common_reply_page.reply("nice to meet you")#回帖

        common_reply_page.quit_common()









