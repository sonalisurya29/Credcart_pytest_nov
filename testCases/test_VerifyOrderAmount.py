import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from pageObjects.VerifyOrderAmount_Page import VerifyOrderAmount_Class


class Test_VerifyAmount:

    def test_VerifyAmount(self, setup):
        self.driver = setup
        self.ur = UserProfile_Class(self.driver)
        self.voa = VerifyOrderAmount_Class(self.driver)

        self.driver.get("https://automation.credence.in/login")

        self.ur.Enter_Email("Rohits@credence.in")
        self.ur.Enter_Password("Rohit123")
        self.ur.Click_Login_Or_RegisterButton()
        self.voa.Click_AppleMocBook()
        self.voa.Click_AddToCart()
        self.voa.Click_ContinueShoppingButton()
        self.voa.Click_AppleIPad()
        self.voa.Click_AddToCart()
        self.voa.Click_ContinueShoppingButton()
        self.voa.Click_HeadPhone()
        self.voa.Click_AddToCart()
        if self.voa.Validate_Amount() == "Amount is Matched":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False


