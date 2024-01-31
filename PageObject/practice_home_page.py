import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By




class PracticeHomePage():

    def __init__(self, driver):
        self.driver = driver

    Practice_Module = (By.XPATH, "//*[text()='Practice']")
    Practice_banner_button = (By.XPATH, "//*[text()='Practice from Book']")
    Continue_Practice = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]")
    Author_Books = (By.XPATH, "//*[text()='Books With Videos & Solutions']/parent::div/div[2]/div/div/div[1]/div[1]/div/div[1]")
    Practice_Chapter = (By.XPATH, "//*[contains(text(),'Adaptive Practice Chapters From')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    Embibe_big_books = (By.XPATH, "//*[contains(text(), 'Embibe Big Books')]/parent::div/div[2]/div/div[1]/div[1]/div/div/div[1]")
    practice_now_btn = (By.XPATH, "//*[text()='Practice Now']")
    book_toc = (By.CSS_SELECTOR, "[class='toc-content']>div")
    book_chapter_practice = (By.XPATH, "//ol[@class='toc-content']/li[@class='rowPracticeList practiceTile']/img[@alt='practice']")

    # def test_practicemodule(self):
    #     self.driver.find_element(*practiceHome.Practice_Module).click()

    def practice_banner(self):
        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Practice_banner_button).click()
        book_toc = self.driver.find_element(*PracticeHomePage.book_toc)
        book_toc.is_displayed()
        self.driver.find_element(*PracticeHomePage.book_chapter_practice).click()
        self.practice_taking()

    def practice_chapters(self):

        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Practice_Chapter).click()
        practice_now_btn = self.driver.find_element(*PracticeHomePage.practice_now_btn)
        practice_now_btn.is_displayed()
        practice_now_btn.click()
        self.practice_taking()

    def author_books(self):

        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Author_Books).click()
        book_toc = self.driver.find_element(*PracticeHomePage.book_toc)
        book_toc.is_displayed()
        self.driver.find_element(*PracticeHomePage.book_chapter_practice).click()
        self.practice_taking()

    def embibe_big_books(self):

        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Embibe_big_books).click()
        book_toc = self.driver.find_element(*PracticeHomePage.book_toc)
        book_toc.is_displayed()
        self.driver.find_element(*PracticeHomePage.book_chapter_practice).click()
        self.practice_taking()


    def practice_taking(self):
        for i in range(1, 3):


            try:
                question_element = self.driver.find_element(By.XPATH,
                                                       "//div[@id='PracticeConatiner']/div/section/div/div[2]/span[2]")
                question = question_element.text

                if question_element.is_displayed():
                    if question == "Multiple Choice":
                        time.sleep(5)
                        self.driver.find_element(By.XPATH,
                                            "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                        self.driver.find_element(By.XPATH, "//div[@class='question-view-body']/div[2]/div[1]").click()
                        self.driver.find_element(By.XPATH, "//div[@class='question-view-body']/div[2]/div[2]").click()
                        self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                        time.sleep(10)
                        self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()


                    elif question == "Subjective":
                        self.driver.find_element(By.XPATH,
                                            "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, "//*[text()='Full Solution']").click()
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()


                    elif question == "Subjective Numerical":
                        self.driver.find_element(By.XPATH,
                                            "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, "//*[text()='Solve With Us']").click()
                        self.driver.find_element(By.XPATH, "//*[text()='Full Solution']").click()
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                    elif question == "Subjective Answer":
                        time.sleep(5)
                        self.driver.find_element(By.XPATH,
                                            "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                        self.driver.find_element(By.XPATH, "//*[text()='Solve With Us']").click()
                        self.driver.find_element(By.XPATH, "//*[text()='Full Solution']").click()
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()


                    elif question == "Fill in The Blanks":
                        time.sleep(5)
                        self.driver.find_element(By.XPATH,
                                            "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                        self.driver.find_element(By.CSS_SELECTOR, "[id='fb-blank-0']").click()
                        self.driver.find_element(By.CSS_SELECTOR, "[status='DEFAULT']").send_keys("XYZ")
                        self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

                    elif question == "Multiple Fill in The Blanks":
                        time.sleep(5)
                        self.driver.find_element(By.XPATH,
                                            "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                        self.driver.find_element(By.CSS_SELECTOR, "[id='fb-blank-0']").click()
                        self.driver.find_element(By.CSS_SELECTOR, "[status='DEFAULT']").send_keys("XYZ")
                        time.sleep(3)
                        self.driver.find_element(By.CSS_SELECTOR, "[id='fb-blank-1']").click()
                        time.sleep(2)
                        self.driver.find_element(By.CSS_SELECTOR, "[id='fb-blank-1']>input").send_keys("abc")
                        self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()



                    elif question in ["True-False", "Single Choice", "Assertion"]:
                        time.sleep(5)
                        self.driver.find_element(By.XPATH,
                                            "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                        self.driver.find_element(By.XPATH, "//div[@class='question-view-body']/div[2]/div[1]").click()
                        self.driver.find_element(By.XPATH, "//*[text()='Check']").click()
                        time.sleep(10)
                        self.driver.find_element(By.XPATH, "//*[text()='Continue']").click()

            except NoSuchElementException:
                self.driver.find_element(By.XPATH,
                                            "//div[@id='PracticeConatiner']/div/div[1]/div/div[1]").is_displayed()
                print("Learn Intervention screen is displayed")
                self.driver.find_element(By.XPATH, "//*[text()='Continue Practice']").click()


        self.driver.find_element(By.XPATH, "//*[@class='Title_title__og5qd']/div/div[2]/i").click()
        self.driver.find_element(By.XPATH, "//*[text()='End Session']").click()
        time.sleep(5)









