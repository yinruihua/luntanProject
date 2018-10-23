from selenium import webdriver
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


class add_module_page(BasePage):

    center_module_add_page_loc = (By.CSS_SELECTOR, '.lastboard a')#点击添加新模块
    center_module_add_message_page_loc = (By.NAME,"newforum[36][]")#输入模块名称
    center_module_submit_page_loc = (By.ID,'submit_editsubmit')#点击提交按钮
    center_module_quit_page_loc = (By.CSS_SELECTOR,".uinfo a")#点击退出管理中心
