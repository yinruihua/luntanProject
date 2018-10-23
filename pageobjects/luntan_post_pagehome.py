from selenium import webdriver
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

#点击默认版块进入的那一页
class post_page(BasePage):

    post_page_input_post_name_loc = (By.ID, 'subject')#发表文章的标题
    post_page_input_post_message_loc = (By.ID, 'fastpostmessage')#文章的内容
    post_page_post_submit_loc = (By.ID, 'fastpostsubmit')#点击发表文章

    post_page_delete_submit_loc = (By.CSS_SELECTOR,".o input")
    post_page_delete_message_submit_loc = (By.CSS_SELECTOR,'#mdly p a')
    post_page_delete_OK_submit_loc = (By.NAME,'modsubmit')

    post_page_manager_submit_loc = (By.CSS_SELECTOR,"#um a:nth-child(16)")

    post_page_publish_submit_loc = (By.ID,"newspecial")

    post_page_vota_submit_loc = (By.CSS_SELECTOR,'.mbw li:nth-child(2) a')





