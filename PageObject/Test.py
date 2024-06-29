import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

Chrome_option = Options()
Chrome_option.add_argument("--disable-notifications")
obj= Service("/Users/lekhraj/PycharmProjects/EmbibeFramework/browsers driver/chromedriver")
driver = webdriver.Chrome(service=obj, options=Chrome_option)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.embibe.com")
driver.find_element(By.XPATH,"//*[text()='Get Started']").click()
driver.find_element(By.NAME, "email").send_keys("lekhraj.p+15@embibe.com")
driver.find_element(By.XPATH, "//*[text()='Enter using password']").click()
driver.find_element(By.NAME, "password").send_keys("Embibe@1234")
driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "//*[text()='Test']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//*[contains(text(),'Trending Tests for Your Exam')]/parent::div/div[2]/div[2]/div/div[3]/div/div/div").click()
btn = driver.find_element(By.CSS_SELECTOR, "[class='eds-btn eds-btn--primary eds-btn--capsular eds-btn--md']").text
print(btn)

try:
    if btn == 'Start Test':
        driver.find_element(By.XPATH, "//*[text()='Start Test']").click()
        time.sleep(10)
        # popup = driver.find_element(By.XPATH, "//*[@id='app']/main/div[3]/div/div/div")
        # if popup.is_displayed():
        #     driver.find_element(By.XPATH, "//*[text()= 'Show me the EMBIBE Experience']").click()
        #     driver.find_element(By.XPATH, "//*[contains(text(), 'I have ')]").click()
        #     driver.find_element(By.XPATH, "//*[text()='Start Now']").click()
        #
        # else:
        driver.find_element(By.XPATH, "//*[contains(text(), 'I have ')]").click()
        driver.find_element(By.XPATH, "//*[text()='Start Now']").click()
    elif btn == 'Resume':
        driver.find_element(By.XPATH, "//*[text()='Resume']").click()

    time.sleep(5)

    questions = len(driver.find_elements(By.XPATH, "//div[@id='app']/main/div/div/div[4]/div[2]/div/div"))

    print(questions)

    for i in range(1, questions):
        time.sleep(3)
        question = driver.find_element(By.XPATH,
                                       "//body/div[@id='app']/main[1]/div[1]/div[1]/div[3]/div[1]/span[2]").text
        print(question)

        if question == 'Single Choice':
            driver.find_element(By.XPATH,
                                "//div[@id='app']/main/div/div/div[4]/div/div[1]/div/div/div/div[2]/div[1]").click()

            driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()


        elif question == "Multiple Choice":
            driver.find_element(By.XPATH,
                                "//div[@id='app']/main/div/div/div[4]/div/div[1]/div/div/div/div[2]/div[1]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()


        elif question == "True-False":
            time.sleep(3)
            # driver.find_element(By.XPATH, "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").click()
            # driver.find_element(By.XPATH, "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").send_keys("Lekh")
            driver.find_element(By.XPATH,
                                "//div[@id='app']/main/div/div/div[4]/div/div[1]/div/div/div/div[2]/div[1]").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()

        elif question == "Subjective Answer":
            try:
                time.sleep(3)
                driver.find_element(By.XPATH, "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").click()
                driver.find_element(By.XPATH, "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").send_keys("XYZ")
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
            except NoSuchElementException:
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
            except ElementNotInteractableException:
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()

        elif question == "Subjective Numerical":
            try:
                time.sleep(3)
                driver.find_element(By.XPATH, "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").click()
                driver.find_element(By.XPATH, "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").send_keys("123")
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
            except NoSuchElementException:
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
            except ElementNotInteractableException:
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()

        elif question == "Fill in The Blanks":
            try:
                time.sleep(3)
                driver.find_element(By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]").click()
                driver.find_element(By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]").send_keys("Answer")
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
            except NoSuchElementException:
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
            except ElementNotInteractableException:
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()

        elif question == "Single DropDown":
            try:
                driver.find_element(By.XPATH, "//*[text()='select']").click()
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
            except NoSuchElementException:
                driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
        else:
            driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
    driver.find_element(By.XPATH, "//*[contains(text(),'Submit Test')]").click()
    driver.find_element(By.XPATH, "//*[@id='app']/main/div/div/div/div[1]/div/div[4]/div[1]/button[1]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'View Test Feedback')]").click()


except Exception as e:
    if btn == 'View Test Feedback':
        print("Test already Taken")
    else:
        print(f"An error occurred: {e}")