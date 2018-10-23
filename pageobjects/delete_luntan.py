from pageobjects.luntan_post_pagehome import post_page
from pageobjects.base import BasePage
from pageobjects.luntan_login_pagehome import login_page
import time

class Delete(BasePage):

    def delete(self):
        delete= post_page(self.driver)

        self.click(delete.post_page_delete_submit_loc)#点击帖子前头的小方块

        self.click(delete.post_page_delete_message_submit_loc)#点击删除按钮

        self.click(delete.post_page_delete_OK_submit_loc)#点击确定按钮
#元组和字典必须放在参数列表的末尾