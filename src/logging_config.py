# logging_config.py
import logging
import os

# Crear carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

# Crear logger principal
logger = logging.getLogger("pipeline")
logger.setLevel(logging.DEBUG)  # Guarda todo en archivo

# Formato de salida
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s"
)

# Handler para consola (INFO+)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Handler para archivo (DEBUG+)
file_handler = logging.FileHandler("logs/pipeline.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Evitar duplicados si se importa varias veces
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
