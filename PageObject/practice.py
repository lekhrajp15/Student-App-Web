import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

from PageObject.learn_home_page import LearnHomePage

Chrome_option = Options()
Chrome_option.add_argument("--disable-notifications")
obj= Service("/Users/lekhraj/PycharmProjects/EmbibeFramework/browsers driver/chromedriver")
driver = webdriver.Chrome(service=obj, options=Chrome_option)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.embibe.com/test/home")
driver.find_element(By.XPATH,"//*[text()='Get Started']").click()
driver.find_element(By.NAME, "email").send_keys("lekhraj.p+15@embibe.com")
time.sleep(3)
driver.find_element(By.XPATH, "//*[text()='Enter using password']").click()
driver.find_element(By.NAME, "password").send_keys("Embibe@1234")
time.sleep(3)
driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element(By.XPATH, "//div[text()='My Custom Tests']/parent::div[1]/div/div[1]/div/div[1]/div/div/div").click()
ele =driver.find_elements(By.XPATH, "//div[contains(@class, 'test-subjects-wrapper--subject-selection')]/div/div/div[3]/div/div")
print(len(ele))

for i in range (1, len(ele)):
    driver.find_element(By.XPATH, "//div[contains(@class, 'test-subjects-wrapper--subject-selection')]/div/div/div[3]/div/div["+str(i)+"]").click()
    time.sleep(3)

driver.find_element(By.XPATH, "//span[text()='Next']").click()
chapters_count =driver.find_elements(By.XPATH, "//div[contains(@class,'test-chapters-wrapper--subjects hide')]/div")

for i in range (1, len(chapters_count)+1):
    driver.find_element(By.XPATH, "//div[contains(@class,'test-chapters-wrapper--subjects hide')]/div["+str(i)+"]").click()
    driver.find_element(By.XPATH, "//span[text()= 'All Chapters']").click()
    time.sleep(3)

driver.find_element(By.XPATH, "//span[text()='Quick 5 Minute Test']").click()


