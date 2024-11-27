import time


from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.practice_home_page import PracticeHomePage
from PageObject.test_home_page import TestHomePage


class UserHome(PracticeHomePage, TestHomePage):

    def __init__(self, driver):
        self.driver = driver

    user_home = (By.XPATH, "//span[text()='Home']")
    bookmark_video_tile = (
    By.XPATH, "//div[text()='My Bookmarks']/parent::div/div[2]/div/div[1]/div[1]/div/div/div/div[2]")
    bookmark_question_tile = (By.XPATH, "//div[text()='My Bookmarks']/parent::div/div[2]/div/div[1]/div[2]/div/div")
    play_all_btn = (By.XPATH, "//span[text()='Play All']")
    practice_all_btn = (By.XPATH, "//span[text()='Practice All']")
    video_bookmark = (By.XPATH, "//*[@class='summary-banner-wrapper__icon-title']/span")
    practice_bookmark_button = (By.XPATH, "//i[@class='demo-icon demo-icon--filled demo-icon--xs icon-style']")
    video_carousel = (
    By.XPATH, "//div[text()='Trending Videos for Your Exam']/parent::div/div[2]/div[2]/div/div[4]/div")
    add_fav_book = (By.XPATH,
                    "//*[@src='https://sss.embibe.com/cdn-cgi/image/q=75,w=25,fit=scale-down,onerror=redirect/https://assets.embibe.com/production/web-assets/assets/images/Home/en/manage_books.png']")
    add_book = (By.XPATH, "//div[@class='favBooks-wrapper']/div[2]/div/div[2]/div/div[3]/div")
    done_button = (By.XPATH, "//*[text()='Done']")
    test_tile = (By.XPATH, '//*[@id="app"]/main/div[2]/div/div[6]/div[2]/div[2]/div/div[1]/div/div/div/div[4]')
    view_test_fb = (By.XPATH, "//*[text()='View Test Feedback']")
    revision_list = (By.ID, "revision-lists")
    rl_important_ques = (By.XPATH, "//*[text()='IMPORTANT QUESTIONS']")
    rl_important_ques_chap_1 = (By.XPATH, "//*[text()='IMPORTANT QUESTIONS']/parent::div/parent::div/parent::div/parent::div/div[2]/div[1]")
    rl_practice_btn = (By.CSS_SELECTOR, "[class='accordian-button-wrapper']")
    rl_filter_dd = (By.XPATH, "//*[text()='Questions To Revise']")
    rl_topics_to_revise = (By.XPATH, "//*[text()='Topics To Revise']")
    rl_solved_examples = (By.XPATH, "//*[text()='SOLVED EXAMPLES']")
    rl_solved_examples_chap_1 = (By.XPATH, "//*[text()='SOLVED EXAMPLES']/parent::div/parent::div/parent::div/parent::div/div[2]/div[1]")
    rl_topics_to_revise_learn_button= (By.XPATH, "//*[text()='SOLVED EXAMPLES']/parent::div/parent::div/parent::div/parent::div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div/button")
    rl_sub_dd = (By.XPATH, "//*[text()='All Subjects']")
    rl_sub_options = (By.XPATH, "//*[@class='eds-dropdown-menu__wrapper revision-list-filter-menu-wrapper']/li[2]/button/div/span")
    UH_live_class_btn = (By.XPATH, "//div[@class='section subject-section']/div[2]/div/div/div[2]/div/div/div/span[text()='Live Classes']")
    past_live_class_watch_now_btn = (By.XPATH, "//*[text()='Past Live Classes']/parent::div/div[2]/div[2]/div/div[@data-index='0']/div/div/div/div[5]/button")
    live_class_watch_recording_btn = (By.XPATH, "//*[text()='Watch Recording']")
    live_class_chat_button = (By.XPATH, "//*[text()='Chat']")
    live_class_performance_button = (By.XPATH, "//*[text()='Performance']")

    def watch_past_live_class(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.user_home)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.UH_live_class_btn)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.past_live_class_watch_now_btn)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.live_class_watch_recording_btn)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.live_class_performance_button)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(UserHome.live_class_chat_button)
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.live_class_performance_button)
        ).click()

        assert self.driver.find_element(By.CSS_SELECTOR, "[class='text']").text == "You have not attended this class!"

    def practice_in_revision_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.user_home)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.revision_list)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.rl_important_ques)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.rl_important_ques_chap_1)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.rl_practice_btn)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "loader"))  # Adjust this condition as needed.
        )

    def learn_in_revision_lis(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UserHome.user_home)
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UserHome.revision_list)
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UserHome.rl_filter_dd)
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UserHome.rl_topics_to_revise)
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UserHome.rl_solved_examples)
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UserHome.rl_solved_examples_chap_1)
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UserHome.rl_topics_to_revise_learn_button)
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element((By.CLASS_NAME, "loader"))  # Adjust if a loader or spinner is expected.
            )

            self.recommendlearningvideos()

    def add_favourite_book(self):
        # Click on the user home button
        self.driver.find_element(*UserHome.user_home).click()

        # Wait for the element containing 'My Favourite Books' to be visible
        fav_books_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'My Favourite Books')]"))
        )

        # Scroll into view to make sure it's visible
        self.driver.execute_script("arguments[0].scrollIntoView();", fav_books_element)

        # Wait for the 'Add Favourite Book' button to be clickable and click it
        add_fav_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@src='https://sss.embibe.com/cdn-cgi/image/q=75,w=25,fit=scale-down,onerror=redirect/https://assets.embibe.com/production/web-assets/assets/images/Home/en/manage_books.png']"))
        )
        add_fav_button.click()

        # # Wait for the 'Add Book' button to be clickable and click it
        # add_book_button = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Add Book')]"))
        # )
        # add_book_button.click()
        #
        # # Click on the Done button
        # done_button = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Done')]"))
        # )
        # done_button.click()

    def video_bookmark_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.video_carousel)
        ).click()

        # Click on the summary banner title
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='summary-banner-wrapper__icon-title']/span"))
        ).click()

        # Get description text
        desc = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='eds-row eds-row-start eds-row-top']/div/p"))
        ).text
        print(desc)

        # Navigate back to the user home
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.user_home)
        ).click()

        # Scroll to the bottom of the page
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        )

        # Click on the bookmark video tile
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UserHome.bookmark_video_tile)
        ).click()

        # Get expected description text
        exp_desc = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='section-division']/div[1]/div/div[2]/div/div[1]/div"))
        ).text
        print(exp_desc)

        # Compare descriptions
        if desc == exp_desc:
            print("Bookmark video matching")
        else:
            print("Bookmark video not matching")

    def play_bookmark_video(self):
        self.driver.find_element(*UserHome.user_home).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element(*UserHome.bookmark_video_tile).click()
        self.driver.find_element(*UserHome.play_all_btn).click()
        time.sleep(10)
        self.driver.back()

    def practice_bookmark_question(self):
        # Click on the user home button
        self.driver.find_element(*UserHome.user_home).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.driver.find_element(*UserHome.bookmark_question_tile).click()
        self.driver.find_element(*UserHome.practice_all_btn).click()
        time.sleep(5)
        self.driver.back()

    def test_i_have_taken(self):
        self.driver.find_element(*UserHome.user_home).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.driver.find_element(*UserHome.test_tile).click()
        time.sleep(2)
        self.driver.find_element(*UserHome.view_test_fb).click()
        time.sleep(5)
        score = self.driver.find_element(By.CSS_SELECTOR,
                                         "[class='tf-score-card__item-value-score']>div:nth-of-type(1)")
        print(score.text)
        score.click()
        time.sleep(3)
        obtained_score = self.driver.find_element(By.CSS_SELECTOR, "[class='tf-score-value']>div:nth-of-type(1)").text
        print(obtained_score)
        self.driver.find_element(By.CSS_SELECTOR, "[alt='arrow']").click()
        time.sleep(3)
        # negative behavior
        try:
            self.driver.find_element(By.XPATH,
                                     "//div[@class='test-feedback-container ']/div[2]/div[2]/div/div[2]").is_displayed()
            self.driver.find_element(By.XPATH,
                                     "//div[@class='test-feedback-container ']/div[2]/div[2]/div/div[2]").click()
            self.driver.find_element(By.XPATH,
                                     "//div[@class='tf-section-detail-page']/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/picture").click()
            time.sleep(5)
            self.driver.back()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, "[alt='arrow']").click()

        except NoSuchElementException:
            print("No Negative Behavior")
        time.sleep(3)

        # Positive behavior

        # Time Management
        self.driver.find_element(By.XPATH, "//*[text()='Time Management']").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "[alt='arrow']").click()

        time.sleep(3)
        # Chapterwise Analysis
        self.driver.find_element(By.XPATH,
                                 "//*[contains(text(), 'Chapterwise Analysis') or contains(text(), 'Topicwise Analysis')]").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "[alt='arrow']").click()

        time.sleep(3)
        # Overall Strong/Weak Chapters Analysis
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Overall Strong')]").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "[alt='arrow']").click()

        time.sleep(3)
        # Questionwise Analysis
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Questionwise Analysis')]").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "[alt='arrow']").click()



