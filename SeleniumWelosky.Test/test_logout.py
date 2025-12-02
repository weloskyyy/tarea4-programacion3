from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_logout():
    driver = webdriver.Chrome()

    # 1. Ir al login
    driver.get("file:///C:/Users/juanf/OneDrive/Escritorio/tarea4-P3/tarea4-programacion3/web/index.html")

    # 2. Limpiar sesión por si quedó algo de otra prueba
    driver.execute_script("window.sessionStorage.clear();")
    driver.delete_all_cookies()
    driver.refresh()
    time.sleep(1)

    # 3. Hacer login con credenciales válidas
    driver.find_element(By.ID, "txtEmail").send_keys("a@a.com")
    driver.find_element(By.ID, "txtPassword").send_keys("welosky123")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(2)

    # 4. Verificar que estamos en crud.html
    assert "crud.html" in driver.current_url.lower()

    # 5. Hacer logout
    driver.find_element(By.ID, "btnLogout").click()
    time.sleep(2)

    # 6. Validar que volvimos al login (index.html)
    assert "index.html" in driver.current_url.lower()

    # y que el formulario de login está visible
    login_form = driver.find_element(By.ID, "loginForm")
    assert login_form.is_displayed()

    driver.quit()
