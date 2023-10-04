import configparser
import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.edge.options import Options as EdgeOptions
import requests
from selenium.webdriver.common.by import By

edge_options = EdgeOptions()
edge_options.add_argument('--disable-notifications')
obj= Service('/Users/lekhraj/PycharmProjects/EmbibeFramework/browsers driver/msedgedriver')
driver = webdriver.Edge(service=obj, options=edge_options)
driver.implicitly_wait(20)
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.embibe.com")
driver.find_element(By.XPATH, "//*[contains(text(),'Log in')]").click()
driver.find_element(By.NAME, "email").send_keys("lekhraj.p@embibe.com")
driver.find_element(By.XPATH,"//*[contains(text(),'password')]").click()
driver.find_element(By.NAME, "password").send_keys("embibe1234")
driver.find_element(By.NAME, "password").send_keys(keys.Keys.ENTER)
driver.find_element(By.CSS_SELECTOR,"[to='/learn/home']").click()
subname= driver.find_elements(By.XPATH,  "//body/div[@id='app']/main[1]/div[2]/div[2]/div[2]/div[1]/div/div")
size = len(subname)
print(size)
current_row = 2
cp=configparser.ConfigParser()
cp.read('/Users/lekhraj/PycharmProjects/EmbibeFramework/Test/config.ini')

for i in range(1, size):
    subjectname=subname[i].text.lower()
    sub = requests.get("https://api-prod-cf.embibe.com/fiber_ms/v2/home/learn/"+subjectname.title()+"", params={
                'exam_code': 'kve101426',
                'exam': '8th%20CBSE',
                 'goal': 'CBSE',
                 'goal_code': 'kve97670',
                 'locale': 'en',
             }, headers = {
        'embibe-token': cp['Prod']['embibe-token']})
    workbook = openpyxl.load_workbook('/Users/lekhraj/PycharmProjects/EmbibeFramework/TestData/Automationreport.xlsx')
    for j in range(2,12):
        carousel =sub.json()[j]['section_name']
        sh=workbook['Learn_Subject Carousels']
        name = sh.cell(row=current_row, column=1, value=carousel)
        if name == "Trending Videos for Your Exam":
            trendingvideo = i
            print("index value of trendingvideo is ", trendingvideo)

        current_row += 1

        trending_video = By.XPATH("//body/div[@id='app']/main[1]/div[2]/div["+str(trendingvideo)+"]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]")





    workbook.save("/Users/lekhraj/PycharmProjects/EmbibeFramework/TestData/Automationreport.xlsx")







