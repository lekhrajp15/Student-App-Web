import time

from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By




class LearnHomePage():

    def __init__(self, driver):
        self.driver=driver

    Curated_Video = (By.XPATH, '//*[text() = "World''s Best Curated Learning Content"]/parent::div/div[2]/div/div/div[1]/div/div/div')
    learn_chapter = (By.XPATH, "//*[contains(text(), 'Chapters From')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    trending_videos = (By.XPATH, "//*[text()='Trending Videos for Your Exam']/parent::div/div[2]/div/div/div[1]/div/div/div")
    embibe_explainers= (By.XPATH,"//*[text()='Embibe Explainers']/parent::div/div[2]/div/div/div[1]/div/div/div")
    learn_module = (By.CSS_SELECTOR, "[to='/learn/home']")
    hero_button = (By.CSS_SELECTOR, "[data-tour='learn-button']")
    subject_buttons = (By.XPATH, "//*[@id='app']/main[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div")
    last_subject_button = (By.CSS_SELECTOR, "[id='subL']")
    video_play = (By.CSS_SELECTOR, "[data-tour='learn-button']")
    continue_learning = (By.XPATH, '//*[text() = "Continue Learning"]/parent::div/div[2]/div/div/div[1]/div/div/div')
    learn_button = (By.CSS_SELECTOR, "[class='action-bar-wrapper']>button")
    more_topic = (By.XPATH, "//*[text()='More on this Topic']")
    topic_video = (By.XPATH, "//*[@class = 'video-summary-wrapper__section-data-wrapper']/div/div[2]/div[1]/div/div[1]")
    related_video = (By.XPATH, "//*[text()='Related Videos']")
    related_video_click = (By.XPATH, "//*[@class = 'video-summary-wrapper__section-data-wrapper']/div/div[2]/div[1]/div/div[1]")
    # all_videos = (By.XPATH, "//*[@class='learn-summary-wrapper__section-data-wrapper']/div/div[2]/div[2]/div[1]/div[1]")
    topic_in_this_chapter = (By.XPATH, "//*[text()='Topics in this Chapter']")
    video_click = (By.XPATH, "//*[@class='learn-summary-wrapper__section-data-wrapper']/div/div[2]/div[2]/div[1]/div[1]")
    hero_banner_sub = (By.XPATH, "//*[contains(@class,'banner--info-content')]/div/div[2]/div/div[1]/span[1]/span[1]")
    practice_module = (By.XPATH, "//*[text()='Practice']")
    test_module = (By.XPATH, "//*[text()='Test']")
    ptr = (By.XPATH, "//*[text()='Points to Remember']")
    prerequisite = (By.XPATH, "//*[text()='Prerequisite Topics to ace this Topic']")
    practice_banner_button = (By.XPATH, "//*[text()='Practice from Book']")
    custom_test = (By.XPATH, "//div[contains(text(),'My Custom Tests')]")
    achieve_module = (By.CSS_SELECTOR, "[to='/achieve/landing']")
    start_achieving = (By.XPATH, "//span[contains(text(),'Start Achieving Now')]")
    user_home = (By.XPATH, "//span[contains(text(),'Home')]")
    parent_assignment= (By.XPATH, "//div[contains(text(),'Assignment from My Parents')]")
    enrich_your_learning_carousel = (By.XPATH, "//*[contains(text(),'Enrich')]")
    enrich_tile = (By.XPATH, "//*[contains(text(),'Enrich')]/parent::div/div[2]/div[2]/div[1]/div[1]/div/div/div")

    sub_embibe_explainers = (By.XPATH, "//*[contains(text(), 'Embibe Explainers For')]")
    sub_embibe_explainers_tile = (By.XPATH, "//*[contains(text(), 'Embibe Explainers For')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    sub_trendingvideos = (By.XPATH, "//*[contains(text(), 'Trending Videos for Your Exam')]")
    sub_trendingvideos_tile   = (By.XPATH, "//*[contains(text(), 'Trending Videos for Your Exam')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    sub_topic_video = (By.XPATH, "//body[1]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]")
    sub_related_video = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]")
    sub_all_video = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[6]")
    sub_prerequisite_video = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]")



    def learn_hero_banner(self):

        self.driver.find_element(*LearnHomePage.learn_module).click()
        self.driver.find_element(*LearnHomePage.hero_button).is_displayed()
        total_subject= self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(0,count-2):
            self.driver.find_element(By.CSS_SELECTOR,"[id='sub"+str(i)+"']").click()
            subname = self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").text
            hero_banner_subject = self.driver.find_element(*LearnHomePage.hero_banner_sub).text

            self.driver.refresh()
            self.driver.find_element(*LearnHomePage.hero_button).click()
            time.sleep(20)
            self.driver.find_element(*LearnHomePage.hero_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*LearnHomePage.hero_button).send_keys(keys.Keys.ESCAPE)

            assert subname == hero_banner_subject, "Assertion failed: subname is not equal to hero_banner_subject"

    def Banner_belongs_to_the_current_exam(self):

            self.driver.find_element(*LearnHomePage.learn_module).click()
            self.driver.find_element(*LearnHomePage.hero_button).is_displayed()
            total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
            count = len(total_subject)
            for i in range(0, count - 2):
                self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").click()
                self.driver.refresh()
                subname = self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").text
                hero_banner_subject = self.driver.find_element(*LearnHomePage.hero_banner_sub).text
                print(subname, hero_banner_subject)
                assert subname.casefold() == hero_banner_subject.casefold(), "Assertion failed: subname is not equal to hero_banner_subject"


            self.driver.find_element(*LearnHomePage.last_subject_button).click()
            subname = self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").text
            hero_banner_subject = self.driver.find_element(*LearnHomePage.hero_banner_sub).text
            print(subname, hero_banner_subject)
            assert subname.casefold() == hero_banner_subject.casefold(), "Assertion failed: subname is not equal to hero_banner_subject"

    def click_each_module_Tab_is_navigation_to_module(self):
        self.driver.find_element(*LearnHomePage.learn_module).click()
        self.driver.find_element(*LearnHomePage.hero_button).is_displayed()
        self.driver.find_element(*LearnHomePage.test_module).click()
        self.driver.find_element(*LearnHomePage.custom_test).click()
        self.driver.find_element(*LearnHomePage.practice_module).click()
        self.driver.find_element(*LearnHomePage.practice_banner_button).is_displayed()
        self.driver.find_element(*LearnHomePage.achieve_module).click()
        self.driver.find_element(*LearnHomePage.start_achieving).is_displayed()
        self.driver.find_element(*LearnHomePage.user_home).click()
        self.driver.find_element(*LearnHomePage.parent_assignment).is_displayed()

    def learn_trending_videos(self):
        self.driver.find_element(*LearnHomePage.trending_videos).click()
        time.sleep(5)
        self.play_video_button()
        try:
            self.driver.find_element(*LearnHomePage.more_topic).click()
            self.driver.find_element(*LearnHomePage.topic_video).click()
            self.play_video_button()
            self.driver.back()
        except NoSuchElementException:
            print("More Topics Link is not present")

        try:
            self.driver.find_element(*LearnHomePage.related_video).click()
            self.driver.find_element(*LearnHomePage.related_video_click).click()
            self.play_video_button()
            self.driver.back()

        except NoSuchElementException:
            print("Related Videos Link is not present")

    def learn_embibe_explainers(self):
        self.driver.find_element(*LearnHomePage.embibe_explainers).click()
        self.play_video_button()
        # self.driver.find_element(*LearnHomePage.more_topic).click()
        # self.driver.find_element(*LearnHomePage.topic_video).click()
        # self.play_video_button()
        # self.driver.back()
        # self.driver.find_element(*LearnHomePage.related_video).click()
        # self.driver.find_element(*LearnHomePage.related_video_click).click()
        # self.play_video_button()
        # self.driver.back()
        try:
            self.driver.find_element(*LearnHomePage.more_topic).click()
            self.driver.find_element(*LearnHomePage.topic_video).click()
            self.play_video_button()
            self.driver.back()
        except NoSuchElementException:
            print("More Topics Link is not present")

        try:
            self.driver.find_element(*LearnHomePage.related_video).click()
            self.driver.find_element(*LearnHomePage.related_video_click).click()
            self.play_video_button()
            self.driver.back()

        except NoSuchElementException:
            print("Related Videos Link is not present")

    def learn_continue_learning(self):
        self.driver.find_element(*LearnHomePage.continue_learning).click()
        self.play_video_button()
        self.driver.back()

    def learn_learn_chapter(self):
        self.driver.find_element(*LearnHomePage.learn_chapter).click()
        time.sleep(5)

        self.play_video_button()
        try:
            self.driver.find_element(*LearnHomePage.topic_in_this_chapter).click()
            time.sleep(2)
            self.driver.find_element(*LearnHomePage.video_click).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
        except:
            print("No Topic in this Chapter link present")

        self.driver.find_element(*LearnHomePage.ptr).click()
        try:
            self.driver.find_element(*LearnHomePage.prerequisite).click()
            self.driver.find_element(*LearnHomePage.video_click).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
        except:
            print("No Prerequisite Videos present")

    def learn_subject_filter(self):
        self.driver.find_element(*LearnHomePage.learn_module).click()
        total_subject= self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(0,count-2):
            self.driver.find_element(By.CSS_SELECTOR,"[id='sub"+str(i)+"']").click()
            self.driver.refresh()
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.sub_trendingvideos).click()
            time.sleep(5)
            self.play_video_button()
            try:
                self.driver.find_element(*LearnHomePage.more_topic).click()
                time.sleep(5)
                self.driver.find_element(*LearnHomePage.topic_video).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
            except:
                print("No More Topic Link is present")

            try:
                self.driver.find_element(*LearnHomePage.related_video).click()
                time.sleep(3)
                self.driver.find_element(*LearnHomePage.related_video_click).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
                self.driver.back()
            except:
                print("No Related Videos Link is present")


            self.driver.find_element(*LearnHomePage.sub_embibeexplainers).click()
            time.sleep(5)
            self.play_video_button()
            try:
                self.driver.find_element(*LearnHomePage.more_topic).click()
                time.sleep(3)
                self.driver.find_element(*LearnHomePage.topic_video).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
            except:
                print("No Topic Videos Link is present")

            try:
                self.driver.find_element(*LearnHomePage.related_video).click()
                time.sleep(3)
                self.driver.find_element(*LearnHomePage.related_video_click).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
                self.driver.back()
            except:
                print("No Related Videos Link is present")


            self.driver.find_element(*LearnHomePage.learn_chapter).click()
            time.sleep(5)
            self.play_video_button()

            # self.driver.find_element(*Learnpage.sub_all_video).click()
            # time.sleep(5)
            # self.playvideobutton()
            try:
                self.driver.find_element(*LearnHomePage.topic_in_this_chapter).click()
                time.sleep(5)
                self.driver.find_element(*LearnHomePage.video_click).click()
                self.play_video_button()
                self.driver.back()
            except:
                print("Topics in this Chapter link is not present")


            self.driver.find_element(*LearnHomePage.ptr).click()

            try:
                self.driver.find_element(*LearnHomePage.prerequisite).click()
                self.driver.find_element(*LearnHomePage.video_click).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
                self.driver.back()
                self.driver.back()
            except:
                print("No PreRequisite videos present")

        self.driver.find_element(*LearnHomePage.last_subject_button).click()
        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element(*LearnHomePage.sub_trendingvideos).click()
        time.sleep(5)
        self.play_video_button()
        try:
            self.driver.find_element(*LearnHomePage.more_topic).click()
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.topic_video).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
        except:
            print("No More Topic Videos Present")

        try:
            self.driver.find_element(*LearnHomePage.related_video).click()
            time.sleep(3)
            self.driver.find_element(*LearnHomePage.related_video_click).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
            self.driver.back()
        except:
            print("No Related Videos Present")


        self.driver.find_element(*LearnHomePage.sub_embibeexplainers).click()
        time.sleep(5)
        self.play_video_button()
        try:
            self.driver.find_element(*LearnHomePage.more_topic).click()
            time.sleep(3)
            self.driver.find_element(*LearnHomePage.topic_video).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
        except:
            print("No Topic Videos Present")

        try:
            self.driver.find_element(*LearnHomePage.related_video).click()
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.related_video_click).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
            self.driver.back()
        except:
            print("No related Videos Present")


        self.driver.find_element(*LearnHomePage.learn_chapter).click()
        time.sleep(5)
        self.play_video_button()

        # self.driver.find_element(*Learnpage.sub_all_video).click()
        # time.sleep(5)
        # self.playvideobutton()
        try:
            self.driver.find_element(*LearnHomePage.topic_in_this_chapter).click()  # need to check
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.video_click).click()
            self.play_video_button()
            self.driver.back()
        except:
            print("Topic in this Chapter is not present")

        self.driver.find_element(*LearnHomePage.ptr).click()
        try:
            self.driver.find_element(*LearnHomePage.prerequisite).click()
            self.driver.find_element(*LearnHomePage.video_click).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
            self.driver.back()
        except:
            print("No Prerequisite Videos Present")

    def all_subject_tile_is_present_in_LPT(self):
        self.driver.find_element(*LearnHomePage.learn_module).click()
        learn_total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        learn_sub_count = len(learn_total_subject)
        print(learn_sub_count)

        self.driver.find_element(*LearnHomePage.test_module).click()
        test_total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        test_sub_count = len(test_total_subject)
        print(test_sub_count)

        self.driver.find_element(*LearnHomePage.practice_module).click()
        practice_total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        practice_sub_count = len(practice_total_subject)
        print(practice_sub_count)

        assert learn_sub_count == test_sub_count == practice_sub_count, "Assertion failed: Not all elements have the same value"

    def enrich_your_learning_carousels(self):
        try:
            self.driver.find_element(*LearnHomePage.enrich_your_learning_carousel).is_displayed()
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.enrich_tile).click()
            self.play_video_button()

            try:
                self.driver.find_element(*LearnHomePage.more_topic).click()
                time.sleep(3)
                self.driver.find_element(*LearnHomePage.topic_video).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
            except NoSuchElementException:
                print("No Topic Videos Present")
                self.driver.back()

            try:
                self.driver.find_element(*LearnHomePage.related_video).click()
                time.sleep(5)
                self.driver.find_element(*LearnHomePage.related_video_click).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
                self.driver.back()
            except NoSuchElementException:
                print("No related Videos Present")
                self.driver.back()

        except NoSuchElementException:
            print("Enrich Your Carousel is not present")

    def sub_embibe_explainers_carousels(self):
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(0, count - 2):
            self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").click()
            try:
                self.driver.find_element(*LearnHomePage.sub_embibe_explainers).is_displayed()
                time.sleep(5)
                # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
                self.driver.find_element(*LearnHomePage.sub_embibe_explainers_tile).click()
                self.play_video_button()
                try:
                    self.driver.find_element(*LearnHomePage.more_topic).click()
                    time.sleep(3)
                    self.driver.find_element(*LearnHomePage.topic_video).click()
                    time.sleep(5)
                    self.play_video_button()
                    self.driver.back()
                except NoSuchElementException:
                    print("No Topic Videos Present")
                    self.driver.back()

                try:
                    self.driver.find_element(*LearnHomePage.related_video).click()
                    time.sleep(5)
                    self.driver.find_element(*LearnHomePage.related_video_click).click()
                    time.sleep(5)
                    self.play_video_button()
                    self.driver.back()
                    self.driver.back()
                except NoSuchElementException:
                    print("No related Videos Present")
                    self.driver.back()

            except NoSuchElementException:
                    print("Embibe Explainers Carousel is not present")
        self.driver.find_element(*LearnHomePage.last_subject_button).click()
        try:
            self.driver.find_element(*LearnHomePage.sub_embibe_explainers).is_displayed()
            time.sleep(5)
            # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
            self.driver.find_element(*LearnHomePage.sub_embibe_explainers_tile).click()
            self.play_video_button()
            try:
                self.driver.find_element(*LearnHomePage.more_topic).click()
                time.sleep(3)
                self.driver.find_element(*LearnHomePage.topic_video).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
            except NoSuchElementException:
                print("No Topic Videos Present")
                self.driver.back()

            try:
                self.driver.find_element(*LearnHomePage.related_video).click()
                time.sleep(5)
                self.driver.find_element(*LearnHomePage.related_video_click).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
                self.driver.back()
            except NoSuchElementException:
                print("No related Videos Present")
                self.driver.back()

        except NoSuchElementException:
            print("Trending Carousel is not present")

    def sub_trending_videos_carousels(self):
        total_subject = self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(0, count - 2):
            self.driver.find_element(By.CSS_SELECTOR, "[id='sub" + str(i) + "']").click()
            try:
                self.driver.find_element(*LearnHomePage.sub_trendingvideos).is_displayed()
                time.sleep(5)
                # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
                self.driver.find_element(*LearnHomePage.sub_trendingvideos_tile).click()
                self.play_video_button()
                try:
                    self.driver.find_element(*LearnHomePage.more_topic).click()
                    time.sleep(3)
                    self.driver.find_element(*LearnHomePage.topic_video).click()
                    time.sleep(5)
                    self.play_video_button()
                    self.driver.back()
                except NoSuchElementException:
                    print("No Topic Videos Present")
                    self.driver.back()

                try:
                    self.driver.find_element(*LearnHomePage.related_video).click()
                    time.sleep(5)
                    self.driver.find_element(*LearnHomePage.related_video_click).click()
                    time.sleep(5)
                    self.play_video_button()
                    self.driver.back()
                    self.driver.back()
                except NoSuchElementException:
                    print("No related Videos Present")
                    self.driver.back()

            except NoSuchElementException:
                    print("Trending Carousel is not present")
        self.driver.find_element(*LearnHomePage.last_subject_button).click()
        try:
            self.driver.find_element(*LearnHomePage.sub_trendingvideos).is_displayed()
            time.sleep(5)
            # self.driver.find_element(*LearnHomePage.sub_embibe_explainers).click()
            self.driver.find_element(*LearnHomePage.sub_trendingvideos_tile).click()
            self.play_video_button()
            try:
                self.driver.find_element(*LearnHomePage.more_topic).click()
                time.sleep(3)
                self.driver.find_element(*LearnHomePage.topic_video).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
            except NoSuchElementException:
                print("No Topic Videos Present")
                self.driver.back()

            try:
                self.driver.find_element(*LearnHomePage.related_video).click()
                time.sleep(5)
                self.driver.find_element(*LearnHomePage.related_video_click).click()
                time.sleep(5)
                self.play_video_button()
                self.driver.back()
                self.driver.back()
            except NoSuchElementException:
                print("No related Videos Present")
                self.driver.back()

        except NoSuchElementException:
            print("Trending Carousel is not present")

    def play_video_button(self):

        self.driver.find_element(*LearnHomePage.learn_button).click()
        try:
            popup = self.driver.find_element(By.CSS_SELECTOR, "[class='sc-llJcti cLATmR sc-jfmDQi LQhpp']")
            if popup.is_displayed():
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "[class='sc-gicCDI kMRQrC']>button:nth-of-type(1)").click()
                time.sleep(10)
                self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
                time.sleep(5)
        except NoSuchElementException:
            time.sleep(10)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            time.sleep(5)

        except ElementClickInterceptedException:
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*LearnHomePage.learn_button).send_keys(keys.Keys.ESCAPE)





























