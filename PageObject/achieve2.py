from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    options = Options()
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def login(driver):
    driver.get("https://www.embibe.com/signup")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="email"]')))
    driver.find_element(By.XPATH, '//*[@name="email"]').send_keys("9035371071")
    driver.find_element(By.XPATH, '//*[text()="Enter using password"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="password"]')))
    driver.find_element(By.XPATH, '//*[@name="password"]').send_keys("Embibe@1")
    driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[1]/div/form/div[4]/div/button').click()

def navigate_to_achieve(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Achieve"]')))
    driver.find_element(By.XPATH, '//*[text()="Achieve"]').click()

def start_achieving(driver):
    try:
        driver.execute_script("window.scrollBy(0, 600);")
        start_achieving_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Start Achieving Now"]')))
        start_achieving_btn.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), " Start your ")]')))
        driver.find_element(By.XPATH, '//*[contains(text(), " Start your ")]').click()
    except Exception as e:
        print(f"Error starting achieve: {e}")
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(5)

def select_sub_elements(driver):
    sub_elements = driver.find_elements(By.XPATH, '//div[@class="eds-col-xs-12 eds-col-sm-3 eds-col-md-3 eds-col-lg-3"]/div')
    for sub_element in sub_elements:
        sub_element.click()
    driver.find_element(By.XPATH, "//span[text()='Continue']").click()

def select_chapters(driver):
    chapter_sel = driver.find_elements(By.XPATH, "//div[@class='chapter-selection-wrapper--subjects eds-col-md-3 eds-col-lg-3']/div")
    for chapter in chapter_sel:
        chapter.click()
        driver.find_element(By.XPATH, '//*[text()="All Chapters"]').click()
    driver.find_element(By.XPATH, "//span[text()='Continue']").click()

def test_taking(driver):
    try:
        btn = driver.find_element(By.CSS_SELECTOR, "[class='eds-btn eds-btn--tertiary eds-btn--capsular eds-btn--md test-button']").text
        if btn == 'Start Test':
            driver.find_element(By.XPATH, "//*[text()='Start Test']").click()
            time.sleep(10)
            driver.find_element(By.XPATH, "//*[contains(text(), 'I have ')]").click()
            time.sleep(5)
            driver.find_element(By.XPATH, "//*[text()='Start Now']").click()
            time.sleep(5)
        elif btn == 'Resume':
            driver.find_element(By.XPATH, "//*[text()='Resume']").click()
            time.sleep(10)

        questions = driver.find_elements(By.XPATH, "//div[@id='app']/main/div/div/div[4]/div[2]/div/div")
        for i in range(len(questions)):
            time.sleep(3)
            question_type = driver.find_element(By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[1]/div[3]/div[1]/span[2]").text
            handle_question(driver, question_type)

        driver.find_element(By.XPATH, "//*[contains(text(),'Submit Test')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[contains(text(),'Submit Test')]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[contains(text(),'Continue to Achieve')]").click()
        time.sleep(10)
    except Exception as e:
        print(f"An error occurred during test taking: {e}")

def handle_question(driver, question_type):
    if question_type == 'Single Choice':
        driver.find_element(By.XPATH, "//div[@id='app']/main/div/div/div[4]/div/div[1]/div/div/div/div[2]/div[1]").click()
    elif question_type == "Multiple Choice":
        driver.find_element(By.XPATH, "//div[@id='app']/main/div/div/div[4]/div/div[1]/div/div/div/div[2]/div[1]").click()
    elif question_type == "True-False":
        driver.find_element(By.XPATH, "//div[@id='app']/main/div/div/div[4]/div/div[1]/div/div/div/div[2]/div[1]").click()
    elif question_type == "Subjective Answer" or question_type == "Subjective Numerical":
        try:
            input_element = driver.find_element(By.XPATH, "//*[@id='app']/main/div[1]/div/div[4]/div[1]/div[1]/div/div/div/input")
            input_element.click()
            input_element.send_keys("XYZ" if question_type == "Subjective Answer" else "123")
        except Exception:
            pass
    elif question_type == "Fill in The Blanks":
        try:
            input_element = driver.find_element(By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
            input_element.click()
            input_element.send_keys("Answer")
        except Exception:
            pass
    elif question_type == "Single DropDown":
        try:
            driver.find_element(By.XPATH, "//*[text()='select']").click()
        except Exception:
            pass
    driver.find_element(By.XPATH, "//span[contains(text(),'Save & Next')]").click()

def main():
    driver = setup_driver()
    try:
        login(driver)
        navigate_to_achieve(driver)
        start_achieving(driver)
        select_sub_elements(driver)
        select_chapters(driver)
        test_taking(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
