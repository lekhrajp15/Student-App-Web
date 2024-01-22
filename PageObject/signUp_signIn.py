import time
from logging import getLogger, log

from selenium.webdriver.common.by import By

from PageObject.learn_home_page import LearnHomePage


class signIn_up:
    log = getLogger()

    def __init__(self, driver):
        self.driver = driver


    get_started =  (By.XPATH, "//*[text() ='Get Started']")
    enter_using_password = (By.XPATH, "//*[text() ='Enter using password']")
    enter_using_OTP = (By.XPATH, "//*[text() ='Enter using OTP']")
    email_field = (By.XPATH, "//*[@placeholder = 'Student Mobile / Email']")
    password_field = (By.XPATH, '//*[@name="password"]')
    proceed_btn = (By.XPATH, "//*[text() ='Proceed']")
    forgot_password = (By.XPATH, "//*[text() ='Forgot password?']")
    OTP_field = (By.CSS_SELECTOR, "[name='otp-input']")
    embium_icon = (By.CSS_SELECTOR, "[class='sc-lmHNfd hHTGNc']")
    learn_module = (By.CSS_SELECTOR, "[to='/learn/home']")





    def sign_in_with_mobile(self):
        self.driver.find_element(*signIn_up.get_started).click()
        self.driver.find_element( *signIn_up.email_field).send_keys("lekhraj.p+15@embibe.com")
        self.driver.find_element(*signIn_up.enter_using_password).click()
        self.driver.find_element(*signIn_up.password_field).send_keys("Embibe@1234")
        self.driver.find_element(*signIn_up.proceed_btn).click()
        self.driver.find_element(*signIn_up.learn_module).click()
        try :
            embium_icon = self.driver.find_element(*signIn_up.embium_icon)
            embium_icon.is_displayed()
            signIn_up.log.info("Embium Icon is present")
        except Exception as e:
            print(signIn_up.log.error(e))

    def sign_in_with_email(self):
        self.driver.find_element(*signIn_up.get_started).click()
        self.driver.find_element(*signIn_up.email_field).send_keys("lekhraj.p+15@embibe.com")
        self.driver.find_element(*signIn_up.enter_using_password).click()
        self.driver.find_element(*signIn_up.password_field).send_keys("Embibe@1234")
        self.driver.find_element(*signIn_up.proceed_btn).click()
        self.driver.find_element(*signIn_up.learn_module).click()
        try :
            embium_icon = self.driver.find_element(*signIn_up.embium_icon)
            embium_icon.is_displayed()
            signIn_up.log.info("Embium Icon is present")
        except Exception as e:
            print(signIn_up.log.error(e))

    def test_sign_in_password(self):
        self.driver.find_element(*signIn_up.get_started).click()
        self.driver.find_element(*signIn_up.email_field).send_keys("lekhraj.p+15@embibe.com")
        self.driver.find_element(*signIn_up.enter_using_password).click()
        self.driver.find_element(*signIn_up.password_field).send_keys("Embibe@1234")
        self.driver.find_element(*signIn_up.proceed_btn).click()
        time.sleep(5)
        self.driver.find_element(*signIn_up.learn_module).click()



