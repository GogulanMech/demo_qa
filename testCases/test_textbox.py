from selenium.webdriver.common.by import By

from Utilities.readproperties import Readconfig
from Pageobjects.Elements import Text
import pytest

class Test_001_text:

    url = Readconfig.get_url()


    def test_homepage_title(self, setup):
        driver = setup
        driver.get(self.url)
        act_title = driver.title
        if act_title == "ToolsQA":
            assert True
            driver.quit()
        else:
            driver.save_screenshot("ScreenShots\\test_homepage_title.png")
            driver.quit()
            assert False
    def test_text(self, setup):
        driver = setup
        driver.get(self.url)
        txt = Text(driver)
        txt.click_element()
        txt.click_text()
        txt.set_fullname("gogulan")
        txt.set_email("gogulanknp@gmail.com")
        txt.set_currentaddress("palladam")
        txt.set_permanentaddress("Tirupur")
        txt.click_submit()
        message = driver.find_element(By.TAG_NAME, "Body")
        print(message.text)
        if "Name:gogulan" and "Email:gogulanknp@gmail.com" and "Current Address :palladam" and \
                "Permananet Address :Tirupur" in message.text:
            assert True
            driver.quit()
        else:
            driver.save_screenshot("ScreenShots\\test_text.png")
            driver.quit()
            assert False
