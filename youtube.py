from selenium_driver import BaseClass

import work_with_file_system as work_fs

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import random


class YouTube(BaseClass):

    def __init__(self, DRIVER, login, password):
        super(YouTube, self).__init__(DRIVER)

        self.DRIVER = DRIVER
        self.login = login
        self.password = password

    def auth(self):

        """Authorization at the youtube"""

        self.DRIVER.get('http://youtube.com')

        # press button "Войти"
        time.sleep(random.uniform(7, 10))
        self.DRIVER.implicitly_wait(10)

        #  if self.xpath_exists('//tp-yt-paper-button[@aria-label="Accept the use of cookies and other data for the purposes described"]'):
        if self.xpath_exists(
                '//tp-yt-paper-button[@aria-label="Accept the use of cookies and other data for the purposes described"]'):
            self.DRIVER.find_element(By.XPATH,
                                     value='//tp-yt-paper-button[@aria-label="Accept the use of cookies and other data for the purposes described"]').click()
            time.sleep(random.uniform(2, 3))

        # if self.xpath_exists('//tp-yt-paper-button[@aria-label="Sign in"]'):
        if self.xpath_exists('//tp-yt-paper-button[@aria-label="Войти"]'):
            #  self.DRIVER.find_element(By.XPATH, value='//tp-yt-paper-button[@aria-label="Sign in"]').click()
            self.DRIVER.find_element(By.XPATH, value='//tp-yt-paper-button[@aria-label="Войти"]').click()

            # enter login
            time.sleep(random.uniform(7, 10))
            self.DRIVER.implicitly_wait(10)
            self.DRIVER.find_element(By.XPATH, value='//input[@type="email"]').send_keys(self.login)
            time.sleep(random.uniform(.5, 2))
            self.DRIVER.find_element(By.XPATH, value='//input[@type="email"]').send_keys(Keys.ENTER)

            # enter password
            time.sleep(random.uniform(7, 10))
            self.DRIVER.implicitly_wait(10)
            self.DRIVER.find_element(By.XPATH, value='//input[@type="password"]').send_keys(self.password)
            time.sleep(random.uniform(.5, 2))
            self.DRIVER.find_element(By.XPATH, value='//input[@type="password"]').send_keys(Keys.ENTER)

            # if self.xpath_exists('//tp-yt-paper-button[@aria-label="Sign in"]'):
            if self.xpath_exists('//tp-yt-paper-button[@aria-label="Войти"]'):
                self.auth()  # This func links on the self

    def create_chanel(self):
        pass

    def work_studia(self):

        self.DRIVER.get("https://studio.youtube.com/channel/")
        time.sleep(random.uniform(7, 10))
        # self.DRIVER.implicitly_wait(10)

        if self.xpath_exists('//ytd-channel-creation-dialog-renderer'):
            # rename chanel
            # ToDo: app register account, change photo and rename on the chanel
            self.create_chanel()

