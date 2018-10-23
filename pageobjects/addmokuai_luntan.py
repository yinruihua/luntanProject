from pageobjects.luntan_post_pagehome import post_page
from pageobjects.base import BasePage
from pageobjects.luntan_center_login_page import center_login_page
from pageobjects.luntan_center_main_page import center_main_page
from pageobjects.luntan_add_module_pagehome import add_module_page
import time

class addMokuai(BasePage):

    def add(self):
        add = post_page(self.driver)
        self.click(*add.post_page_manager_submit_loc)#管理中心

    def center_login(self,password):
        center_password = center_login_page(self.driver)
        self.sendkeys(password,*center_password.center_login_page_password_loc)
        self.click(*center_password.center_login_page_submit_loc)#登录管理中心

    def luntan_buttom(self):
        luntan_bottom = center_main_page(self.driver)
        self.click(*luntan_bottom.center_luntan_page_loc)#点击论坛按钮

    def add_module(self,add_message):
        add_module = add_module_page(self.driver)
        self.click(*add_module.center_module_add_page_loc)
        self.sendkeys(add_message,*add_module.center_module_add_message_page_loc)
        self.click(*add_module.center_module_submit_page_loc)#添加新模块

    def quit(self):
        add_module = add_module_page(self.driver)
        self.click(*add_module.center_module_quit_page_loc)#退出管理中心


