import glob
import os
import pandas as pd
import python_automatizacion.datos.utilidades as utilidades
import python_automatizacion.datos.limpieza as limpieza
import python_automatizacion.datos.graficos as graficos
from os import system

#Parametros

ruta_datasets = "data/datasets"
ruta_guardado = "exports/batch_ejecutado"
COLUMNAS_DUPLICADAS = ["COD_ACAD"] #Columnas donde se borraran duplicados
COLUMNAS_NULAS = ["DNI_POSTULANTE"] #Columnas donde se borraran filas con nulos
batch = True #Si se quiere correr todo el batch automaticamente sin pedir input
graficos_columnas = {
    1: ["NOMB_PROC_ADM"]
} #Columnas y graficos a generar

def ejecutar_pipeline():
    print("Bienvenido al programa de automatización de datos.")
    print("Asegúrate de tener tus archivos en la carpeta 'data'.")
    print("Los archivos procesados se guardarán en la carpeta 'exports'.")
    print("Se realizara limpieza, análisis y visualización de datos automáticamente de todos los archivos en la carpeta 'data/datasets':")
    archivos = glob.glob("data/datasets/*")
    if not archivos:
        print("No se encontraron archivos en la carpeta 'data/datasets'. Por favor, agrega archivos y vuelve a intentarlo.")
        return
    for archivo in archivos:
        print(f"Procesando archivo: {archivo}")
        df = utilidades.leer_archivo(archivo)
        print("Iniciando limpieza de datos...")
        df = limpieza.transformar_columnas(df)
        df = limpieza.eliminar_filas_nulas(df,COLUMNAS_NULAS)
        df = limpieza.eliminar_duplicados(df,COLUMNAS_DUPLICADAS)
        print("Limpieza de datos completada.")
        print("Realizando análisis de datos...")
        limpieza.analisis(df,batch)
        print("Análisis de datos completado.")
        print("Generando gráficos...")
        for opcion,columnas in graficos_columnas.items():
            for col in columnas:
                df_graficos = graficos.hacer_graficos(df,opcion,col,ruta_guardado)
        print("Gráficos generados.")
        nombre_salida = os.path.basename(archivo).rsplit('.', 1)[0] + "_procesado." + archivo.rsplit('.', 1)[1]
        utilidades.guardar_archivo(df, nombre_salida,ruta_guardado)

    print("Iniciando el proceso...")

    utilidades.pausa()
    utilidades.limpiar_pantalla()

ejecutar_pipeline()
  
