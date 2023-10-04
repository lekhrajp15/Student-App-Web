import configparser

import openpyxl
import requests

cp = configparser.ConfigParser()
cp.read('/Users/lekhraj/PycharmProjects/EmbibeFramework/Test/config.ini')
learn_home = requests.get(url=cp['Prod']['LH'], params={
        'exam_code': cp['Prod']['exam_code'],
        'exam': cp['Prod']['exam'],
        'goal': cp['Prod']['goal'],
        'goal_code': cp['Prod']['goal_code'],
        'locale': cp['Prod']['locale']
        ,
    }, headers={
        'embibe-token': cp['Prod']['embibe-token']})
workbook = openpyxl.load_workbook('/Users/lekhraj/PycharmProjects/EmbibeFramework/TestData/Automationreport.xlsx')
section_name = len(learn_home.json())
for i in range(1, section_name - 1):
    name = learn_home.json()[i]['section_name']
    sh0 = workbook['Carousel Names in Home Page']
    sh0.cell(row=i + 1, column=1, value=name)
    if name == "Trending Videos for Your Exam":
        trendingvideo = i
        print("index value of trendingvideo is ", trendingvideo )
    workbook.save("/Users/lekhraj/PycharmProjects/EmbibeFramework/TestData/Automationreport.xlsx")

