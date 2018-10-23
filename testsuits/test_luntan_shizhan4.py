from testsuits.base_testcase import BaseTestCase
from pageobjects.login_luntan import Login
from pageobjects.post_luntan import postMessage_page
from pageobjects.startVota_luntan import startVota_page
from pageobjects.vota_message_luntan import vota_Message
from pageobjects.toupiao_luntan import toupiao_select_page
import time

class Test_startVoteLuntan(BaseTestCase):

    def test_start_vote_luntan(self):
        login_page= Login(self.driver)
        login_page.login('admin','haotest')#登录

        time.sleep(3)
        post_page = postMessage_page(self.driver)
        post_page.default_submit()#点击默认模块

        #点击发帖
        startvota = startVota_page(self.driver)
        startvota.click_startVota()

        votaMessage = vota_Message(self.driver)
        votaMessage.vota_message('谁最棒','他','她','它')

        toupiao_message = toupiao_select_page(self.driver)
        toupiao_message.toupiao_sel_page()



