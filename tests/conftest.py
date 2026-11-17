import os
from datetime import datetime
from pathlib import Path
import re

import pytest

from selenium import webdriver

import pytest_html

CARPETA_CAPTURAS = Path(__file__).resolve().parents[1] / "screenshots"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when != "call" or not reporte.failed:
        return

    driver = item.funcargs.get("driver")

    if driver is None:
        return

    CARPETA_CAPTURAS.mkdir(exist_ok=True)

    nombre_test = re.sub(r"[^a-zA-Z0-9_-]", "_", item.name)
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")

    ruta_captura = CARPETA_CAPTURAS / f"{nombre_test}_{fecha}.png"

    driver.save_screenshot(str(ruta_captura))

    extras = getattr(reporte, "extras", [])

    extras.append(
        pytest_html.extras.png(
            driver.get_screenshot_as_base64(), name="Captura del fallo"
        )
    )

    reporte.extras = extras


@pytest.fixture
def driver():
    opciones = webdriver.ChromeOptions()

    if os.getenv("CI") == "true":
        opciones.add_argument("--headless=new")
        opciones.add_argument("--no-sandbox")
        opciones.add_argument("--disable-dev-shm-usage")
        opciones.add_argument("--window-size=1920,1080")

    navegador = webdriver.Chrome(options=opciones)

    yield navegador
    navegador.quit()
