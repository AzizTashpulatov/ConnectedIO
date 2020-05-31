import time

from selenium import webdriver

from PageObjects.login import Login
from utilites.BaseClass import BaseClass



class TestDashboard(BaseClass):
    def test_Cards(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()

        titles= len(self.driver.find_elements_by_xpath("//h6[@class]"))
        assert titles==8
        title = self.driver.find_elements_by_xpath("//h6[@class]")
        for x in title:
            print(x.text)


class TestSections(BaseClass):
    def test_DiviceOnline(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        self.driver.find_element_by_xpath("//div[contains(@class,'col col1 dvice_online')]").click()
        status=self.driver.find_element_by_xpath("//span[contains(@class,'pr-2')]").text
        print(status)
        assert status=="Online"

class TestSection1(BaseClass):
    def test_DiviceOffline(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        self.driver.find_element_by_xpath("//div[contains(@class,'col col2 dvice_offline')]").click()
        status=self.driver.find_element_by_xpath("//span[contains(@class,'pr-2')]").text
        print(status)
        assert status=="Offline"










































