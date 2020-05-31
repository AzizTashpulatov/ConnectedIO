from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    UserName = (By.XPATH, "//input[@placeholder='Email address']")
    Password = (By.XPATH, "//input[@placeholder='Password']")
    Submit= (By.XPATH, "//button[@type='submit']")

    def getusername(self):
        return self.driver.find_element(*Login.UserName)
    def getpassword(self):
        return  self.driver.find_element(*Login.Password)
    def getsubmit(self):
        return  self.driver.find_element(*Login.Submit)

