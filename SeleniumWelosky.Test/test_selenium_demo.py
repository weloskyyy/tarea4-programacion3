from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def test_demo():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    time.sleep(3)
    driver.quit()
