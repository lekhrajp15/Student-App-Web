import time
from configparser import ConfigParser
from logging import getLogger, log

from selenium.webdriver.common.by import By

from Utilities.utility import utility


class signIn_up:

    email_id = utility.readConfig('Prod', 'Email_id')
    email_password = utility.readConfig('Prod', 'Email_password')
    mobile_num = utility.readConfig('Prod', 'Mobile_number')
    mobile_password = utility.readConfig('Prod', 'Mobile_password')


    def __init__(self, driver):
        self.driver = driver


    get_started =  (By.XPATH, "//*[text() ='Get Started']")
    enter_using_password = (By.XPATH, "//*[text() ='Enter using password']")
    enter_using_OTP = (By.XPATH, "//*[text() ='Enter using OTP']")
    email_field = (By.XPATH, "//*[@name = 'email']")
    password_field = (By.XPATH, '//*[@name="password"]')
    proceed_btn = (By.XPATH, "//*[text() ='Proceed']")
    forgot_password = (By.XPATH, "//*[text() ='Forgot password?']")
    OTP_field = (By.CSS_SELECTOR, "[name='otp-input']")
    embium_icon = (By.CSS_SELECTOR, "[class='sc-lmHNfd hHTGNc']")
    learn_module = (By.CSS_SELECTOR, "[to='/learn/home']")
    # whatsapp_popup = (By.XPATH, "//*[text()='Remind me later']")

    def sign_in_with_mobile(self):
        self.driver.find_element(*signIn_up.get_started).click()
        self.driver.find_element( *signIn_up.email_field).send_keys(self.mobile_num)
        self.driver.find_element(*signIn_up.enter_using_password).click()
        time.sleep(2)
        self.driver.find_element(*signIn_up.password_field).send_keys(self.mobile_password)
        time.sleep(2)
        self.driver.find_element(*signIn_up.proceed_btn).click()

        self.driver.find_element(*signIn_up.learn_module).click()
        # try :
        #     embium_icon = self.driver.find_element(*signIn_up.embium_icon)
        #     embium_icon.is_displayed()
        #     signIn_up.log.info("Embium Icon is present")
        # except Exception as e:
        #     print(signIn_up.log.error(e))
        # time.sleep(3)
        # self.driver.find_element(*signIn_up.whatsapp_popup).click()

    def sign_in_with_email(self):
        self.driver.find_element(*signIn_up.get_started).click()
        self.driver.find_element(*signIn_up.email_field).send_keys(self.email_id)
        time.sleep(2)
        self.driver.find_element(*signIn_up.enter_using_password).click()
        self.driver.find_element(*signIn_up.password_field).send_keys(self.email_password)
        time.sleep(2)
        self.driver.find_element(*signIn_up.proceed_btn).click()
        self.driver.find_element(*signIn_up.learn_module).click()
        # try :
        #     embium_icon = self.driver.find_element(*signIn_up.embium_icon)
        #     embium_icon.is_displayed()
        #     signIn_up.log.info("Embium Icon is present")
        # except Exception as e:
        #     print(signIn_up.log.error(e))
        # time.sleep(3)
        # try:
        #     self.driver.find_element(*signIn_up.whatsapp_popup).is_displayed()
        #     self.driver.find_element(*signIn_up.whatsapp_popup).click()
        # except:
        #     pass

    def test_sign_in_password(self):
        self.driver.find_element(*signIn_up.get_started).click()
        self.driver.find_element(*signIn_up.email_field).send_keys(self.mobile_num)
        time.sleep(2)
        self.driver.find_element(*signIn_up.enter_using_password).click()
        self.driver.find_element(*signIn_up.password_field).send_keys(self.mobile_password)
        time.sleep(2)
        self.driver.find_element(*signIn_up.proceed_btn).click()

        self.driver.find_element(*signIn_up.learn_module).click()
        # time.sleep(3)
        # self.driver.find_element(*signIn_up.whatsapp_popup).click()
        # time.sleep(3)



