import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from Utilities.readproperties import Readconfig
from Utilities.Logger import Logging_Class

class Test_User_Profile:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    log = Logging_Class.log_genarator()

    def test_UserRegistration_001(self, setup):
        self.log.info("test_UserRegistration_001 is started")
        # self.log.debug("this is debug log")
        # self.log.info("this is info log")
        # self.log.warning("this is warning log")
        # self.log.error("this is error log")
        # self.log.critical("this is critical log")
        self.driver = setup
        self.log.info(" Opening Browser")
        # 1 Browser Open
        # self.driver = webdriver.Firefox()
        self.ur = UserProfile_Class(self.driver)
        # 2 Go to registration url
        self.driver.get(self.RegistrationUrl)
        self.log.info("Going to Url-->" + self.RegistrationUrl)

        # 3 Enter Name
        # driver.find_element(By.ID, 'name').send_keys("Rohit")
        self.ur.Enter_Name("Rohit")
        self.log.info("Entering the name")

        # 4 Enter EMail Id
        # self.driver.find_element(By.ID, 'email').send_keys("Rohit3442@credence.in")
        email = Generate_Email()
        self.ur.Enter_Email(email)
        self.log.info("Entering the Email-->" + email)
        #print(email)

        # 5 Enter Password
        # self.driver.find_element(By.ID, 'password').send_keys("rohit@123")
        self.ur.Enter_Password("Test123")
        self.log.info("Entering the password")

        # 6 Enter Confirm Password
        # self.driver.find_element(By.ID, "password-confirm").send_keys("rohit@123")
        self.ur.Enter_ConfirmPassword("Test123")
        self.log.info("Entering the confirm password")

        # 7 Click on Register button
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        self.ur.Click_Login_Or_RegisterButton()
        self.log.info("Clicking on Register Button")

        # 7 Validate Registration
        # try:
        #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        #     print("Registration Pass")
        #     assert True
        # except:
        #     print("Registration Fail")
        #     assert False

        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            self.log.info("test_UserRegistration_001 is pass")
            self.driver.save_screenshot(
                "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Registration_Pass.png")
            # self.driver.close()
            assert True
        else:
            self.log.info("test_UserRegistration_001 is fail")
            self.driver.save_screenshot(
                "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Registration_Fail.png")
            # self.driver.close()
            assert False
        self.log.info("test_UserRegistration_001 is completed")





    def test_UserLogin_002(self, setup):
        self.log.info("test_UserLogin_002 is started")
        self.driver = setup
        self.log.info(" Opening Browser")

        # 1 Browser Open
        # 2 Go to Url https://automation.credence.in/login
        self.driver.get(self.LoginUrl)
        self.ur = UserProfile_Class(self.driver)
        self.log.info(" Going to login Url-->"+ self.LoginUrl)
        # 3 Enter email
        # driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Rohit344@credence.in")
        self.ur.Enter_Email(self.Username)
        self.log.info(" Entering email"+ self.Username)
        # 4 Enter Password
        # driver.find_element(By.XPATH, "//input[@id='password']").send_keys("rohit@123")
        self.ur.Enter_Password(self.Password)
        self.log.info(" Entering password" + self.Password)
        # 5 Click on Login button
        # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.ur.Click_Login_Or_RegisterButton()
        # 6 Validate Login
        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            self.log.info(" logging Success" )
            self.driver.save_screenshot(
                "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Pass.png")

            # self.driver.close()
            assert True
        else:
            self.log.info(" logging Fail")
            self.driver.save_screenshot(
                "F:\\Sonali\\python revision nov\\Pytest_credframework\\Screenshots\\Login_Fail.png")

            # self.driver.close()
            assert False
        self.log.info("test_UserLogin_002 is completed")

def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=4))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"

# pytest -v --html=HTMLReports/Chrome_Report.html --browser chrome -n=5 --alluredir="C:\Users\Govind\Desktop\recording\pytes_framework_by_tushar_sir\selenium-8 -part 9-jan-2024 logs file & ddt\Pytest_Credkart - Copy - Copy\AllureReports"
# allure serve "folder Path"
# allure serve "C:\Users\Govind\Desktop\recording\pytes_framework_by_tushar_sir\selenium-8 -part 9-jan-2024 logs file & ddt\Pytest_Credkart - Copy - Copy\AllureReports"
#
# pytest -v --html=HtmlReports/24dempreports.html "F:\Sonali\python revision nov\Pytest_credframework\testCases\test_UserProfile.py" --alluredir="F:\Sonali\python revision nov\Pytest_credframework\AllureReports"

#

# config -- > url, login id pass
# Logs
# Data Driven Test Case
