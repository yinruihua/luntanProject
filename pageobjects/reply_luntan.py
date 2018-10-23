from pageobjects.luntan_reply_pagehome import reply_page
from pageobjects.base import BasePage
from pageobjects.luntan_login_pagehome import login_page
import time


class replyMessage_page(BasePage):

    def reply(self,reply_message):

        reply = reply_page(self.driver)
        self.sendkeys(reply_message, *reply.reply_page_input_post_message_loc)

        self.click(*reply.reply_page_post_submit_loc)

    def quit(self):
        quit = login_page(self.driver)
        self.click(*quit.login_page_submit_quit_loc)

    def quit_common(self):
        quit_common = login_page(self.driver)
        self.click(*quit_common.login_page_quit_common_loc)
