import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_argument('--disable-notifications')
driver = webdriver.Chrome(options=option)

def achieve():
    option = Options()
    option.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get("https://www.embibe.com/signup")
    time.sleep(5)
    # driver.find_element(By.XPATH, '//*[@id="app"]/main/div[2]/div[1]/div[1]/div/div/div[2]/div/div[2]/button').click()
    driver.find_element(By.XPATH, '//*[@name="email"]').send_keys("9035371071")
    driver.find_element(By.XPATH, '//*[text()="Enter using password"]').click()
    driver.find_element(By.XPATH, '//*[@name="password"]').send_keys("Embibe@1")
    driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[1]/div/form/div[4]/div/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[text()="Achieve"]').click()
    time.sleep(5)

    # driver.execute_script("arguments[0].scrollIntoView();" ,achieve_now_btn)
    #
    # achieve_now_btn.click()
    try:
        driver.execute_script("window.scrollBy(0, 600);")
        start_achieving_btn = driver.find_element(By.XPATH, '//*[text()="Start Achieving Now"]')
        if start_achieving_btn.is_displayed():
            start_achieving_btn.click()
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[contains(text(), " Start your ")]').click()
            time.sleep(5)

            # Locate and click all the sub-elements
            sub_elements = driver.find_elements(By.XPATH,
                                                '//div[@class="eds-col-xs-12 eds-col-sm-3 eds-col-md-3 eds-col-lg-3"]/div')
            for sub_element in sub_elements:
                sub_element.click()
        else:
            raise Exception("Button not displayed")  # This will trigger the scroll action in the except block
    except:
        # Scroll down and perform an action if the button is not found or not displayed
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(5)

        # driver.find_element(By.CSS_SELECTOR, "[class='create-achieve-journey-text-wrapper']").click()
        # time.sleep(5)



    sub_elements = driver.find_elements(By.XPATH,
                                        '//div[@class="eds-col-xs-12 eds-col-sm-3 eds-col-md-3 eds-col-lg-3"]/div')
    print(len(sub_elements))
    for i in range(1, len(sub_elements)):
        driver.find_element(By.XPATH,
                             '//div[@class="eds-col-xs-12 eds-col-sm-3 eds-col-md-3 eds-col-lg-3"]/div['+str(i)+']').click()

    driver.find_element(By.XPATH, "//span[text()='Continue']").click()
    chapter_sel = driver.find_elements(By.XPATH, "//div[@class='chapter-selection-wrapper--subjects eds-col-md-3 eds-col-lg-3']/div")

    for k in chapter_sel:
        k.click()
        driver.find_element(By.XPATH, '//*[text()="All Chapters"]').click()

    driver.find_element(By.XPATH, "//span[text()='Continue']").click()
    time.sleep(20)
    test_Taking()
    test_Taking()



def test_Taking():
       btn = driver.find_element(By.CSS_SELECTOR,
                                 "[class='eds-btn eds-btn--tertiary eds-btn--capsular eds-btn--md test-button']").text
       print(btn)

       try:
           if btn == 'Start Test':
               driver.find_element(By.XPATH, "//*[text()='Start Test']").click()
               time.sleep(10)
               driver.find_element(By.XPATH, "//*[contains(text(), 'I have ')]").click()
               time.sleep(5)
               driver.find_element(By.XPATH, "//*[text()='Start Now']").click()
               time.sleep(5)
           elif btn == 'Resume':
               print("resume")
               driver.find_element(By.XPATH, "//*[text()='Resume']").click()
               time.sleep(10)

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
                       driver.find_element(By.XPATH,
                                           "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").click()
                       driver.find_element(By.XPATH,
                                           "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").send_keys(
                           "XYZ")
                       driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
                   except NoSuchElementException:
                       driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
                   except ElementNotInteractableException:
                       driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()

               elif question == "Subjective Numerical":
                   try:
                       time.sleep(3)
                       driver.find_element(By.XPATH,
                                           "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").click()
                       driver.find_element(By.XPATH,
                                           "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input").send_keys(
                           "123")
                       driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
                   except NoSuchElementException:
                       driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()
                   except ElementNotInteractableException:
                       driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()

               elif question == "Fill in The Blanks":
                   try:
                       time.sleep(3)
                       driver.find_element(By.XPATH,
                                           "//body/div[@id='app']/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]").click()
                       driver.find_element(By.XPATH,
                                           "//body/div[@id='app']/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]").send_keys(
                           "Answer")
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
           time.sleep(3)
           driver.find_element(By.XPATH, "//*[contains(text(),'Submit Test')]").click()
           time.sleep(5)
           driver.find_element(By.XPATH, "//*[contains(text(),'Continue to Achieve')]").click()
           time.sleep(10)



       except Exception as e:
           print(f"An error occurred: {e}")



achieve()
