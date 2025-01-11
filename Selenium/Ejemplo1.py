import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Inicializar el navegador con configuración
service = Service(executable_path="/path/to/chromedriver")  # Cambia a la ruta de tu chromedriver
browser = webdriver.Chrome(service=service)

try:
    # Navegar al formulario
    browser.get("https://demo.guru99.com/test/login.html")
    
    # Interactuar con el formulario
    browser.find_element(By.ID, "email").send_keys(Keys.CONTROL + "a", "ddd")  # Seleccionar y escribir email
    browser.find_element(By.ID, "passwd").send_keys(Keys.CONTROL + "a", "ddd")  # Seleccionar y escribir contraseña

    # Usar ActionChains para enviar el formulario
    action = ActionChains(browser)
    submit_button = browser.find_element(By.ID, 'SubmitLogin')
    action.move_to_element(submit_button).click().perform()

    # Confirmación
    print("Formulario enviado correctamente.")
    
    # Pausar para visualizar el resultado
    time.sleep(4)

finally:
    # Cerrar el navegador
    print("\nCerrando navegador...")
    browser.quit()
