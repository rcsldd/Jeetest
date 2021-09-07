import time

from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
from pages.Menbermanage import Menbermanage


class Main(BasePage):
    _base_url = 'http://120.24.21.52:8980/jeesite/a/index'


    def goto_user_management(self):
        # 打开组织管理
        self.finds(By.CSS_SELECTOR, '.icon-grid')[0].click()
        # 打开用户管理
        self.find(By.XPATH, '//*[@id="leftMenu"]/ul/li[1]/ul/li[1]/ul/li[1]/a/span').click()
        time.sleep(1)
        return Menbermanage(self._driver)

    def get_usermanagetitle(self, aimtitle):
        self.find(By.CSS_SELECTOR, '.icon-user').click()
        time.sleep(1)
        self.switch_frame(1)
        self.switch_frame('mainFrame')
        title = self.find(By.XPATH, '/html/body/div/div/div/div[1]/div[1]').text
        if aimtitle == title:
            return True
        else:
            return False

    def finderror(self):
        a = self.find(By.XPATH, '//*[@id="kw111"]')
        return a
