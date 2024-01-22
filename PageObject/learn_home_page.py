import time
from logging import getLogger

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from Utilities.utility import utility



class LearnHomePage(utility):
    log = getLogger()
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

    ptr = (By.XPATH, "//*[text()='Points to Remember']")
    prerequisite = (By.XPATH, "//*[text()='Prerequisite Topics to ace this Topic']")

    sub_embibeexplainers = (By.XPATH, "//*[contains(text(), 'Embibe Explainers For')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    sub_trendingvideos = (By.XPATH, "//*[contains(text(), 'Trending Videos for Your Exam')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    sub_topic_video = (By.XPATH, "//body[1]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]")
    sub_related_video = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]")
    sub_all_video = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[6]")
    sub_prerequisite_video = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]")



    def test_learn_hero_banner(self):
        LearnHomePage.log.info("Test case : Playing Hero Banners for the current Exam")
        self.driver.find_element(*LearnHomePage.learn_module).click()
        self.driver.find_element(*LearnHomePage.hero_button).is_displayed()
        total_subject= self.driver.find_elements(*LearnHomePage.subject_buttons)
        count = len(total_subject)
        for i in range(0,count-2):
            self.driver.find_element(By.CSS_SELECTOR,"[id='sub"+str(i)+"']").click()
            self.driver.refresh()
            self.driver.find_element(*LearnHomePage.hero_button).click()
            time.sleep(20)
            self.driver.find_element(*LearnHomePage.hero_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*LearnHomePage.hero_button).send_keys(keys.Keys.ESCAPE)


        self.driver.find_element(*LearnHomePage.last_subject_button).click()
        self.driver.find_element(*LearnHomePage.hero_button).click()
        time.sleep(20)
        self.driver.find_element(*LearnHomePage.hero_button).send_keys(keys.Keys.ESCAPE)
        self.driver.find_element(*LearnHomePage.hero_button).send_keys(keys.Keys.ESCAPE)

    def test_trending_videos(self):
        LearnHomePage.log.info("Test case : Playing Video in the Trending Videos Carousel")
        self.driver.find_element(*LearnHomePage.trending_videos).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.find_element(*LearnHomePage.more_topic).click()
        self.driver.find_element(*LearnHomePage.topic_video).click()
        self.play_video_button()
        self.driver.back()
        self.driver.find_element(*LearnHomePage.related_video).click()
        self.driver.find_element(*LearnHomePage.related_video_click).click()
        self.play_video_button()
        self.driver.back()

    def test_embibe_explainers(self):
        LearnHomePage.log.info("Test case : Playing Video in the Embibe Explainer Carousel")
        self.driver.find_element(*LearnHomePage.embibe_explainers).click()
        self.play_video_button()
        self.driver.find_element(*LearnHomePage.more_topic).click()
        self.driver.find_element(*LearnHomePage.topic_video).click()
        self.play_video_button()
        self.driver.back()
        self.driver.find_element(*LearnHomePage.related_video).click()
        self.driver.find_element(*LearnHomePage.related_video_click).click()
        self.play_video_button()
        self.driver.back()

    def test_continue_learning(self):
        LearnHomePage.log.info("Test case : Playing Video from Continue Learning Carousel")
        self.driver.find_element(*LearnHomePage.continue_learning).click()
        self.play_video_button()
        self.driver.back()

    def test_learn_chapter(self):
        LearnHomePage.log.info("Test case : Playing Video in the Learn Chapter Carousel")
        self.driver.find_element(*LearnHomePage.learn_chapter).click()
        time.sleep(5)
        self.play_video_button()

        self.driver.find_element(*LearnHomePage.topic_in_this_chapter).click()
        time.sleep(2)
        self.driver.find_element(*LearnHomePage.video_click).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.back()

        self.driver.find_element(*LearnHomePage.ptr).click()

        self.driver.find_element(*LearnHomePage.prerequisite).click()
        self.driver.find_element(*LearnHomePage.video_click).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.back()

    def test_subject_filter(self):
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
            self.driver.find_element(*LearnHomePage.more_topic).click()
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.topic_video).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
            self.driver.find_element(*LearnHomePage.related_video).click()
            time.sleep(3)
            self.driver.find_element(*LearnHomePage.related_video_click).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
            self.driver.back()


            self.driver.find_element(*LearnHomePage.sub_embibeexplainers).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.find_element(*LearnHomePage.more_topic).click()
            time.sleep(3)
            self.driver.find_element(*LearnHomePage.topic_video).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
            self.driver.find_element(*LearnHomePage.related_video).click()
            time.sleep(3)
            self.driver.find_element(*LearnHomePage.related_video_click).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
            self.driver.back()


            self.driver.find_element(*LearnHomePage.learn_chapter).click()
            time.sleep(5)
            self.play_video_button()

            # self.driver.find_element(*Learnpage.sub_all_video).click()
            # time.sleep(5)
            # self.playvideobutton()

            self.driver.find_element(*LearnHomePage.topic_in_this_chapter).click() #need to check
            time.sleep(5)
            self.driver.find_element(*LearnHomePage.video_click).click()
            self.play_video_button()
            self.driver.back()


            self.driver.find_element(*LearnHomePage.ptr).click()
            self.driver.find_element(*LearnHomePage.prerequisite).click()
            self.driver.find_element(*LearnHomePage.video_click).click()
            time.sleep(5)
            self.play_video_button()
            self.driver.back()
            self.driver.back()
            self.driver.back()

        self.driver.find_element(*LearnHomePage.last_subject_button).click()
        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element(*LearnHomePage.sub_trendingvideos).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.find_element(*LearnHomePage.more_topic).click()
        time.sleep(5)
        self.driver.find_element(*LearnHomePage.topic_video).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.back()
        self.driver.find_element(*LearnHomePage.related_video).click()
        time.sleep(3)
        self.driver.find_element(*LearnHomePage.related_video_click).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.back()
        self.driver.back()


        self.driver.find_element(*LearnHomePage.sub_embibeexplainers).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.find_element(*LearnHomePage.more_topic).click()
        time.sleep(3)
        self.driver.find_element(*LearnHomePage.topic_video).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.back()
        self.driver.find_element(*LearnHomePage.related_video).click()
        time.sleep(5)
        self.driver.find_element(*LearnHomePage.related_video_click).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.back()
        self.driver.back()


        self.driver.find_element(*LearnHomePage.learn_chapter).click()
        time.sleep(5)
        self.play_video_button()

        # self.driver.find_element(*Learnpage.sub_all_video).click()
        # time.sleep(5)
        # self.playvideobutton()

        self.driver.find_element(*LearnHomePage.topic_in_this_chapter).click()  # need to check
        time.sleep(5)
        self.driver.find_element(*LearnHomePage.video_click).click()
        self.play_video_button()
        self.driver.back()

        self.driver.find_element(*LearnHomePage.ptr).click()
        self.driver.find_element(*LearnHomePage.prerequisite).click()
        self.driver.find_element(*LearnHomePage.video_click).click()
        time.sleep(5)
        self.play_video_button()
        self.driver.back()
        self.driver.back()


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






















