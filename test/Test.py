import sys
from pathlib import Path
import os

parents_path = Path(__file__).parents
project_root = os.path.abspath(parents_path[2])
sys.path.append(project_root)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Page.login import Login
from Page.MainPage import MainPage
from Page.DevTool import DevTool
import unittest
from time import sleep
from selenium.webdriver.chrome.service import Service


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test1(self):
        self.driver.get("https://127.0.0.1:5601")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        dev_tool = DevTool(driver=self.driver)
        login.enter_username("elastic")
        login.enter_password("password")
        login.click_on_login_button()
        main_page.check_main_page()
        query = "curl -X GET 'http://localhost:9200/hello_world/_search?pretty=true' \
             -H 'content-type: application/json' " \
                "GET /my-index-000001/_search" + str({
            "timeout": "2s",
            "query": {
                "match": {
                    "my-index-000001.message": "hello_world"
                }
            }
        })

        dev_tool.check_dev_tool(query=query)
        sleep(1)

    def test2(self):
        self.driver.get("https://127.0.0.1:5601")
        login = Login(driver=self.driver)
        login.enter_username("elastic")
        login.enter_password("password2")
        login.click_on_login_button()
        sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
