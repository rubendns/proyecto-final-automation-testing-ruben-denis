import requests
import csv
from pathlib import Path

import pytest

from utils.logger import obtener_logger

logger = obtener_logger(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"

RUTA_CSV = Path(__file__).resolve().parents[2] / "data" / "publicaciones.csv"


def cargar_publicaciones():
    with open(RUTA_CSV, newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def test_obtener_publicacion():
    logger.info("Iniciando prueba API GET")

    respuesta = requests.get(f"{BASE_URL}/posts/1", timeout=15)

    logger.info("Código de respuesta GET: %s", respuesta.status_code)

    assert respuesta.status_code == 200

    datos = respuesta.json()

    assert datos["id"] == 1
    assert "title" in datos
    assert "body" in datos

    logger.info("Prueba API GET finalizada correctamente")


@pytest.mark.parametrize("publicacion", cargar_publicaciones())
def test_crear_publicacion(publicacion):
    logger.info("Iniciando prueba API POST")

    nueva_publicacion = {
        "title": publicacion["title"],
        "body": publicacion["body"],
        "userId": int(publicacion["userId"]),
    }

    respuesta = requests.post(f"{BASE_URL}/posts", json=nueva_publicacion, timeout=15)

    logger.info("Código de respuesta POST: %s", respuesta.status_code)

    assert respuesta.status_code == 201

    datos = respuesta.json()

    assert datos["title"] == nueva_publicacion["title"]
    assert datos["body"] == nueva_publicacion["body"]
    assert datos["userId"] == nueva_publicacion["userId"]
    assert "id" in datos

    logger.info("Publicación creada correctamente: %s", nueva_publicacion["title"])


def test_eliminar_publicacion():
    logger.info("Iniciando prueba API DELETE")

    respuesta = requests.delete(f"{BASE_URL}/posts/1", timeout=15)

    logger.info("Código de respuesta DELETE: %s", respuesta.status_code)

    assert respuesta.status_code == 200

    datos = respuesta.json()

    assert datos == {}

    logger.info("Prueba API DELETE finalizada correctamente")
