from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_correcto():
    driver = webdriver.Chrome()

    # Abrir la página de login local
    driver.get("file:///C:/Users/juanf/OneDrive/Escritorio/tarea4-P3/tarea4-programacion3/web/index.html")

    # Llenar email y contraseña (IDs reales del HTML)
    driver.find_element(By.ID, "txtEmail").send_keys("a@a.com")
    driver.find_element(By.ID, "txtPassword").send_keys("welosky123")

    # Click en el botón login
    driver.find_element(By.ID, "btnLogin").click()

    # Darle un tiempo a que redirija
    time.sleep(2)

    # Validar que llegó al CRUD (crud.html)
    assert "crud" in driver.current_url.lower()

    driver.quit()
