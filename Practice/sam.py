import random
import time

import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument('--disable-notifications')
obj= Service("/browsers driver/chromedriver")
driver = webdriver.Chrome(service=obj, options=chrome_options)
driver.implicitly_wait(20)
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.embibe.com/")
driver.find_element(By.XPATH, "//*[contains(text(),'Log in')]").click()
driver.find_element(By.NAME, "email").send_keys("9035371071")
driver.find_element(By.XPATH,"//*[contains(text(),'password')]").click()
driver.find_element(By.NAME, "password").send_keys("embibe1234")
driver.find_element(By.NAME, "password").send_keys(keys.Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, "[to='/learn/home']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//body/div[@id='app']/main[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/img[1]").click()



# Find the stable parent element that contains the carousel items
parent_element = driver.find_elements(By.XPATH, "//*[@class='carousel-header']")
carousel_item_texts = []

for item in parent_element:
    # Get the text of each carousel item and append it to the list
    carousel_item_texts.append(item.text)

# Print the list of carousel item texts
print(carousel_item_texts)



# Trending_Videos_index = [i for i, item in enumerate(carousel_item_texts) if "Trending"in item]
# if Trending_Videos_index:
#      print(Trending_Videos_index)
#
# else:
#     print("not found")
#
# learn_index = [i for i, item in enumerate(carousel_item_texts) if "Learn"in item]
# if learn_index:
#      print(learn_index)
#
# else:
#     print("not found")
#
# Big_Books_index = [i for i, item in enumerate(carousel_item_texts) if "Learn"in item]
# if Big_Books_index:
#      print(Big_Books_index)
#
# else:
#     print("not found")
#
# Books_With_Videos_Solutions_index = [i for i, item in enumerate(carousel_item_texts) if "Learn"in item]
# if Books_With_Videos_Solutions_index:
#      print(Books_With_Videos_Solutions_index)
#
# else:
#     print("not found")
#
# Embibe_Explainers_index = [i for i, item in enumerate(carousel_item_texts) if "Learn"in item]
# if Embibe_Explainers_index:
#      print(Books_With_Videos_Solutions_index)
#
# else:
#     print("not found")
#
# Embibe_Explainers_index = [i for i, item in enumerate(carousel_item_texts) if "Learn"in item]
# if Embibe_Explainers_index:
#      print(Books_With_Videos_Solutions_index)
#
# else:
#     print("not found")










