from logging import getLogger

from selenium.webdriver.common.by import By

from Utilities.utility import utility


class PracticeHomePage(utility):
    log = getLogger()
    def __init__(self, driver):
        self.driver = driver

    Practice_Module = (By.XPATH, "//*[text()='Practice']")
    Practice_banner_button = (By.XPATH, "//*[text()='Practice from Book']")
    Continue_Practice = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]")
    Author_Books = (By.XPATH, "//*[text()='Books With Videos & Solutions']/parent::div/div[2]/div/div/div[1]/div[1]/div/div[1]")
    Practice_Chapter = (By.XPATH, "//*[contains(text(),'Adaptive Practice Chapters From')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    embibe_big_books = (By.XPATH, "//*[contains(text(), 'Embibe Big Books')]/parent::div/div[2]/div/div[1]/div[1]/div/div/div[1]")
    practice_now_btn = (By.XPATH, "//*[text()='Practice Now']")
    book_toc = (By.CSS_SELECTOR, "[class='toc-content']>div")

    # def test_practicemodule(self):
    #     self.driver.find_element(*practiceHome.Practice_Module).click()

    def test_practice_banner(self):
        PracticeHomePage.log.info("Test case : Clicking on Practice Banner in Practice Home")
        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Practice_banner_button).click()
        book_toc = self.driver.find_element(*PracticeHomePage.book_toc)
        book_toc.is_displayed()

    def test_practice_chapters(self):
        PracticeHomePage.log.info("Test case : Clicking on Practice Chapter in Practice Home")
        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Practice_Chapter).click()
        practice_now_btn = self.driver.find_element(*PracticeHomePage.practice_now_btn)
        practice_now_btn.is_displayed()

    def test_author_books(self):
        PracticeHomePage.log.info("Test case : Clicking on Author Book in Practice Home")
        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.Author_Books).click()
        book_toc = self.driver.find_element(*PracticeHomePage.book_toc)
        book_toc.is_displayed()

    def test_embibe_big_books(self):
        PracticeHomePage.log.info("Test case : Clicking on Author Book in Practice Home")
        self.driver.find_element(*PracticeHomePage.Practice_Module).click()
        self.driver.find_element(*PracticeHomePage.embibe_big_books).click()
        book_toc = self.driver.find_element(*PracticeHomePage.book_toc)
        book_toc.is_displayed()
