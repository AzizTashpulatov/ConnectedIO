from selenium import webdriver

from PageObjects.login import Login
from utilites.BaseClass import BaseClass


class TestChangePassword(BaseClass):
    def test_changePassword(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        self.driver.find_element_by_xpath("//div[@class='dropdown']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Change Password')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='New Password']").send_keys("149599Aziz$")
        self.driver.find_element_by_xpath("//input[@placeholder='Confirm New Password']").send_keys("149599Aziz$")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        alert = self.driver.find_element_by_xpath("//span[@role='alert']").text

        print(alert)
        assert "Success" in alert


class TestChangePassword1(BaseClass):
    def test_OldPasswordAlert(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        self.driver.find_element_by_xpath("//div[@class='dropdown']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Change Password')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='New Password']").send_keys("149599Aziz$")
        self.driver.find_element_by_xpath("//input[@placeholder='Confirm New Password']").send_keys("149599Aziz$")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        alert = self.driver.find_element_by_xpath("//span[@role='alert']").text
        assert "Old and new password cannot be same." in alert
        print(alert)


class TestChangePassword2(BaseClass):
    def test_LessThen6charatcters(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        self.driver.find_element_by_xpath("//div[@class='dropdown']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Change Password')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='New Password']").send_keys("14959")
        self.driver.find_element_by_xpath("//input[@placeholder='Confirm New Password']").send_keys("14959")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        alert = self.driver.find_element_by_xpath("//div[contains(text(),'Password must be minimum 6 characters.')]").text
        assert "Password must be minimum 6 characters." in alert
        print(alert)


class TestChangePassword3(BaseClass):
    def test_PasswordNotMatch(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        self.driver.find_element_by_xpath("//div[@class='dropdown']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Change Password')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='New Password']").send_keys("14959")
        self.driver.find_element_by_xpath("//input[@placeholder='Confirm New Password']").send_keys("1499")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        alert = self.driver.find_element_by_xpath("//div[contains(text(),'Passwords must match')]").text
        assert "Passwords must match" in alert
        print(alert)

class TestChangePassword4(BaseClass):
    def test_PasswordNotMatch(self):
        login = Login(self.driver)

        login.getusername().send_keys("aziz.tashpulatov89@gmail.com")
        login.getpassword().send_keys("149599Aziz$")
        login.getsubmit().click()
        self.driver.find_element_by_xpath("//div[@class='dropdown']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Change Password')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='New Password']").send_keys("149596")
        self.driver.find_element_by_xpath("//input[@placeholder='Confirm New Password']").send_keys("149596")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        alert = self.driver.find_element_by_xpath(" //span[@class='alert w-100 alert-warning']").text
        assert "Password should contain one alphabet and a number." in alert
        print(alert)


