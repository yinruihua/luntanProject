from selenium import  webdriver
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Search_page(BasePage):

    search_page_post_username_loc = (By.CSS_SELECTOR,'.pbw font')
    search_page_luntan_name_loc = (By.CSS_SELECTOR,'.ts #thread_subject')


