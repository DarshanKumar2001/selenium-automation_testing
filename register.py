import time
import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service("C:/Users/DARSHAN/Desktop/Placement-webapp-using-Django-master/chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://127.0.0.1:8000/register/")
print(driver.title)
driver.find_element(By.NAME,'username').send_keys(data.name)
time.sleep(10)
driver.find_element(By.NAME,'email').send_keys(data.email)
time.sleep(10)
driver.find_element(By.NAME,'password1').send_keys(data.password)
time.sleep(10)
driver.find_element(By.NAME,'password2').send_keys(data.password)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > button > strong").click()
print("Test Successfull")
driver.quit()