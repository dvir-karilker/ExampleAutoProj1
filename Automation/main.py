# " pipreqs . --force " to update requirements
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service  #Chrome instead? Change to  "..webdriver.chrome.service.." and download the Chrome Driver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time


# "Base" Class start
class Base:

    # driver Obj creation - 
    def __init__(self):
        service = Service(executable_path="geckodriver.exe")
        self.driver = webdriver.Firefox(service=service)

    # Navigation function -
    def navigation(self, url):
        self.driver.get(url)
    
    # Get Location/URL function -
    def get_location(self):
        return self.driver.current_url

    # A function to close the browser, "ending" the driver -
    def close_driver(self):
        self.driver.quit()


    # Methods:
    # A function to return the WebElement by a selected Attribute and its Value -
    def get_web_element(self, attr, value):

        # setting the required attribute (more flexible this way)
        by_what = getattr(By, attr.upper())

        # Using an Explicit Wait to hold for a certain time before "failing" our action
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by_what, value))

        )
        return element

    
    # A function to click an Element - 
    def click_on(self, element):
        WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(element)
            ).click()
        time.sleep(1)


    # A function to insert text to an Element - 
    def insert_text(self, element, text):
        if element.get_attribute("id") != "ff_8_pictures_1":  #<- CAN NOT "clear" file upload inputs
            element.clear()
            element.send_keys(text)
        else:
            element.send_keys(text)