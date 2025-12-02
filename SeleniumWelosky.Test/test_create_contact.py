from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_crear_contacto():
    driver = webdriver.Chrome()

    # 1. Ir al login
    driver.get("file:///C:/Users/juanf/OneDrive/Escritorio/tarea4-P3/tarea4-programacion3/web/index.html")

    # 2. Login
    driver.find_element(By.ID, "txtEmail").send_keys("a@a.com")
    driver.find_element(By.ID, "txtPassword").send_keys("welosky123")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(2)

    # 3. Asegurarse de estar en crud.html (por si acaso)
    if "crud" not in driver.current_url.lower():
        driver.get("file:///C:/Users/juanf/OneDrive/Escritorio/tarea4-P3/tarea4-programacion3/web/crud.html")
        time.sleep(1)

    # 4. Llenar formulario de crear contacto
    nombre = "Contacto Prueba Selenium"
    telefono = "8090000000"
    correo = "selenium@prueba.com"

    driver.find_element(By.ID, "txtNombre").clear()
    driver.find_element(By.ID, "txtNombre").send_keys(nombre)

    driver.find_element(By.ID, "txtTelefono").clear()
    driver.find_element(By.ID, "txtTelefono").send_keys(telefono)

    driver.find_element(By.ID, "txtCorreo").clear()
    driver.find_element(By.ID, "txtCorreo").send_keys(correo)

    # 5. Click en Guardar
    driver.find_element(By.ID, "btnGuardar").click()
    time.sleep(2)

    # 6. Validar que el contacto aparece en la tabla
    tbody = driver.find_element(By.ID, "tblContactosBody")
    assert nombre in tbody.text

    driver.quit()
