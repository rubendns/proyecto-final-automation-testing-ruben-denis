import json
from pathlib import Path

import pytest
from pages.login_page import LoginPage

from utils.logger import obtener_logger

logger = obtener_logger(__name__)

RUTA_JSON = Path(__file__).resolve().parents[2] / "data" / "usuarios.json"

with open(RUTA_JSON, encoding="utf-8") as archivo:
    usuarios = json.load(archivo)["usuarios"]


@pytest.mark.parametrize(
    "usuario", usuarios, ids=[usuario["tipo"] for usuario in usuarios]
)
def test_login(driver, usuario):
    logger.info("Iniciando test de login: %s", usuario["tipo"])

    pagina_login = LoginPage(driver)
    pagina_login.abrir()

    pagina_login.iniciar_sesion(usuario["username"], usuario["password"])

    logger.info("Formulario de login enviado")

    if usuario["tipo"] == "valido":
        assert "inventory.html" in driver.current_url
        logger.info("Login válido realizado correctamente")
    else:
        mensaje_error = pagina_login.obtener_error()

        assert "Username and password do not match" in mensaje_error

        logger.info("Login inválido rechazado correctamente")
