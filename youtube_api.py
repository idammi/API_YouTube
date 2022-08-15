import re

from selenium_driver import BaseClass

import work_with_file_system as work_fs

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import random


class YouTube(BaseClass):

    def __init__(self, DRIVER):
        super(YouTube, self).__init__(DRIVER)

        self.DRIVER = DRIVER


    def auth(self, login=str, password=str):

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
            self.DRIVER.find_element(By.XPATH, value='//input[@type="email"]').send_keys(login)
            time.sleep(random.uniform(.5, 2))
            self.DRIVER.find_element(By.XPATH, value='//input[@type="email"]').send_keys(Keys.ENTER)

            # enter password
            time.sleep(random.uniform(7, 10))
            self.DRIVER.implicitly_wait(10)
            self.DRIVER.find_element(By.XPATH, value='//input[@type="password"]').send_keys(password)
            time.sleep(random.uniform(.5, 2))
            self.DRIVER.find_element(By.XPATH, value='//input[@type="password"]').send_keys(Keys.ENTER)

            # if self.xpath_exists('//tp-yt-paper-button[@aria-label="Sign in"]'):
            if self.xpath_exists('//tp-yt-paper-button[@aria-label="Войти"]'):
                self.auth()  # This func links on the self

            return self.welcome_studio()

    def create_chanel(self):
        pass

    def welcome_studio(self):

        self.DRIVER.get("https://studio.youtube.com/channel/")
        time.sleep(random.uniform(7, 10))

        # creater chanek if new account
        if self.xpath_exists('//ytd-channel-creation-dialog-renderer'):
            # rename chanel xpath '//input[@aria-labelledby="paper-input-label-1"]'
            # button create chanel '//tp-yt-paper-button[@aria-label="СОЗДАТЬ КАНАЛ"]'
            # ToDo: app register account, change photo and rename on the chanel
            self.create_chanel()
            time.sleep(random.uniform(1, 2))

        # This table showing after creating new chanel(first enter)
        if self.xpath_exists('//div[text()="Далее"]'):
            self.DRIVER.find_element(By.XPATH, value='//div[text()="Далее"]').click()
            time.sleep(random.uniform(3, 5))

    def checker_copyright(self):

        # checker copyright(авторское право)
        copyright = self.DRIVER.find_element(By.XPATH, value='//div[@id="results-description"]').text()
        if copyright == 'Нарушений не найдено.':
            print("Авторское право не нарушено")

        elif re.findall(fr'(?im)\bВладелец разрешает\S*\b', copyright) == "Владелец разрешает":
            print("Авторское право нарушено!")

        else:
            print(copyright)
            raise Exception("video is blocked or prohibited by copyright")


    # press botton "Upload video"
    def page1_upload_video(self, path_to_video=str):

        # field for upload vidio on the youtube
        if self.xpath_exists('//input[@type="file"]'):
            print("Loadin video...")
            self.DRIVER.find_element(By.XPATH, value='//input[@type="file"]').send_keys(path_to_video)
            print("Video Uploaded")

    def page2_upload_video(self, title=str, tags=str):

        # title
        self.DRIVER.implicitly_wait(10)
        self.DRIVER.find_element(By.XPATH, value='//div[@id="textbox"]').clear()
        self.DRIVER.find_element(By.XPATH, value='//div[@id="textbox"]').send_keys(title)

        # radio-button "for kids"
        while not self.xpath_exists('//paper-ripple[@checked]'):

            # check exists the radio-button "for kids"
            if self.xpath_exists('//tp-yt-paper-radio-button[@name="VIDEO_MADE_FOR_KIDS_MFK"]'):

                # click on the radio-button "for kids"
                self.DRIVER.find_elements('//tp-yt-paper-radio-button[@name="VIDEO_MADE_FOR_KIDS_MFK"]/div/div')[1].click()

            else:
                print('xpath radio "for kids" don\'t work')
        else:
            print('radio "for kids" turns on')

            # open new param, pressed button "Развернуть"
            self.DRIVER.find_element(By.XPATH, value='//div[text()="Развернуть"]').click()

            # add tags
            time.sleep(random.uniform(5, 8))
            self.DRIVER.implicitly_wait(10)
            self.DRIVER.find_element(By.XPATH, value='//input[@aria-label="Теги"]').clear()
            self.DRIVER.find_element(By.XPATH, value='//input[@aria-label="Теги"]').send_keys('#shorts' + str(tags))

        # press button "Next"
        if self.xpath_exists('//div[text()="Далее"]'):

            # from page "information" to "Adds"
            self.DRIVER.find_elements('//div[text()="Далее"]')[1].click()

    def page3_upload_video(self):
        # from page "Adds" to "Checker YouTube"
        time.sleep(random.uniform(2, 4))
        self.DRIVER.implicitly_wait(10)
        self.DRIVER.find_elements('//div[text()="Далее"]')[1].click()

    def page4_upload_video(self):

        # check uploaded video on the copyright and baneded content
        self.checker_copyright()

        # from page "Checker YouTube" to access
        time.sleep(random.uniform(2, 4))
        self.DRIVER.implicitly_wait(10)
        self.DRIVER.find_elements('//div[text()="Далее"]')[1].click()

    def page5_upload_video(self):
        # select radio-button public access
        time.sleep(random.uniform(1, 4))
        self.DRIVER.implicitly_wait(10)
        self.DRIVER.find_element('//tp-yt-paper-radio-button[@name="PUBLIC"]/div').click()

        # while upload not completed
        def status():
            status_now = self.DRIVER.find_element(
                '//span[@class="progress-label style-scope ytcp-video-upload-progress"]').text()
            print(status_now)
            if not status_now.split(".")[0] == "Проверка завершена":
                status()

        status()

        # press button upload
        time.sleep(random.uniform(1, 4))
        self.DRIVER.implicitly_wait(10)
        self.DRIVER.find_element('//ytcp-button[@id="done-button"]').click()

    def upload_video(self, path_to_file=str, title=str, tags=str):
        # press button "upload video" on the studia YouTube
        if self.xpath_exists('//ytcp-icon-button[@id="upload-icon"]'):
            self.DRIVER.find_element(By.XPATH, value='//ytcp-icon-button[@id="upload-icon"]').click()

        time.sleep(random.uniform(5, 8))

        # pass page #1 for uploated video on the Youtube
        self.page1_upload_video(path_to_video=path_to_file)

        self.page2_upload_video(title=title, tags=tags)

        self.page3_upload_video()

        self.page4_upload_video()

        self.page5_upload_video()

        # press button "Close"
        time.sleep(random.uniform(1, 4))
        self.DRIVER.implicitly_wait(10)
        self.DRIVER.find_element('//div[text()="Закрыть"]').click()

        time.sleep(20)

    # ToDO: через map iter func and list video
    # ToDo: checker exists file or video in dir
    # ToDo: del vidos при нарушении авторских прав, можно відівать ошибку