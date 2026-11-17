from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    BOTON_AGREGAR = (By.ID, "add-to-cart-sauce-labs-backpack")
    CARRITO_CONTADOR = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def obtener_cantidad_productos(self):
        productos = self.driver.find_elements(*self.PRODUCTOS)
        return len(productos)

    def agregar_mochila_al_carrito(self):
        boton_agregar = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.BOTON_AGREGAR)
        )
        boton_agregar.click()

    def obtener_cantidad_carrito(self):
        contador = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.CARRITO_CONTADOR)
        )
        return int(contador.text)
