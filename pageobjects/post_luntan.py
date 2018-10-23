from pageobjects.luntan_post_pagehome import post_page
from pageobjects.base import BasePage
from pageobjects.luntan_login_pagehome import login_page
import time

class postMessage_page(BasePage):


    def default_submit(self):
        login = login_page(self.driver)
        self.click(*login.login_page_submit_default_loc)

    def post(self, post_name, post_message):
        post = post_page(self.driver)
        self.sendkeys(post_name, *post.post_page_input_post_name_loc)
        self.sendkeys(post_message, *post.post_page_input_post_message_loc)

        self.click(*post.post_page_post_submit_loc)