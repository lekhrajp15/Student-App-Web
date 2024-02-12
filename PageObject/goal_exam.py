import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import configparser


class GoalExamPage:


        def __init__(self,driver):
            self.driver= driver

        exam_button = (By.XPATH, "//div[@class='banner-wrapper clearfix ']/div[2]/div/div/button")
        goal_search_field = (By.XPATH, "//div[@class='edit-profile-wrapper']/div[2]/div[2]/input")
        goal_school= (By.XPATH, "//*[contains(text(),'School Exams')]")
        goal_cbse = (By.XPATH, "//*[contains(text(),'CBSE')]")
        exam_tab = (By.XPATH, "//*[contains(text(),'10th CBSE')]")
        eng_lang_btn =(By.XPATH, "//*[contains(@class,'selection-box')]/div[1]/span/div[1][contains(text(),'English')]")
        hindi_lang_btn = (By.XPATH, "//*[contains(text(),'Hindi')]")
        lang_done_btn = (By.XPATH, "//div[@id='app']/main/div/div[2]/div[2]/div[2]")
        manage_profile = (By.XPATH, "//*[contains(text(), 'Manage')]")
        profile_edit = (By.XPATH, "//div[@class='avatar-wrapper ']/div[2]")
        profile_name = (By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
        update_profile = (By.XPATH, "//div[@class='eds-col-12']/div[4]/button[1]")
        edit_goal = (By.XPATH, "//div[@class='eds-col-12']/div[4]/button[2]")
        avatar_edit_btn = (By.CSS_SELECTOR, "[alt='edit Icon']")
        avatar_done_btn = (By.XPATH, "//*[text()='Done']")
        avatar_click = (By.CSS_SELECTOR, "[class='avatar-wrapper ']>div:nth-of-type(1)")
        profile_icon = (By.XPATH, "//img[@alt='profile image']")

        def hero_banner_goal_exam_selection_eng(self):
            self.driver.find_element(*GoalExamPage.exam_button).click()
            self.driver.find_element(*GoalExamPage.goal_school).click()
            self.driver.find_element(*GoalExamPage.goal_cbse).click()
            self.driver.find_element(*GoalExamPage.exam_tab).click()
            self.driver.find_element(*GoalExamPage.eng_lang_btn).click()
            self.driver.find_element(*GoalExamPage.lang_done_btn).click()
            self.driver.find_element(By.XPATH, "//*[@to='/learn/home']").click()
            ele = self.driver.find_element(By.XPATH, "//*[@to='/test/home']").text
            # self.assertEqual(ele, 'test', f"Expected 'test', but got '{ele}'")
            if ele == 'Test':
                print("User langugae is English")
            else :
                print("User language is not changed")

        def hero_banner_goal_exam_selection_hin(self):
            self.driver.find_element(*GoalExamPage.exam_button).click()
            self.driver.find_element(*GoalExamPage.goal_school).click()
            self.driver.find_element(*GoalExamPage.goal_cbse).click()
            self.driver.find_element(*GoalExamPage.exam_tab).click()
            self.driver.find_element(*GoalExamPage.hindi_lang_btn).click()
            self.driver.find_element(*GoalExamPage.lang_done_btn).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@to='/learn/home']").click()
            ele = self.driver.find_element(By.XPATH, "//*[@to='/test/home']").text
            if ele == 'टेस्ट':
                print("User successfully changed his language to Hindi")
            else:
                print("User language not changed")
            cp = configparser.ConfigParser()
            cp.read('/Users/lekhraj/PycharmProjects/EmbibeFramework/Test/config.ini')
            exam_name = cp.get('Prod', 'exam_name')
            self.driver.find_element(*GoalExamPage.exam_button).click()
            time.sleep(1)
            self.driver.find_element(*GoalExamPage.goal_search_field).send_keys(exam_name)
            time.sleep(1)
            self.driver.find_element(By.XPATH, f"//*[contains(text(), '{exam_name}')]").click()
            time.sleep(1)
            self.driver.find_element(*GoalExamPage.eng_lang_btn).click()
            self.driver.find_element(*GoalExamPage.lang_done_btn).click()
            # self.driver.find_element(By.XPATH, "//*[@to='/learn/home']").click()
            ele = self.driver.find_element(By.XPATH, "//*[@to='/test/home']").text
            if ele == 'Test':
                print("User successfully changed his language to Hindi")
            else:
                print("User language not changed")


        def edit_profile(self):
            ele = self.driver.find_element(*GoalExamPage.profile_icon)
            act = ActionChains(self.driver)
            act.move_to_element(ele).perform()
            self.driver.find_element(*GoalExamPage.manage_profile).click()
            self.driver.find_element(*GoalExamPage.profile_edit).click()
            self.driver.find_element(*GoalExamPage.profile_name).send_keys("LRAJ")
            time.sleep(3)
            self.driver.find_element(*GoalExamPage.update_profile).click()

        def edit_avatar(self):
            ele = self.driver.find_element(*GoalExamPage.profile_icon)
            act = ActionChains(self.driver)
            act.move_to_element(ele).perform()
            self.driver.find_element(*GoalExamPage.manage_profile).click()
            time.sleep(2)
            self.driver.find_element(*GoalExamPage.profile_edit).click()
            time.sleep(2)
            self.driver.find_element(*GoalExamPage.avatar_edit_btn).click()
            self.driver.find_element(*GoalExamPage.avatar_done_btn).click()

        def edit_goal_exam(self):
            ele = self.driver.find_element(*GoalExamPage.profile_icon)
            act = ActionChains(self.driver)
            act.move_to_element(ele).perform()
            self.driver.find_element(*GoalExamPage.manage_profile).click()
            self.driver.find_element(*GoalExamPage.profile_edit).click()
            self.driver.find_element(*GoalExamPage.edit_goal).click()
            self.driver.find_element(*GoalExamPage.goal_school).click()
            self.driver.find_element(*GoalExamPage.goal_cbse).click()
            self.driver.find_element(*GoalExamPage.exam_tab).click()
            self.driver.find_element(*GoalExamPage.eng_lang_btn).click()
            self.driver.find_element(*GoalExamPage.lang_done_btn).click()
            self.driver.find_element(*GoalExamPage.avatar_click).click()
            self.driver.find_element(By.XPATH, "//*[@to='/learn/home']").click()
            ele = self.driver.find_element(By.XPATH, "//*[@to='/test/home']").text
            # self.assertEqual(ele, 'test', f"Expected 'test', but got '{ele}'")
            if ele == 'Test':
                print("User langugae is English")
            else:
                print("User language is not changed")






















