from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import obtener_logger


logger = obtener_logger(__name__)


def test_agregar_producto_al_carrito(driver):
    logger.info("Iniciando test del carrito")

    pagina_login = LoginPage(driver)
    pagina_login.abrir()
    pagina_login.iniciar_sesion("standard_user", "secret_sauce")

    logger.info("Sesión iniciada correctamente")

    pagina_inventario = InventoryPage(driver)
    pagina_inventario.agregar_mochila_al_carrito()

    logger.info("Producto agregado al carrito")

    cantidad_carrito = pagina_inventario.obtener_cantidad_carrito()

    logger.info("Cantidad de productos en carrito: %s", cantidad_carrito)

    assert cantidad_carrito == 1, (
        f"Se esperaba 1 producto en el carrito, pero se encontraron {cantidad_carrito}"
    )

    logger.info("Test del carrito finalizado correctamente")
