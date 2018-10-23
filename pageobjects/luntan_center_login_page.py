from selenium import webdriver
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


class center_login_page(BasePage):
    center_login_page_password_loc = (By.CLASS_NAME, "txt")  # 登录管理中心
    center_login_page_submit_loc = (By.NAME, "submit")#点击登录

