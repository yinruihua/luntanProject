from selenium import webdriver
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

#点击默认版块进入的那一页
class votaMessage_page(BasePage):

    vota_page_vota_title_loc = (By.ID,"subject")


    vota_page_vota_message1_loc = (By.CSS_SELECTOR,".mbm p:nth-child(1) input")


    vota_page_vota_message2_loc = (By.CSS_SELECTOR,".mbm p:nth-child(2) input")


    vota_page_vota_message3_loc =(By.CSS_SELECTOR,".mbm p:nth-child(3) input")


    vota_page_vota_sumbit_message1_loc =(By.ID,"postsubmit")

