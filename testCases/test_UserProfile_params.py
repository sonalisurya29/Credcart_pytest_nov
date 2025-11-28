import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from Utilities.readproperties import Readconfig
# from testCases.conftest import getDataForRegisteration


class Test_User_Profile_Params:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Name = Readconfig.getname()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    Confirmpass = Readconfig.getConfirmPassword()

    # def test_UserRegistrationPparams_001(self, setup):
    #     self.driver = setup
    #     self.ur = UserProfile_Class(self.driver)
    #     # 2 go to registration url
    #     self.driver.get(self.RegistrationUrl)
    #
    #     # 3 Enter Name
    #     self.ur.Enter_Name(self.Name)
    #
    #     # 4 Enter EMail Id
    #     self.ur.Enter_Email(self.Username)
    #
    #     # 5 Enter Password
    #     self.ur.Enter_Password(self.Password)
    #
    #     # 6 Enter Confirm Password
    #     self.ur.Enter_ConfirmPassword(self.Confirmpass)
    #
    #     # 7 Click on Register button
    #     self.ur.Click_Login_Or_RegisterButton()
    #
    #     if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
    #         if getDataForRegisteration[4] == "Pass":
    #             self.driver.save_screenshot(
    #                 "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Pass.png")
    #
    #             assert True
    #         elif getDataForRegisteration[4] == "Fail":
    #             self.driver.save_screenshot(
    #                 "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Pass.png")
    #             assert False
    #
    #     else:  # Login Fail
    #         if getDataForRegisteration[4] == "Pass":
    #             self.driver.save_screenshot(
    #                 "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Pass.png")
    #
    #             assert False
    #         elif getDataForRegisteration[4] == "Fail":
    #             self.driver.save_screenshot(
    #                 "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Pass.png")
    #             assert True
    #
    #         self.driver.save_screenshot(
    #             "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Fail.png")

    def test_UserLogin_Params_005(self, setup, getDataForLogin):
        self.driver = setup
        self.driver.get(self.LoginUrl)
        self.ur = UserProfile_Class(self.driver)
        self.ur.Enter_Email(getDataForLogin[0])
        print("Username-->" + getDataForLogin[0])
        self.ur.Enter_Password(getDataForLogin[1])
        print("Password-->" + getDataForLogin[1])
        self.ur.Click_Login_Or_RegisterButton()
        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                    "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Pass.png")

                assert True
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Pass.png")
                assert False

        else:  # Login Fail
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                    "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Pass.png")

                assert False
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Pass.png")
                assert True

            self.driver.save_screenshot(
                "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Fail.png")

# pytest -v --html=HTMLReports/Edge_Report.html --browser edge -n=3 --alluredir="C:\Users\HP\Desktop\Python revision Jan 24\Pytest_Credkart\AllureReports"
# allure serve "folder Path"

# pytest -v --html=HTMLReports/Firefox.html --browser firefox -n=3 --alluredir="C:\Users\Govind\Desktop\recording\pytes_framework_by_tushar_sir\selenium (6) 7 jan 2024\7_jan _Py\Pytest_Credkart\AllureReports"
#
# pytest -v --html=HTMLReports/Chrome.html --browser chrome -n=3 --alluredir="C:\Users\Govind\Desktop\recording\pytes_framework_by_tushar_sir\selenium (6) 7 jan 2024\7_jan _Py\Pytest_Credkart\AllureReports"
# allure serve "C:\Users\Govind\Desktop\recording\pytes_framework_by_tushar_sir\selenium (6) 7 jan 2024\7_jan _Py\Pytest_Credkart\AllureReports"
# config -- > url, login id pass
# Logs
# Data Driven Test Case
