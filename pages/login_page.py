from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.URL)

    def iniciar_sesion(self, usuario, contrasena):
        self.driver.find_element(*self.USERNAME).send_keys(usuario)
        self.driver.find_element(*self.PASSWORD).send_keys(contrasena)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def obtener_error(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
