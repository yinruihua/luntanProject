#与业务无关的公共方法
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from configparser import ConfigParser
import os
import time

#创建一个log日志
logger = Logger(logger="BasePage").getlog()#实例化方法，自动调用__init__方法

class BasePage(object):
    #所有页面的基类，封装了页面的公共方法,与业务无关

    def __init__(self,driver):
        #构造函数
        self.driver = driver

    def back(self):

        #浏览器的后退按钮
        self.driver.back()
        logger.info("Click back on current page.")

    def forward(self):

        # 浏览器的前进按钮
        self.driver.forward()
        logger.info("Click forward on current page.")

    def open_url(self,url):

        #打开url站点
        self.driver.get(url)

    def quit_browser(self):

        #关闭并停止浏览器的服务
        self.driver.quit()

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except Exception as e:
            logger.error("Failed to quit the browser with %s." % e)

    # *代表元组 ** 代表字典
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素-->",loc)
        except:
            self.get_windows_img()
            logger.error(" %s 页面中未能找到 %s 元素" % (self, loc))
    # 保存图片
    def get_windows_img(self):
        #将file_path写死，直接保存到screenshot下
        file_path = os.path.dirname(os.path.abspath('.')) +'/screenshots'
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = file_path +rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s" % e)
    #输入
    def sendkeys(self,text,*loc):

        el = self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("The element %s was send." % el.text)
        except Exception as e:
            self.get_window_img()
            logger.error("Failed to sendkeys the element with %s" % e)

    def clear(self,*loc):

        el = self.find_element(*loc)
        try:
            el.clear()
            logger.info("The element %s was clear." % el.text)
        except Exception as e:
            self.get_window_img()
            logger.error("Failed to clean the element with %s" % e)

#点击元素
    def click(self,*loc):

        el = self.find_element(*loc)
        try:
            logger.info("The element %s was click." % el.text)
            el.click()
        except Exception as e:
            logger.error("Failed to click the element with %s" % e)
    #切换窗口
    def active(self,list_window):
        list_window = list_window.current_window_handle

        try:
            list_window.switch_to_window(list_window.current_window_handle)
            logger.info("窗口切换成功")
        except Exception as e:
            logger.error("窗口切换失败")
    #定义一个输出的方法
    def print(self,*loc):
        el = self.find_element(*loc)
        try:
            logger.info("The element %s was print." % el.text)

        except Exception as e:
            logger.error("Failed to print the element with %s" % e)

