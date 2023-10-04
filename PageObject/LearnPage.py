import time
from logging import getLogger

from selenium.common import NoSuchElementException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from Utilities.utility import utility



class Learnpage(utility):
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
    topic_video = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")
    related_video = (By.XPATH, "//*[text()='Related Videos']")
    all_videos = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]")
    chapter_topic = (By.XPATH, "//*[text()='Topics in this Chapter']")
    chapter_video = (By.XPATH,"//body/div[@id='app']/main[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]")
    ptr = (By.XPATH, "//*[text()='Points to Remember']")
    prerequisite = (By.XPATH, "//*[text()='Prerequisite Topics to ace this Topic']")
    prerequisitetopic = (By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]")

    sub_embibeexplainers = (By.XPATH, "//*[contains(text(), 'Embibe Explainers For')]/parent::div/div[2]/div/div/div[1]/div/div/div")
    sub_trendingvideos = (By.XPATH, "//*[contains(text(), 'Trending Videos for Your Exam')]/parent::div/div[2]/div/div/div[1]/div/div/div")


    def test_Learnpage(self):
        self.driver.find_element(*Learnpage.learn_module).click()
        self.driver.find_element(*Learnpage.hero_button).is_displayed()
        total_subject= self.driver.find_elements(*Learnpage.subject_buttons)
        count = len(total_subject)
        for i in range(0,count-2):
            self.driver.find_element(By.CSS_SELECTOR,"[id='sub"+str(i)+"']").click()
            self.driver.refresh()
            self.driver.find_element(*Learnpage.hero_button).click()
            time.sleep(20)
            self.driver.find_element(*Learnpage.hero_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*Learnpage.hero_button).send_keys(keys.Keys.ESCAPE)


        self.driver.find_element(*Learnpage.last_subject_button).click()
        self.driver.find_element(*Learnpage.hero_button).click()
        time.sleep(20)
        self.driver.find_element(*Learnpage.hero_button).send_keys(keys.Keys.ESCAPE)
        self.driver.find_element(*Learnpage.hero_button).send_keys(keys.Keys.ESCAPE)

    def test_TrendingVideos(self):
        print(Learnpage.trending_videos)
        self.driver.find_element(*Learnpage.trending_videos).click()
        time.sleep(5)
        self.playvideobutton()
        self.driver.find_element(*Learnpage.more_topic).click()
        self.driver.find_element(*Learnpage.topic_video).click()
        self.playvideobutton()
        self.driver.back()
        self.driver.find_element(*Learnpage.related_video).click()
        self.driver.find_element(*Learnpage.topic_video).click()
        self.playvideobutton()
        self.driver.back()

    def test_EmbibeExplainers(self):
        Learnpage.log.info("Test case : Playing Video in the Embibe Explainer Carousel")
        self.driver.find_element(*Learnpage.embibe_explainers).click()
        self.playvideobutton()
        self.driver.find_element(*Learnpage.more_topic).click()
        self.driver.find_element(*Learnpage.topic_video).click()
        self.playvideobutton()
        self.driver.back()
        self.driver.find_element(*Learnpage.related_video).click()
        self.driver.find_element(*Learnpage.topic_video).click()
        self.playvideobutton()
        self.driver.back()

    def test_Continuelearning(self):
        self.driver.find_element(*Learnpage.continue_learning).click()
        self.playvideobutton()
        self.driver.back()

    def test_LearnChapter(self):
        self.driver.find_element(*Learnpage.learn_chapter).click()
        time.sleep(5)
        self.playvideobutton()

        self.driver.find_element(*Learnpage.all_videos).click()
        time.sleep(8)
        self.driver.find_element(*Learnpage.learn_button).send_keys(keys.Keys.ESCAPE)
        self.driver.find_element(*Learnpage.learn_button).send_keys(keys.Keys.ESCAPE)

        self.driver.find_element(*Learnpage.chapter_topic).click()
        self.driver.find_element(*Learnpage.chapter_video).click()
        time.sleep(5)
        self.playvideobutton()
        self.driver.back()
        self.driver.find_element(*Learnpage.ptr).click()
        self.driver.find_element(*Learnpage.prerequisite).click()
        self.driver.find_element(*Learnpage.prerequisitetopic).click()
        time.sleep(5)
        self.playvideobutton()
        self.driver.back()

    def test_SubjectFilter(self):
        self.driver.find_element(*Learnpage.learn_module).click()
        total_subject= self.driver.find_elements(*Learnpage.subject_buttons)
        count = len(total_subject)
        for i in range(0,count-2):
            self.driver.find_element(By.CSS_SELECTOR,"[id='sub"+str(i)+"']").click()
            self.driver.refresh()
            self.driver.find_element(*Learnpage.sub_trendingvideos).click()
            time.sleep(5)
            self.playvideobutton()
            time.sleep(5)
            self.driver.find_element(*Learnpage.more_topic).click()
            self.driver.find_element(*Learnpage.topic_video).click()
            time.sleep(5)
            self.playvideobutton()
            self.driver.back()
            self.driver.find_element(*Learnpage.related_video).click()
            self.driver.find_element(*Learnpage.topic_video).click()
            time.sleep(5)
            self.playvideobutton()
            self.driver.back()
            self.driver.back()


            self.driver.find_element(*Learnpage.sub_embibeexplainers).click()
            time.sleep(5)
            self.playvideobutton()
            time.sleep(5)
            self.driver.find_element(*Learnpage.more_topic).click()
            self.driver.find_element(*Learnpage.topic_video).click()
            time.sleep(5)
            self.playvideobutton()
            self.driver.back()
            self.driver.find_element(*Learnpage.related_video).click()
            self.driver.find_element(*Learnpage.topic_video).click()
            time.sleep(5)
            self.playvideobutton()
            self.driver.back()
            self.driver.back()


            self.driver.find_element(*Learnpage.learn_chapter).click()
            time.sleep(5)
            self.playvideobutton()

            self.driver.find_element(*Learnpage.all_videos).click()
            time.sleep(8)
            self.driver.find_element(*Learnpage.learn_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*Learnpage.learn_button).send_keys(keys.Keys.ESCAPE)

            self.driver.find_element(*Learnpage.chapter_topic).click()
            time.sleep(5)
            self.driver.find_element(*Learnpage.chapter_video).click()
            self.playvideobutton()
            self.driver.back()


            self.driver.find_element(*Learnpage.ptr).click()
            self.driver.find_element(*Learnpage.prerequisite).click()
            self.driver.find_element(*Learnpage.prerequisitetopic).click()
            time.sleep(5)
            self.playvideobutton()
            self.driver.back()
            self.driver.back()



    def playvideobutton(self):
        self.driver.find_element(*Learnpage.learn_button).click()

        try:
            popup = self.driver.find_element(By.CSS_SELECTOR, "[class='sc-llJcti cLATmR sc-jfmDQi LQhpp']")
            if popup.is_displayed():
                time.sleep(5)
                self.driver.find_element(By.CSS_SELECTOR, "[class='sc-gicCDI kMRQrC']>button:nth-of-type(1)").click()
                time.sleep(10)
                self.driver.find_element(*Learnpage.learn_button).send_keys(keys.Keys.ESCAPE)
                self.driver.find_element(*Learnpage.learn_button).send_keys(keys.Keys.ESCAPE)
                time.sleep(5)
        except NoSuchElementException:
            time.sleep(10)
            self.driver.find_element(*Learnpage.learn_button).send_keys(keys.Keys.ESCAPE)
            self.driver.find_element(*Learnpage.learn_button).send_keys(keys.Keys.ESCAPE)
            time.sleep(5)






















