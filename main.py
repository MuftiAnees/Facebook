import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from colorama import Fore, Back, Style
from CommonScripts.login import *
from selenium.common.exceptions import NoSuchElementException

driver.maximize_window()


PATH = "D:\Coding\Python\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def login():
    driver.get("http://172.16.10.4:8082/jw/web/login")
    sleep(2)
    search = driver.find_element(By.ID, "j_username")
    search.send_keys("admin")
    search = driver.find_element(By.ID, "j_password")
    search.send_keys("CareKamra@2022")
    search = driver.find_element(By.NAME, "submit").click()
    print("Login Successful!")
    sleep(2)