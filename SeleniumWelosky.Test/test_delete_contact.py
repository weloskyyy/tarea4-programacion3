from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_eliminar_contacto():
    driver = webdriver.Chrome()

    # 1. Login
    driver.get("file:///C:/Users/juanf/OneDrive/Escritorio/tarea4-P3/tarea4-programacion3/web/index.html")
    driver.find_element(By.ID, "txtEmail").send_keys("a@a.com")
    driver.find_element(By.ID, "txtPassword").send_keys("welosky123")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(2)

    # 2. Ir al CRUD
    if "crud" not in driver.current_url.lower():
        driver.get("file:///C:/Users/juanf/OneDrive/Escritorio/tarea4-P3/tarea4-programacion3/web/crud.html")
        time.sleep(1)

    # 3. Asegurarnos de que existe un contacto a eliminar
    nombre_a_eliminar = "Contacto Editado Selenium"
    if nombre_a_eliminar not in driver.page_source:
        # Si no existe, lo creamos para poder eliminarlo
        driver.find_element(By.ID, "txtNombre").send_keys(nombre_a_eliminar)
        driver.find_element(By.ID, "txtTelefono").send_keys("8090000000")
        driver.find_element(By.ID, "txtCorreo").send_keys("selenium@prueba.com")
        driver.find_element(By.ID, "btnGuardar").click()
        time.sleep(2)

    # 4. Click en Eliminar del contacto
    driver.find_element(
        By.XPATH,
        f"//table[@id='tblContactos']//tr[td[contains(normalize-space(),'{nombre_a_eliminar}')]]//button[contains(text(),'Eliminar')]"
    ).click()

    # Si tu app usa alert() para confirmar, descomenta esto:
    # try:
    #     alert = driver.switch_to.alert
    #     alert.accept()
    # except:
    #     pass

    time.sleep(2)

    # 5. Validar que YA NO esté en la tabla
    tbody = driver.find_element(By.ID, "tblContactosBody")
    assert nombre_a_eliminar not in tbody.text

    driver.quit()
