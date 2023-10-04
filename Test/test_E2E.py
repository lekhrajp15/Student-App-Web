
import pytest
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from PageObject.LearnPage import Learnpage
from PageObject.PracticePage import practiceHome
from Utilities.utility import utility


class TestEmbibe(utility):
    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_signin(self):
        # self.driver.find_element(By.ID, "wzrk-cancel").click()
        log = self.getLogger()
        log.info("Test case : Sign In with Password ")
        self.driver.find_element(By.XPATH, "//*[contains(text(),'Log in')]").click()
        self.driver.find_element(By.NAME, "email").send_keys("9035371071")
        self.driver.find_element(By.XPATH,"//*[contains(text(),'password')]").click()
        self.driver.find_element(By.NAME, "password").send_keys("embibe1234")
        self.driver.find_element(By.NAME, "password").send_keys(keys.Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR,"[to='/learn/home']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[data-tour='learn-button']").is_displayed()

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_playsubjectHeroBanner(self):
        log = self.getLogger()
        log.info("Playing Subject Hero Banner Videos")
        self.test_signin()
        learn = Learnpage(self.driver)
        learn.test_Learnpage()

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_Continuelearning(self):
        log = self.getLogger()
        log.info("Playing Videos present in the Continue Learning Carousel")
        self.test_signin()
        learn = Learnpage(self.driver)
        learn.test_Continuelearning()

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_TrendingVideos(self):
        self.test_signin()
        learn = Learnpage(self.driver)
        learn.test_TrendingVideos()
        log = self.getLogger()
        log.info("Test case Executed : Playing  Videos present in the Trending Videos")
        log.info("Test case Executed : Playing Videos present in the More Topic Carousel present inside Trending Videos details Page")
        log.info("Test case : Playing Videos present in the Related Videos Carousel present inside Trending Videos details Page")

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_EmbibeExplainers(self):
        self.test_signin()
        learn = Learnpage(self.driver)
        learn.test_EmbibeExplainers()
        log = self.getLogger()
        log.info("Test case Executed : Playing Videos present in the Embibe Explainers Carousel")
        log.info("Test case Executed : Playing Video present in the More Topics carousel present in Embibe Explainers details Page")
        log.info("Test case Executed : Playing Video present in the Related Videos carousel present in Embibe Explainers details Page")

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_LearnChapter(self):
        self.test_signin()
        learn = Learnpage(self.driver)
        learn.test_LearnChapter()
        log = self.getLogger()
        log.info("Test case Executed : Playing Video in the Continue Learning Carousel")
        log.info("Test case Executed : Playing Video present in the All Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case Executed : Playing Video present in the Topic Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case Executed : Displaying Points to Remember  in Learn Chapter Summary Page")
        Learnpage.log.info("Test case Executed : Playing Video present in the Prerequisite  carousel present in Learn Chapter Summary Page")


    @pytest.mark.usefixtures("setup")
    def test_SubjectFilter(self):
        self.test_signin()
        learn = Learnpage(self.driver)
        learn.test_SubjectFilter()

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_practicebanner(self):
        self.test_signin()
        ph = practiceHome(self.driver)
        ph.test_practicebanner()

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_trendingbooks(self):
        self.test_signin()
        ph = practiceHome(self.driver)
        ph.test_trendingbooks()

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_AuthorBooks(self):
        self.test_signin()
        ph = practiceHome(self.driver)
        ph.test_AuthorBooks()

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_practicechapters(self):
        self.test_signin()
        ph = practiceHome(self.driver)
        ph.test_practicechapters()















