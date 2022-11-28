from locator import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class DevTool:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver=driver)

    def check_dev_tool(self,query):
        self.driver.find_element("id", text_area_id).click()
        self.actions.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()
        self.driver.find_element('id', text_area_id).send_keys(query)
        self.driver.find_element('class', send_request_botton).click()



