from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_editar_contacto():
    driver = webdriver.Chrome()

    # 1. Login
    driver.get("file:///C:/Users/juanf/OneDrive/Escritorio/tarea4-P3/tarea4-programacion3/web/index.html")
    driver.find_element(By.ID, "txtEmail").send_keys("a@a.com")
    driver.find_element(By.ID, "txtPassword").send_keys("welosky123")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(2)

    # 2. Ir al CRUD si no está ya
    if "crud" not in driver.current_url.lower():
        driver.get("file:///C:/Users/juanf/OneDrive/Escritorio/tarea4-P3/tarea4-programacion3/web/crud.html")
        time.sleep(1)

    # 3. Asegurarnos de que exista un contacto base
    nombre_original = "Contacto Prueba Selenium"
    if nombre_original not in driver.page_source:
        # Si no existe, lo creamos rápido
        driver.find_element(By.ID, "txtNombre").send_keys(nombre_original)
        driver.find_element(By.ID, "txtTelefono").send_keys("8090000000")
        driver.find_element(By.ID, "txtCorreo").send_keys("selenium@prueba.com")
        driver.find_element(By.ID, "btnGuardar").click()
        time.sleep(2)

    # 4. Click en Editar del contacto
    driver.find_element(
        By.XPATH,
        f"//table[@id='tblContactos']//tr[td[contains(normalize-space(),'{nombre_original}')]]//button[contains(text(),'Editar')]"
    ).click()

    time.sleep(1)

    # 5. Editar el nombre y guardar
    nuevo_nombre = "Contacto Editado Selenium"

    nombre_input = driver.find_element(By.ID, "txtNombre")
    nombre_input.clear()
    nombre_input.send_keys(nuevo_nombre)

    driver.find_element(By.ID, "btnGuardar").click()
    time.sleep(2)

    # 6. Validar que el nuevo nombre aparece
    tbody = driver.find_element(By.ID, "tblContactosBody")
    assert nuevo_nombre in tbody.text

    driver.quit()
