## Proyecto: Automatización de Datos con Python
 ## Objetivo de la sesión

Implementar estadísticas rápidas con NumPy y un sistema de logging en el pipeline de procesamiento de datos.

## 1️ Estructura del proyecto
python_automatizacion/
│
├─ datos/
│   ├─ __init__.py
│   ├─ utilidades.py
│   ├─ limpieza.py
│   ├─ graficos.py
│   └─ estadisticas.py
│
├─ exports/
├─ logs/
├─ data/
│   └─ datasets/
├─ logging_config.py
└─ pipeline.py

## 2️ Funcionalidades añadidas
✅ Estadísticas con NumPy

Función: analisis_numpy(df, columnas=None, ruta_guardado_json=None)

Genera:

Media (np.mean)

Mediana (np.median)

Desviación estándar (np.std)

Guardado opcional de resultados en JSON:

Carpeta: exports/

Formato legible con indent=4

UTF-8 (ensure_ascii=False)

✅ Logging básico

Configuración en logging_config.py

Captura de:

Información general (INFO)

Errores (ERROR)

Advertencias (WARNING)

Salida:

Consola

Archivo: logs/pipeline.log

Ejemplos de uso:

logger.info("Inicio del pipeline")
logger.error(f"Error procesando archivo: {e}")
logger.warning("Columna X no encontrada")
logger.debug(resumen_json)


logging.captureWarnings(True) captura warnings de Python.

## 3️ Uso del pipeline

Colocar datasets en data/datasets/

Ejecutar pipeline:

python pipeline.py


El pipeline realiza automáticamente:

Validación de columnas obligatorias

Limpieza de duplicados y nulos

Análisis de datos y cálculo de estadísticas con NumPy

Generación de gráficos

Guardado de resultados en exports/

Revisar trazabilidad en logs/pipeline.log

## 4️ Nota

El bloque de estadísticas NumPy es opcional y se puede activar proporcionando columnas y ruta_guardado_json.

Todo el flujo está registrado mediante logging para facilitar debug y seguimiento.