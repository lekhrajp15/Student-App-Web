import time

import pytest
from PageObject.learn_home_page import LearnHomePage
from PageObject.practice_home_page import PracticeHomePage
from PageObject.signUp_signIn import signIn_up
from PageObject.test_home_page import TestHomePage
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
    def test_play_subject_hero_banner(self):
        log = self.getLogger()
        log.info("Playing Subject Hero Banner Videos")
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.test_learn_hero_banner()


    @pytest.mark.usefixtures("setup")
    def test_continue_learning(self):
        log = self.getLogger()
        log.info("Playing Videos present in the Continue Learning Carousel")
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.test_continue_learning()



    @pytest.mark.usefixtures("setup")
    def test_trending_videos(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.test_trending_videos()
        log = self.getLogger()
        log.info("Test case Executed : Playing  Videos present in the Trending Videos")
        log.info("Test case Executed : Playing Videos present in the More Topic Carousel present inside Trending Videos details Page")
        log.info("Test case : Playing Videos present in the Related Videos Carousel present inside Trending Videos details Page")


    @pytest.mark.usefixtures("setup")
    def test_embibe_explainers(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.test_embibe_explainers()
        log = self.getLogger()
        log.info("Test case Executed : Playing Videos present in the Embibe Explainers Carousel")
        log.info("Test case Executed : Playing Video present in the More Topics carousel present in Embibe Explainers details Page")
        log.info("Test case Executed : Playing Video present in the Related Videos carousel present in Embibe Explainers details Page")


    @pytest.mark.usefixtures("setup")
    def test_learn_chapter(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.test_learn_chapter()
        log = self.getLogger()
        log.info("Test case Executed : Playing Video in the Continue Learning Carousel")
        log.info("Test case Executed : Playing Video present in the All Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case Executed : Playing Video present in the Topic Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case Executed : Displaying Points to Remember  in Learn Chapter Summary Page")
        LearnHomePage.log.info("Test case Executed : Playing Video present in the Prerequisite  carousel present in Learn Chapter Summary Page")


    @pytest.mark.usefixtures("setup")
    def test_subject_filter(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.test_subject_filter()


    @pytest.mark.usefixtures("setup")
    def test_practice_banner(self):
        self.test_sign_in_password()
        ph = PracticeHomePage(self.driver)
        ph.test_practice_banner()

    @pytest.mark.usefixtures("setup")
    def test_author_books(self):
        self.test_sign_in_password()
        ph = PracticeHomePage(self.driver)
        ph.test_author_books()


    @pytest.mark.usefixtures("setup")
    def test_embibe_big_books(self):
        self.test_sign_in_password()
        ph = PracticeHomePage(self.driver)
        ph.test_embibe_big_books()


    @pytest.mark.usefixtures("setup")
    def test_practicechapters(self):
        self.test_sign_in_password()
        ph = PracticeHomePage(self.driver)
        ph.test_practice_chapters()

    @pytest.mark.usefixtures("setup")

    def test_trending_test_embibe_exp_ui(self):
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.trending_test_embibe_exp_ui()

    @pytest.mark.usefixtures("setup")

    def test_full_test_embibe_exp_ui(self):
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.full_test_embibe_exp_ui()


    @pytest.mark.usefixtures("setup")
    def test_chapter_test_embibe_exp_ui(self):
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.chapter_test_embibe_exp_ui()

    @pytest.mark.usefixtures("setup")
    def test_test_home_subject_banner(self):
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.test_home_sub_banner()
















