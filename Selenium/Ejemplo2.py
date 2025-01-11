import time
from selenium import webdriver

# Inicializar el navegador
browser = webdriver.Chrome()

try:
    # Abrir tres pestañas y navegar a diferentes páginas
    browser.get("https://www.python.org")  # Primera pestaña
    browser.execute_script("window.open('https://www.wikipedia.org', '_blank');")  # Segunda pestaña
    browser.execute_script("window.open('https://www.github.com', '_blank');")  # Tercera pestaña

    # Obtener todas las pestañas
    tabs = browser.window_handles

    # Navegar entre las pestañas con un delay de 2 segundos
    for tab in tabs:
        browser.switch_to.window(tab)
        print(f"Navegando a: {browser.current_url}")
        time.sleep(2)

finally:
    # Cerrar el navegador
    print("\nCerrando navegador...")
    browser.quit()
