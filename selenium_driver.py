""" This file work with Selenium """

import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseClass:

    def __init__(self, DRIVER=None):  # add user-agent
        self.DRIVER = DRIVER

    def driver(self):

        chrome_options = uc.ChromeOptions()

        #chrome_options.add_argument("--disable-gpu") # if headless
        chrome_options.add_argument("--disable-extensions")  # отключает рассширения
        chrome_options.add_argument("--disable-popup-blocking")  # отключает блокировку всплывающих окон
        chrome_options.add_argument("--incognito")

        # chrome_options.headless = True
        # chrome_options.add_argument('--headless')

        self.DRIVER = uc.Chrome(options=chrome_options)
        self.DRIVER.delete_all_cookies()
        self.DRIVER.maximize_window()

        return self.DRIVER


    def xpath_exists(self, xpath):

        try:
            self.DRIVER.implicitly_wait(15)
            self.DRIVER.find_element(By.XPATH, value=xpath)
            exist = True
        except NoSuchElementException:
            exist = False

        return exist