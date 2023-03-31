import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

PATH = "Documents\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()


driver.get("http://172.16.10.4:8082/jw/web/login")
sleep(2)
search = driver.find_element(By.ID, "j_username")
search.send_keys("admin")
search = driver.find_element(By.ID, "j_password")
search.send_keys("CareKamra@2022")
search = driver.find_element(By.NAME, "submit").click()
print("Login Successful!")
sleep(2)