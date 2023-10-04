import inspect
import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import logging


class utility:

    def playvideobutton(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-tour='learn-button']").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "[data-tour='learn-button']").send_keys(keys.Keys.ESCAPE)
        self.driver.find_element(By.CSS_SELECTOR, "[data-tour='learn-button']").send_keys(keys.Keys.ESCAPE)
        time.sleep(5)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

