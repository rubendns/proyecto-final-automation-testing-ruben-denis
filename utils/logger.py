import logging
from pathlib import Path


RUTA_LOGS = Path(__file__).resolve().parents[1] / "logs"
RUTA_LOGS.mkdir(exist_ok=True)

ARCHIVO_LOG = RUTA_LOGS / "ejecucion.log"


def obtener_logger(nombre):
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        archivo = logging.FileHandler(ARCHIVO_LOG, encoding="utf-8")

        formato = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        archivo.setFormatter(formato)
        logger.addHandler(archivo)

    return logger
