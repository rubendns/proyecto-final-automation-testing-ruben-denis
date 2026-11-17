from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from utils.logger import obtener_logger


logger = obtener_logger(__name__)


def test_compra_exitosa(driver):
    logger.info("Iniciando test de checkout")

    pagina_login = LoginPage(driver)
    pagina_login.abrir()
    pagina_login.iniciar_sesion("standard_user", "secret_sauce")

    logger.info("Sesión iniciada correctamente")

    pagina_inventario = InventoryPage(driver)
    pagina_inventario.agregar_mochila_al_carrito()

    logger.info("Producto agregado al carrito")

    pagina_checkout = CheckoutPage(driver)
    pagina_checkout.completar_compra("Juan", "Perez", "1900")

    logger.info("Formulario de compra completado")

    mensaje = pagina_checkout.obtener_confirmacion()

    logger.info("Mensaje de confirmación: %s", mensaje)

    assert mensaje == "Thank you for your order!"

    logger.info("Test de checkout finalizado correctamente")
