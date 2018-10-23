from pageobjects.luntan_vota_message_pagehome import votaMessage_page
from pageobjects.base import BasePage
from pageobjects.luntan_login_pagehome import login_page
import time


class vota_Message(BasePage):

    def vota_message(self,vota_title,vota_message1,vota_message2,vota_message3):

        vota_message = votaMessage_page(self.driver)
        self.sendkeys(vota_title,*vota_message.vota_page_vota_title_loc)
        self.sendkeys(vota_message1,*vota_message.vota_page_vota_message1_loc)
        self.sendkeys(vota_message2,*vota_message.vota_page_vota_message2_loc)
        time.sleep(3)
        self.sendkeys(vota_message3,*vota_message.vota_page_vota_message3_loc)
        self.click(*vota_message.vota_page_vota_sumbit_message1_loc)


