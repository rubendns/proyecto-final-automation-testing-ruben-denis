from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT = (By.ID, "checkout")
    NOMBRE = (By.ID, "first-name")
    APELLIDO = (By.ID, "last-name")
    CODIGO_POSTAL = (By.ID, "postal-code")
    CONTINUAR = (By.ID, "continue")
    FINALIZAR = (By.ID, "finish")
    MENSAJE_CONFIRMACION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def completar_compra(self, nombre, apellido, codigo_postal):
        self.driver.find_element(*self.CARRITO).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT)
        ).click()

        campo_nombre = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.NOMBRE)
        )

        campo_nombre.send_keys(nombre)

        campo_apellido = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.APELLIDO)
        )

        campo_apellido.send_keys(apellido)

        campo_postal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CODIGO_POSTAL)
        )

        self.driver.execute_script(
            """
            const campo = arguments[0];
            const valor = arguments[1];

            const setter = Object.getOwnPropertyDescriptor(
                HTMLInputElement.prototype, 'value'
            ).set;

            setter.call(campo, valor);
            campo.dispatchEvent(new Event('input', { bubbles: true }));
            campo.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            campo_postal,
            codigo_postal,
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver: campo_postal.get_attribute("value") == codigo_postal
        )

        boton_continuar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUAR)
        )

        self.driver.execute_script("arguments[0].click();", boton_continuar)

        boton_finalizar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINALIZAR)
        )

        self.driver.execute_script("arguments[0].click();", boton_finalizar)

    def obtener_confirmacion(self):
        mensaje = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MENSAJE_CONFIRMACION)
        )
        return mensaje.text
