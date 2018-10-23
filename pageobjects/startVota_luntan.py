from pageobjects.luntan_reply_pagehome import reply_page
from pageobjects.base import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from framework.logger import Logger
from pageobjects.luntan_post_pagehome import post_page
import time

logger = Logger(logger="startVota_page").getlog()

class startVota_page(BasePage):


    def click_startVota(self):
        vota = post_page(self.driver)
        time.sleep(5)
        self.click(*vota.post_page_publish_submit_loc)
        self.click(*vota.post_page_vota_submit_loc)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(vota.post_page_publish_submit_loc)
        # actions.click(vota.post_page_vota_submit_loc)
        # actions.perform()
