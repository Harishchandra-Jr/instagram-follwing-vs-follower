# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import re
import os


driver = webdriver.Chrome(executable_path='L:\instagram-follwing-vs-follower/chromedriver.exe')

# soup = BeautifulSoup(page_html, 'html.parser')

base_url = 'https://www.instagram.com/itsharishchandra/?hl=en'

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get(base_url)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        
    def get_unfollowers(self):
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        button = self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup.find(class_="_7UhW9   xLCgt      MMzan   _0PwGv           fDxYl     "))
            
        # following = self._get_names()
        # self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
        #     .click()
        # followers = self._get_names()
        # not_following_back = [user for user in following if user not in followers]
        # print(not_following_back)

my_bot = InstaBot('itsharishchandra','chandraH') 
my_bot.get_unfollowers()