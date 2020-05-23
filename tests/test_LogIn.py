import time

from selenium import webdriver

from PageObjects.login import Login
from utilites.BaseClass import BaseClass


class TestLogin(BaseClass):
    def test_login(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        portal = self.driver.find_element_by_xpath("//h5[@class='fw-300 m-0 pl-4 text-truncate']").text
        print("Tittle on next page" + portal)
        assert "Device Management Portal" in portal


class TestLoginInvalidEmail(BaseClass):
    def test_LoginInvalidUsername(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov8@gmail.com")
        login.getpassword().send_keys("149599Az$")
        login.getsubmit().click()
        time.sleep(5)
        alert = self.driver.find_element_by_xpath("//div[contains(text(), 'Invalid Login or Password')]").text
        print(alert)
        assert "Invalid Login or Password" in alert


class TestLoginInvalidPassword(BaseClass):
    def test_LoginInvalidPassword(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Az$")
        login.getsubmit().click()
        time.sleep(5)
        alert = self.driver.find_element_by_xpath("//div[contains(text(), 'Invalid Login or Password')]").text
        print(alert)
        assert "Invalid Login or Password" in alert

class TestLoginInvalidFormat(BaseClass):
    def test_LoginInvalidEmailFormat(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.")
        login.getpassword().send_keys("149599Az$")
        login.getsubmit().click()
        time.sleep(5)
        alert = self.driver.find_element_by_xpath("//div[contains(text(),'Email must be a valid email address')]").text
        print(alert)
        assert "Email must be a valid email address" in alert
