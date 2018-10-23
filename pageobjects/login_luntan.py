from pageobjects.luntan_login_pagehome import login_page
from pageobjects.base import BasePage

# 点开网址后的那页
class Login(BasePage):

    def login(self,username,password):
        login = login_page(self.driver)
        self.sendkeys(username, *login.login_page_input_username_loc)#用户名
        self.sendkeys(password, *login.login_page_input_password_loc)#密码
        # time.sleep(2)
        self.click(*login.login_page_button_login_loc)#点击登录按钮
    def quit(self):
        quit = login_page(self.driver)
        self.click(*quit.login_page_submit_quit_loc)#点击退出按钮