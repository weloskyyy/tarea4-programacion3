from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_logout():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000/Login")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(1)

    driver.find_element(By.ID, "btnLogout").click()
    time.sleep(1)

    assert "Login" in driver.title

    driver.quit()
