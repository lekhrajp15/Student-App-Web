import time

import pytest
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from PageObject.LearnPage import Learnpage
from PageObject.PracticePage import practiceHome
from PageObject.SignUp import signIn_up
from Utilities.utility import utility


class TestEmbibe(utility):

    @pytest.mark.usefixtures("setup")
    def test_sign_in_password(self):
        login = signIn_up(self.driver)
        login.test_sign_in_password()


    @pytest.mark.usefixtures("setup")
    def test_signIn_mobile(self):
        login = signIn_up(self.driver)
        login.sign_in_with_mobile()


    @pytest.mark.usefixtures("setup")
    def test_signIn_email(self):
        login = signIn_up(self.driver)
        login.sign_in_with_email()


    @pytest.mark.usefixtures("setup")
    def test_playsubjectHeroBanner(self):
        log = self.getLogger()
        log.info("Playing Subject Hero Banner Videos")
        self.test_sign_in_password()
        learn = Learnpage(self.driver)
        learn.test_LearnHeroBanner()


    @pytest.mark.usefixtures("setup")
    def test_Continuelearning(self):
        log = self.getLogger()
        log.info("Playing Videos present in the Continue Learning Carousel")
        self.test_sign_in_password()
        learn = Learnpage(self.driver)
        learn.test_Continuelearning()


    @pytest.mark.usefixtures("setup")
    def test_TrendingVideos(self):
        self.test_sign_in_password()
        learn = Learnpage(self.driver)
        learn.test_TrendingVideos()
        log = self.getLogger()
        log.info("Test case Executed : Playing  Videos present in the Trending Videos")
        log.info("Test case Executed : Playing Videos present in the More Topic Carousel present inside Trending Videos details Page")
        log.info("Test case : Playing Videos present in the Related Videos Carousel present inside Trending Videos details Page")


    @pytest.mark.usefixtures("setup")
    def test_EmbibeExplainers(self):
        self.test_sign_in_password()
        learn = Learnpage(self.driver)
        learn.test_EmbibeExplainers()
        log = self.getLogger()
        log.info("Test case Executed : Playing Videos present in the Embibe Explainers Carousel")
        log.info("Test case Executed : Playing Video present in the More Topics carousel present in Embibe Explainers details Page")
        log.info("Test case Executed : Playing Video present in the Related Videos carousel present in Embibe Explainers details Page")


    @pytest.mark.usefixtures("setup")
    def test_LearnChapter(self):
        self.test_sign_in_password()
        learn = Learnpage(self.driver)
        learn.test_LearnChapter()
        log = self.getLogger()
        log.info("Test case Executed : Playing Video in the Continue Learning Carousel")
        log.info("Test case Executed : Playing Video present in the All Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case Executed : Playing Video present in the Topic Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case Executed : Displaying Points to Remember  in Learn Chapter Summary Page")
        Learnpage.log.info("Test case Executed : Playing Video present in the Prerequisite  carousel present in Learn Chapter Summary Page")

    @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_SubjectFilter(self):
        self.test_sign_in_password()
        learn = Learnpage(self.driver)
        learn.test_SubjectFilter()


    @pytest.mark.usefixtures("setup")
    def test_practicebanner(self):
        self.test_sign_in_password()
        ph = practiceHome(self.driver)
        ph.test_practicebanner()


    @pytest.mark.usefixtures("setup")
    def test_AuthorBooks(self):
        self.test_sign_in_password()
        ph = practiceHome(self.driver)
        ph.test_AuthorBooks()


    @pytest.mark.usefixtures("setup")
    def test_EmbibeBigBooks(self):
        self.test_sign_in_password()
        ph = practiceHome(self.driver)
        ph.test_Embibe_Big_Books()


    @pytest.mark.usefixtures("setup")
    def test_practicechapters(self):
        self.test_sign_in_password()
        ph = practiceHome(self.driver)
        ph.test_practicechapters()

















