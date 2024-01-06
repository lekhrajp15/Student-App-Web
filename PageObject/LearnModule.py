import configparser
import time
from logging import getLogger

import openpyxl
import requests

from selenium.webdriver.common.by import By

class LearnModule():
    log = getLogger()
    def __init__(self, driver):
        self.driver=driver

    def test_apirequest(self):
        subname = self.driver.find_elements(By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[2]/div[2]/div[1]/div/div")
        size = len(subname)
        print(size)
        current_row = 2
        cp = configparser.ConfigParser()
        cp.read('/Users/lekhraj/PycharmProjects/EmbibeFramework/Test/config.ini')

        for i in range(1, size):
            subjectname = subname[i].text.lower()
            sub = requests.get("https://api-prod-cf.embibe.com/fiber_ms/v2/home/learn/" + subjectname.title() + "",
                               params={
                                   'exam_code': 'kve101426',
                                   'exam': '8th%20CBSE',
                                   'goal': 'CBSE',
                                   'goal_code': 'kve97670',
                                   'locale': 'en',
                               }, headers={
                    'embibe-token': cp['Prod']['embibe-token']})

            workbook = openpyxl.load_workbook(
                '/Users/lekhraj/PycharmProjects/EmbibeFramework/TestData/Automationreport.xlsx')
            video = None
            for j in range(2, 12):
                carousel = sub.json()[j]['section_name']
                sh = workbook['Learn_Subject Carousels']
                name = sh.cell(row=current_row, column=1, value=carousel)
                if name == "Trending Videos for Your Exam":
                    video = i
                    print("index value of trendingvideo is ", video)
                    current_row += 1
                workbook.save("/Users/lekhraj/PycharmProjects/EmbibeFramework/TestData/Automationreport.xlsx")
        trending_video = By.XPATH("//body/div[@id='app']/main[1]/div[2]/div[" + str(video) + "]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]")
        subject_buttons = (By.XPATH, "//*[@id='app']/main[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div")



      





