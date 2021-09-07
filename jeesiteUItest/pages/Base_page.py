import os
import time

import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging

from pages.Base_logging import Log


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self.log = Log()
        self.log.info("当前页面：{0}".format(self.__class__.__name__))
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        try:
            element = self._driver.find_element(by, locator)
            self.log.info("查找到元素{0}".format(locator))
            return element
        except:
            self.screen_shot("元素定位查找")
            self.log.error("元素{0}无法找到".format(locator))
            raise


    def finds(self, by, locator):
        try:
            element = self._driver.find_elements(by, locator)
            self.log.info("查找到元素{0}".format(locator))
            return element
        except:
            self.screen_shot("元素定位查找")
            self.log.error("元素{0}无法找到".format(locator))
            raise

    def switch_frame(self, id):
        return self._driver.switch_to.frame(id)

    def switch_beforframe(self):
        return self._driver.switch_to.parent_frame()

    def wait_for_click(self, locator, time = 10):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_element(self, conditions, time = 10):
        WebDriverWait(self._driver, time).until(conditions)

    def isElementExit(self, element):
        try:
            self._driver.find_element_by_css_selector(element)
            flag = True
            return flag
        except:
            flag = False
            return flag

    def screen_shot(self, msg):
        shot_localtion = os.path.dirname(os.path.dirname(__file__)) + "\\result\\images\\" + time.strftime('%Y-%m-%d')
        if not os.path.exists(shot_localtion):
            os.mkdir(shot_localtion)
        shot_name = '{0}-{1}-{2}失败.png'.format(self.__class__.__name__, time.strftime('%H_%M_%S'), msg)
        shot_path = os.path.join(shot_localtion, shot_name)
        try:
            self._driver.save_screenshot(shot_path)
            with open(shot_path, "rb") as f:
                content = f.read()
                allure.attach(content, attachment_type=allure.attachment_type.PNG)
            self.log.info("截图成功，保存路径:{0},截图名字:{1}".format(shot_localtion, shot_name))
        except Exception:
            self.log.error("截图失败")
            raise

    # def log(self):
    #     # 创建日志器
    #     logger = logging.getLogger('logger')
    #     # 设置级别
    #     logger.setLevel(logging.INFO)
    #     # 创建格式器
    #     formator = logging.Formatter(fmt='%(asctime)s  %(filename)s %(levelname)s %(funcName)s  %(message)s')
    #     # 创建文件处理器
    #     fh = logging.FileHandler('D:/code/jeebiteUItest/log/log.log', encoding='utf-8')
    #     # 创建输出的处理器
    #     sh = logging.StreamHandler()
    #     # 输出处理器加载到日志器
    #     logger.addHandler(sh)
    #     # 文件处理器加载到日志器
    #     logger.addHandler(fh)
    #     # 将格式器放到控制台
    #     sh.setFormatter(formator)
    #     # 将格式器放到文本器里面
    #     fh.setFormatter(formator)
    #     return logger

