from selenium import  webdriver
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class login_page(BasePage):

    login_page_input_username_loc = (By.NAME, 'username')#用户名
    login_page_input_password_loc = (By.NAME, 'password')#密码
    login_page_button_login_loc = (By.CSS_SELECTOR,'.pn')#点击登录按钮
    login_page_submit_default_loc = (By.CSS_SELECTOR, '.fl_tb td:nth-child(2) a')  # 点击默认版块
    login_page_submit_quit_loc =(By.CSS_SELECTOR,'#um a:nth-child(18)')#退出
    login_page_quit_common_loc = (By.CSS_SELECTOR,'#um a:nth-child(13)')#普通用户退出
    login_page_search_loc = (By.ID,'scbar_txt')#搜索框
    login_page_search_submit_loc = (By.ID,'scbar_btn')#搜索符号

