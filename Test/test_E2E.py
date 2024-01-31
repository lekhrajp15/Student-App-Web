import pytest
from PageObject.goal_exam import GoalExamPage
from PageObject.learn_home_page import LearnHomePage
from PageObject.practice_home_page import PracticeHomePage
from PageObject.signUp_signIn import signIn_up
from PageObject.test_home_page import TestHomePage
from Utilities.utility import utility


class TestEmbibe(utility):

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_sign_in_password(self):
        login = signIn_up(self.driver)
        login.test_sign_in_password()
        log = self.getLogger()
        log.info("Testcase: Sign in with Password")


    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_signIn_mobile(self):
        log = self.getLogger()
        login = signIn_up(self.driver)
        login.sign_in_with_mobile()
        log.info("Testcase: Sign in with Mobile number")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_signIn_email(self):
        log = self.getLogger()
        login = signIn_up(self.driver)
        login.sign_in_with_email()
        log.info("Testcase: Sign in with Email ID")

    @pytest.mark.usefixtures("setup")
    def test_goal_exam_en(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.hero_banner_goal_exam_selection_eng()

    @pytest.mark.usefixtures("setup")
    def test_goal_exam_hi(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.hero_banner_goal_exam_selection_hin()

    @pytest.mark.usefixtures("setup")
    def test_update_profile(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.edit_profile()

    @pytest.mark.usefixtures("setup")
    def test_update_avatar(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.edit_avatar()

    @pytest.mark.usefixtures("setup")
    def test_profile_edit_goal_exam(self):
        log = self.getLogger()
        self.test_sign_in_password()
        gep = GoalExamPage(self.driver)
        gep.edit_goal_exam()

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_play_subject_hero_banner(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_hero_banner()
        log.info("Testcase: Playing Subject Hero Banner Videos")


    @pytest.mark.usefixtures("setup")
    def test_Banner_belongs_to_the_current_exam(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.Banner_belongs_to_the_current_exam()
        log.info("Testcase: Banner_belongs_to_the_current_exam")

    @pytest.mark.usefixtures("setup")
    def test_same_exam_subject_button_is_present_in_LPT_Modules(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.all_subject_tile_is_present_in_LPT()
        log.info("Testcase: Same Exam Subjects button is present in Learn,Practice, Test Module")

    @pytest.mark.usefixtures("setup")
    def test_click_each_module_Tab_is_navigating_to_its_module(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.click_each_module_Tab_is_navigation_to_module()
        log.info("Testcase: User is redirected to relevant screen on clicking on Learn/Practice/Test/Achieve/UserHome Tab")

    @pytest.mark.usefixtures("setup")
    def test_enrich_your_learning_carousel(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.enrich_your_learning_carousels()
        log.info("Testcase: Verify Enrich Your Learning carousel is present and no issues in video player")

    @pytest.mark.usefixtures("setup")
    def test_sub_embibe_explainers_carousel(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.sub_embibe_explainers_carousels()
        log.info("Testcase: Verify Embibe Explainers carousel is present in Subject filter and no issues in video player")

    @pytest.mark.usefixtures("setup")
    def test_sub_trendingg_videos_carousel(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.sub_trending_videos_carousels()
        log.info("Testcase: Verify Trending Videos carousel is present and no issues in video player")



    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_learn_continue_learning(self):
        log = self.getLogger()
        log.info("Test case: Playing Videos present in the Continue Learning Carousel")
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_continue_learning()

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_learn_trending_videos(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_trending_videos()
        log = self.getLogger()
        log.info("Test case: Playing  Videos present in the Trending Videos")
        log.info("Test case: Playing Videos present in the More Topic Carousel present inside Trending Videos details Page")
        log.info("Test case: Playing Videos present in the Related Videos Carousel present inside Trending Videos details Page")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_learn_embibe_explainers(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_embibe_explainers()
        log = self.getLogger()
        log.info("Test case: Playing Videos present in the Embibe Explainers Carousel")
        log.info("Test case: Playing Video present in the More Topics carousel present in Embibe Explainers details Page")
        log.info("Test case: Playing Video present in the Related Videos carousel present in Embibe Explainers details Page")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_learn_chapter(self):
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_learn_chapter()
        log = self.getLogger()
        log.info("Test case: Playing Video in the Continue Learning Carousel")
        log.info("Test case: Playing Video present in the All Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case: Playing Video present in the Topic Videos carousel present in Learn Chapter Summary Page")
        log.info("Test case: Displaying Points to Remember  in Learn Chapter Summary Page")
        log.info("Test case: Playing Video present in the Prerequisite  carousel present in Learn Chapter Summary Page")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_learn_subject_filter(self):
        log = self.getLogger()
        self.test_sign_in_password()
        learn = LearnHomePage(self.driver)
        learn.learn_subject_filter()
        log.info("Test case: Playing Videos present in the Subject Filter")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_practicechapters(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ph = PracticeHomePage(self.driver)
        log.info("Test case: Clicking on Practice Chapter in Practice Home")
        log.info("Test case: Practice Now Button is displayed in the Practice Summary")
        log.info("Test case: User is navigated to Practice Taking Screen on clicking on Practice Now button")
        ph.practice_chapters()
        log.info("Test case: User attempts 5 questions and view Learn Intervention screen")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_trending_test_embibe_exp_ui(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.trending_test_embibe_exp_ui()
        log.info("Test case: Click on Trending Test")
        log.info("Test case: Start Test Button is displayed in the Test Summary")
        log.info("Test case: User is navigated to Test Taking Screen on clicking on Start Test button")
        log.info("Test case: User submits the test after attempting all questions in the Test taking screen")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_full_test_embibe_exp_ui(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.full_test_embibe_exp_ui()
        log.info("Test case: Click on Full Test")
        log.info("Test case: Start Test Button is displayed in the Test Summary")
        log.info("Test case: User is navigated to Test Taking Screen on clicking on Start Test button")
        log.info("Test case: User submits the test after attempting all questions in the Test taking screen")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_chapter_test_embibe_exp_ui(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.chapter_test_embibe_exp_ui()
        log.info("Test case: Click on Chapter Test")
        log.info("Test case: Start Test Button is displayed in the Test Summary")
        log.info("Test case: User is navigated to Test Taking Screen on clicking on Start Test button")
        log.info("Test case: User submits the test after attempting all questions in the Test taking screen")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_test_home_subject_banner(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.test_home_sub_banner()
        log.info("Test case: Click on Subject Button present in the Test Page")
        log.info("Test case: Start Test Button is displayed in Test Banner")
        log.info("Test case: User is navigated to Test Taking Screen on clicking on Start Test button")
        log.info("Test case: User submits the test after attempting all questions in the Test taking screen")


    @pytest.mark.usefixtures("setup")
    def test_trending_test_summary(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.trending_test_summary()

    @pytest.mark.usefixtures("setup")
    def test_full_test_summary(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.full_test_summary()

    @pytest.mark.usefixtures("setup")
    def test_chapter_test_summary(self):
        log = self.getLogger()
        self.test_sign_in_password()
        ttp = TestHomePage(self.driver)
        ttp.chapter_test_summary()

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_practice_banner(self):
            log = self.getLogger()
            self.test_sign_in_password()
            ph = PracticeHomePage(self.driver)
            ph.practice_banner()
            log.info("Test case: Click on the Books present in the Practice Banner")
            log.info("Test case: Clicking on the Practice Tile present in the Book TOC")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_author_books(self):
            log = self.getLogger()
            self.test_sign_in_password()
            ph = PracticeHomePage(self.driver)
            ph.author_books()
            log.info("Test case: Click on the Author Books")
            log.info("Test case: Clicking on the Practice Tile present in the Book TOC")

    # @pytest.mark.skip
    @pytest.mark.usefixtures("setup")
    def test_embibe_big_books(self):
            log = self.getLogger()
            self.test_sign_in_password()
            ph = PracticeHomePage(self.driver)
            ph.embibe_big_books()
            log.info("Test case: Click on the Big Books")
            log.info("Test case: Clicking on the Practice Tile present in the Book TOC")

























