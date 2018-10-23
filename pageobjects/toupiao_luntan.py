from pageobjects.luntan_reply_pagehome import reply_page
from pageobjects.base import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from framework.logger import Logger
from pageobjects.luntan_toupiao_pagehome import toupiao_page
import time

logger = Logger(logger="startVota_page").getlog()

class toupiao_select_page(BasePage):


    def toupiao_sel_page(self):
        toupiao_select = toupiao_page(self.driver)
        self.click(*toupiao_select.toupiao_page_select_loc)
        self.click(*toupiao_select.toupiao_page_toupiao_sumbit_loc)#点击投票

        self.print(*toupiao_select.toupiao_page_toupiao_message1_loc)
        self.print(*toupiao_select.toupiao_page_toupiao_message1_percent_loc)
        self.print(*toupiao_select.toupiao_page_toupiao_message2_loc)
        self.print(*toupiao_select.toupiao_page_toupiao_message2_percent_loc)
        self.print(*toupiao_select.toupiao_page_toupiao_message3_loc)
        self.print(*toupiao_select.toupiao_page_toupiao_message3_percent_loc)
        self.print(*toupiao_select.toupiao_page_toupiao_title_loc)#投票信息






