from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import obtener_logger


logger = obtener_logger(__name__)


def test_productos_visibles(driver):
    logger.info("Iniciando test de inventario")

    pagina_login = LoginPage(driver)
    pagina_login.abrir()

    logger.info("Iniciando sesión en SauceDemo")

    pagina_login.iniciar_sesion("standard_user", "secret_sauce")

    pagina_inventario = InventoryPage(driver)
    cantidad_productos = pagina_inventario.obtener_cantidad_productos()

    logger.info("Productos encontrados: %s", cantidad_productos)

    assert cantidad_productos > 0, "No se encontraron productos en el inventario"

    logger.info("Test de inventario finalizado correctamente")
