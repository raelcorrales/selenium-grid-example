
from selenium import webdriver
from selenium.webdriver.common.by import By


print("# Crear un webdriver para Chrome")
options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='http://hub:4444/wd/hub',
    options=options
)

print("# Navegar a una página web")
driver.get("https://automationintesting.com/selenium/testpage/")

print("# Buscar el elemento h1 en la página")
element = driver.find_element(By.TAG_NAME, "h1")

print("# El titulo de la pagina es: {}".format(element.text))

print("# Cerrar el navegador")
driver.quit()


