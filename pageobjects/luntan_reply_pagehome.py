from selenium import webdriver
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

#发表成功后进入的那页
class reply_page(BasePage):

    reply_page_input_post_message_loc = (By.ID, 'fastpostmessage')
    reply_page_post_submit_loc = (By.ID, 'fastpostsubmit')
