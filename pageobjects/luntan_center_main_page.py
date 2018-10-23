from selenium import webdriver
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


class center_main_page(BasePage):
    center_luntan_page_loc = (By.ID, 'header_forum')#点击论坛

