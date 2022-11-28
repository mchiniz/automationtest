from locator import *


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def check_main_page(self):
        self.driver.finde_element('class', button_class).click()
        self.driver.finde_element('class', devtool_class).click()
