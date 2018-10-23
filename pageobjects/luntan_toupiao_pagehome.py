from selenium import webdriver
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

#点击默认版块进入的那一页
class toupiao_page(BasePage):

    toupiao_page_select_loc = (By.ID,"option_1")#选择

    toupiao_page_toupiao_sumbit_loc = (By.NAME,"pollsubmit")#提交

    toupiao_page_toupiao_message1_loc = (By.CSS_SELECTOR,'.pcht tr:nth-child(1) label')#第一个选项

    toupiao_page_toupiao_message1_percent_loc = (By.CSS_SELECTOR,'.pcht tr:nth-child(2) td:nth-child(2)')#百分比

    toupiao_page_toupiao_message2_loc = (By.CSS_SELECTOR,'.pcht tr:nth-child(3) label')#第二个选项

    toupiao_page_toupiao_message2_percent_loc = (By.CSS_SELECTOR,'.pcht tr:nth-child(4) td:nth-child(2)')#第二个百分比

    toupiao_page_toupiao_message3_loc = (By.CSS_SELECTOR,'.pcht tr:nth-child(5) label')#第三个选项

    toupiao_page_toupiao_message3_percent_loc = (By.CSS_SELECTOR,'.pcht tr:nth-child(6) td:nth-child(2)')#第三个百分比

    toupiao_page_toupiao_title_loc  = (By.ID,'thread_subject')
