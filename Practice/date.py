import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
import requests


obj= Service('/browsers driver/msedgedriver')


# Create Edge options to disable notifications
edge_options = EdgeOptions()
edge_options.add_argument('--disable-notifications')
edge_options.add_argument('--disable-notifications')

# Initialize the Edge WebDriver with the options
driver = webdriver.Chrome(service=obj, options=edge_options)

# driver = webdriver.Edge(service=obj,options=edge_options)
driver.implicitly_wait(20)
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.tui.co.uk/")
driver.find_element(By.CSS_SELECTOR, "[id='cmCloseBanner']").click()
time.sleep(20)
current_date = datetime.now()

# Calculate tomorrow's date
tomorrow_date = current_date + timedelta(days=1)

# Format tomorrow's date as a string in a specific format, e.g., "YYYY-MM-DD"
formatted_date = tomorrow_date.strftime("%d")
print(formatted_date)
driver.find_element(By.NAME,"Departure Date").click()
time.sleep(10)
driver.find_element(By.XPATH,"//td[contains(text(),'"+formatted_date+"')]").click()
driver.find_element(By.CSS_SELECTOR,"[aria-label='Done Departure date']").click()
time.sleep(10)