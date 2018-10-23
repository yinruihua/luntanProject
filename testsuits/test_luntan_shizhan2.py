from testsuits.base_testcase import BaseTestCase
from pageobjects.login_luntan import Login
from pageobjects.delete_luntan import Delete
from pageobjects.post_luntan import postMessage_page
from pageobjects.addmokuai_luntan import addMokuai
from pageobjects.reply_luntan import replyMessage_page
from pageobjects.base import BasePage
import time

class testAddModuleLuntan(BaseTestCase):
#@classmethond 整个Test类的开始和结束执行
    def test_luntan_login(self):
        login_page= Login(self.driver)
        login_page.login('admin','haotest')#登录

        time.sleep(3)
        post_page = postMessage_page(self.driver)
        post_page.default_submit()#点击默认版块

        time.sleep(3)
        delete_page = Delete(self.driver)
        delete_page.delete()#删帖

        time.sleep(3)
        center = addMokuai(self.driver)
        center.add()#点击管理中心

        self.driver.switch_to.window(self.driver.window_handles[1])

        center.center_login('haotest')#登录管理中心
        center.luntan_buttom()

        self.driver.switch_to.frame('main')

        center.add_module("haha")#添加模块

        self.driver.switch_to.default_content()#跳出iframe模块
        time.sleep(3)
        center.quit()
        #退出管理员界面
        quit_page = Login(self.driver)
        quit_page.quit()

        common_login_page = Login(self.driver)
        common_login_page.login('huahua', 'huahua')  # 普通用户登录

        time.sleep(3)
        common_post_page = postMessage_page(self.driver)
        common_post_page.default_submit()
        common_post_page.post("woo", "I am very happy")  # 发表

        time.sleep(3)
        common_reply_page = replyMessage_page(self.driver)
        common_reply_page.reply("nice to meet you")#回帖

        common_reply_page.quit_common()#退出






