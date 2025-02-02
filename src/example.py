from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función para crear el WebDriver
def create_driver():
    logger.info("Creando un WebDriver para Chrome")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    
    driver = webdriver.Remote(
        command_executor='http://hub:4444/wd/hub',
        options=options
    )
    return driver

# Función para realizar la prueba
def test_page(driver):
    logger.info("Navegando a la página web")
    driver.get("https://automationintesting.com/selenium/testpage/")
    
    logger.info("Buscando el elemento h1 en la página")
    element = driver.find_element(By.TAG_NAME, "h1")
    
    logger.info(f"El título de la página es: {element.text}")

if __name__ == "__main__":
    try:
        driver = create_driver()
        test_page(driver)
        
    except WebDriverException as e:
        logger.error(f"Error al conectar con el WebDriver: {e}")
    except NoSuchElementException as e:
        logger.error(f"Elemento no encontrado: {e}")
    finally:
        logger.info("Cerrando el navegador")
        driver.quit()
