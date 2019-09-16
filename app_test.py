# coding=utf-8
import unittest
from appium import webdriver
import time
import os
import logging
import datetime

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class AndroidSimpleTest(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        handler1 = logging.FileHandler('test.log', 'w', 'utf-8')
        handler1.setFormatter(
            logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'))
        handler2 = logging.StreamHandler()
        handler2.setFormatter(
            logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'))
        logger.addHandler(handler1)
        logger.addHandler(handler2)
        desired_caps1 = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'MKJNW17C19000245',
#            "app": PATH("./test-app.apk"),
            'appPackage':'com.taobao.taobao',
            'appActivity':'com.taobao.tao.welcome.Welcome',
            # 声明中文
            #'unicodeKeyboard': 'True',
            # 声明中文，否则不支持中文
            #'resetKeyboard' : 'True',
            # 执行时不重新安装包
            'noReset' : 'True',
        }
        desired_caps2 = {
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': '721QADRG22PDL',
            'appPackage': 'com.taobao.taobao',
            'appActivity': 'com.taobao.tao.welcome.Welcome',
            # 声明中文
            # 'unicodeKeyboard': 'True',
            # 声明中文，否则不支持中文
            # 'resetKeyboard' : 'True',
            # 执行时不重新安装包
            'noReset': 'True',
        }
        #self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps1)
        self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps2)

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        # self.driver.find_element_by_accessibility_id("buttonStartWebviewCD").click()
        # input_field = self.driver.find_element_by_id('name_input')
        # time.sleep(1)
        # input_field.clear()
        # input_field.send_keys('Appium User')
        # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Send me your name!\")").click()
        # self.driver.implicitly_wait(4)
        # self.assertTrue(self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"This is my way of saying hello\")").is_displayed())
        # self.driver.find_element_by_id("goBack").click()
        logging.info('script begin wait 1s')
        time.sleep(1)
        logging.info(type(self.driver.get_window_size()))
        logging.info(dir(self.driver.get_window_size()))
        logging.info(self.driver.get_window_size().items())
        x = int(self.driver.get_window_size()['width'] * 1019 / 1080)
        y = int(self.driver.get_window_size()['height'] * 1869 / 1920)
        logging.info(type(x))
        logging.info(x)
        while input('请输入 y') != 'y':
            logging.info('请输入 y')
        #time.sleep(30)
        self.count = 0
        self.begin_time = datetime.datetime.now()

        while True:
            self.now_time = datetime.datetime.now()
            logging.info('当前是第%d次点击，截至目前脚本执行时间为%s秒',self.count,(self.now_time - self.begin_time).seconds)
            self.driver.tap([(x, y)], 500)
            time.sleep(2)
            self.driver.tap([(x, y)], 500)
            time.sleep(1)
            self.count += 1








if __name__ == '__main__':
    unittest.main()