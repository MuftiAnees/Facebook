import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

PATH = "Documents\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()


driver.get("https://www.facebook.com/")
sleep(2)
search = driver.find_element(By.ID, "email")
search.send_keys("email")
search = driver.find_element(By.ID, "pass")
search.send_keys("password")
sleep(2)
search = driver.find_element(By.NAME, "login").click()
sleep(20)