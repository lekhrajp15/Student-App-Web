from logging import getLogger

from selenium.webdriver.common.by import By

from Utilities.utility import utility


class practiceHome(utility):
    log = getLogger()
    def __init__(self, driver):
        self.driver = driver

    Practice_Module = (By.XPATH, "//*[text()='Practice']")
    Practice_banner_button = (By.XPATH, "//*[text()='Practice from Book']")
    Continue_Practice = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]")
    Trending_Books = (By.CSS_SELECTOR, "[class='section other-sections other-sections-4']>div:nth-of-type(2)>div>div>div[data-index='0']>div>div>div")
    Practice_Chapter = (By.CSS_SELECTOR, "[class='section other-sections other-sections-5']>div:nth-of-type(2)>div>div>div[data-index='0']>div>div>div")
    Author_Books = (By.CSS_SELECTOR, "[class='section other-sections other-sections-6']>div:nth-of-type(2)>div>div>div[data-index='0']>div>div>div")


    # def test_practicemodule(self):
    #     self.driver.find_element(*practiceHome.Practice_Module).click()

    def test_practicebanner(self):
        practiceHome.log.info("Test case : Clicking on Practice Banner in Practice Home")
        self.driver.find_element(*practiceHome.Practice_Module).click()
        self.driver.find_element(*practiceHome.Practice_banner_button).click()


    def test_trendingbooks(self):
        practiceHome.log.info("Test case : Clicking on Trending Books in Practice Home")
        self.driver.find_element(*practiceHome.Practice_Module).click()
        self.driver.find_element(*practiceHome.Trending_Books).click()

    def test_practicechapters(self):
        practiceHome.log.info("Test case : Clicking on Practice Chapter in Practice Home")
        self.driver.find_element(*practiceHome.Practice_Module).click()
        self.driver.find_element(*practiceHome.Practice_Chapter).click()

    def test_AuthorBooks(self):
        practiceHome.log.info("Test case : Clicking on Author Book in Practice Home")
        self.driver.find_element(*practiceHome.Practice_Module).click()
        self.driver.find_element(*practiceHome.Author_Books).click()