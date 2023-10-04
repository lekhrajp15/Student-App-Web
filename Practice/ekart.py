import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions

class saucedemo():
    def add2cart(self):
        obj = Service('/browsers driver/msedgedriver')
        edge_options = EdgeOptions()
        edge_options.add_argument('--disable-notifications')
        driver = webdriver.Chrome(service=obj, options=edge_options)
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(5)
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("QA")
        driver.find_element(By.ID, "last-name").send_keys("QA")
        driver.find_element(By.ID, "postal-code").send_keys("560001")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
        time.sleep(5)
        text = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert text == "Thank you for your order!"
obj = saucedemo()
obj.add2cart()
