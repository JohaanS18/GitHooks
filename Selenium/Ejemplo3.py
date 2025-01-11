from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar el navegador
browser = webdriver.Chrome()

try:
    # Navegar al sitio web
    browser.get("https://campusvirtualunillanos.co/")

    # Extraer información de usuarios activos y cursos hechos
    elementos = browser.find_elements(By.CLASS_NAME, 'h-100')

    try:
        usuarios_activos = elementos[0].find_element(By.TAG_NAME, 'h3').text
        cursos_hechos = elementos[1].find_element(By.TAG_NAME, 'h3').text

        print(f"Cantidad de usuarios actualmente activos: {usuarios_activos}")
        print(f"Número total de cursos realizados: {cursos_hechos}")
    except IndexError:
        print("Los elementos necesarios no se pudieron localizar en la página.")
    except Exception as e:
        print("Se produjo un error inesperado:", e)

finally:
    # Cerrar el navegador
    print("\nFinalizando la sesión del navegador...")
    browser.quit()
