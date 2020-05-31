import time

from selenium import webdriver

from PageObjects.login import Login
from utilites.BaseClass import BaseClass


class TestLogout(BaseClass):
    def test_Logout1(self):
        login=Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        self.driver.find_element_by_xpath("//div[@class='dropdown']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        logout= self.driver.find_element_by_xpath("//h2[@class='text-uppercase font-weight-bold my-4']").text
        print(logout)
        assert "LOGIN" in logout
class TestLogout2(BaseClass):
    def test_Logout2(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        self.driver.find_element_by_xpath("//i[@class='fas fa-sign-out-alt']").click()
        time.sleep(5)
        logout= self.driver.find_element_by_xpath("//h2[@class='text-uppercase font-weight-bold my-4']").text
        print(logout)
        assert "LOGIN" in logout