import glob
import os
import pandas as pd
from datetime import datetime
import python_automatizacion.datos.utilidades as utilidades
import python_automatizacion.datos.limpieza as limpieza
import python_automatizacion.datos.graficos as graficos
import python_automatizacion.datos.estadisticas as estadisticas
from logging_config import logger

#Parametros

ruta_datasets = "data/datasets"
ruta_guardado = "exports/batch_ejecutado"
COLUMNAS_DUPLICADAS = ["COD_ACAD"] #Columnas donde se borraran duplicados
COLUMNAS_NULAS = ["DNI_POSTULANTE"] #Columnas donde se borraran filas con nulos
batch = True #Si se quiere correr todo el batch automaticamente sin pedir input
graficos_columnas = {
    1: ["NOMB_PROC_ADM"]
} #Columnas y graficos a generar
COLUMNAS_OBLIGATORIAS = {
    "COD_ACAD" : "object",
    "NOMB_PROC_ADM" : "object",
    "PROGRAMA" : "object"
}


def ejecutar_pipeline():
    logger.info("Bienvenido al programa de automatización de datos.")
    logger.info("Asegúrate de tener tus archivos en la carpeta 'data'.")
    logger.info("Los archivos procesados se guardarán en la carpeta 'exports'.")
    logger.info("Se realizara limpieza, análisis y visualización de datos automáticamente de todos los archivos en la carpeta 'data/datasets':")
    archivos = glob.glob("data/datasets/*")
    if not archivos:
        logger.error("No se encontraron archivos en la carpeta 'data/datasets'. Por favor, agrega archivos y vuelve a intentarlo.")
        return
    for archivo in archivos:
        acciones_realizadas = []
        logger.info(f"Procesando archivo: {archivo}")
        df = utilidades.leer_archivo(archivo)
        logger.info("Iniciando validación de datos...")

        errores = utilidades.validar_dataset(df,COLUMNAS_OBLIGATORIAS)

        if errores:
            logger.error(f"El archivo {archivo} no paso la validacion se omitira, errores encontrados:")
            for e in errores:
                logger.error(f"{e}")
            continue
        else:
            logger.info(f"Archivo validado")
        logger.info("Iniciando limpieza de datos...")
        errores = []
        try: 
            acciones_realizadas.append("Transformar columnas")
            df = limpieza.transformar_columnas(df)
        except Exception as e:
            errores.append(f"Ocurrió un error procesando el archivo {archivo} :  {e}")
        try:
            acciones_realizadas.append("Eliminar filas nulas")
            df = limpieza.eliminar_filas_nulas(df,COLUMNAS_NULAS)
        except Exception as e:
            errores.append(f"Ocurrio un error al eliminar filas nulas en el archivo {archivo} : {e}")  
        try:
            acciones_realizadas.append("Eliminar duplicados")    
            df = limpieza.eliminar_duplicados(df,COLUMNAS_DUPLICADAS)
        except Exception as e:
            errores.append(f"Ocurrio un error inesperado al eliminar duplicados en {archivo}: {e}")
        if errores:
            logger.error("Se tuvo errores en la limpieza:")
            for err in errores:
                logger.error(f"  -{err}")
        else:
            logger.info("Limpieza de datos completada.")

        logger.info("Realizando análisis de datos...")
        try:
            acciones_realizadas.append("Analisis en numpy y pandas")
            limpieza.analisis(df,batch)
            logger.info("Análisis de datos completado.")
            ruta_guardado_json = "exports/batch_analisis_numpy.json"
            logger.info("Analisis en numpy")
            resumen_json = estadisticas.analisis_numpy(df,df.columns,ruta_guardado_json)
            logger.debug(resumen_json)
            logger.info("Analisis de datos en numpy completado")
        except Exception as e:
            logger.error(f"Error en el analisis de datos {e}")
            
        logger.info("Generando gráficos...")
        errores_graf = []
        for opcion,columnas in graficos_columnas.items():
            acciones_realizadas.append("Graficas realizadas")
            for col in columnas:
                try:
                    acciones_realizadas.append(f"Grafico realizado de la {col} ")
                    df_graficos = graficos.hacer_graficos(df,opcion,col,ruta_guardado)
                except Exception as e:
                    errores_graf.append(
                        f"Error en el grafico de la columna {col}"
                    )
                    continue
        if errores_graf:
            for eg in errores_graf:
                logger.error(eg)
            logger.error("Graficos parcialmente generados")
        else:
            logger.info("Gráficos generados.")
        nombre_salida = os.path.basename(archivo).rsplit('.', 1)[0] + "_procesado." + archivo.rsplit('.', 1)[1]
        utilidades.guardar_archivo(df, nombre_salida,ruta_guardado)
        ruta_reporte = generar_reporte(df,archivo,errores,acciones_realizadas)
        logger.info(f"Reporte guardado en {ruta_reporte}")
    logger.info("Proceso Finalizado")
    

    utilidades.pausa()
    utilidades.limpiar_pantalla()

def generar_reporte(df,archivo_orginal,errores= None,acciones = None,ruta ="reports"):
    os.makedirs(ruta,exist_ok=True)
    nombre_salida = os.path.basename(archivo_orginal).rsplit('.',1)[0]+"_report.md"
    ruta_reporte = os.path.join(ruta,nombre_salida)
    if errores is None:
        errores = []
    if acciones is None:
        acciones = []
    with open(ruta_reporte,"w",encoding="utf-8") as f:
        #Cabecera
        f.write(f"# Reporte de procesamiento de datos\n")
        f.write(f"Archivo procesado: {archivo_orginal}\n")
        f.write(f"Fecha de ejecución: {datetime.now()}\n\n")
        f.write(f"## Resumen del archivo: \n\n")
        f.write(f" - Filas: {df.shape[0]}\n")
        f.write(f" - Columnas : {df.shape[1]}\n")
        f.write(df.dtypes.to_markdown() + "\n\n")
        f.write("### Valores nulos (%):\n")
        f.write(((df.isnull().mean()*100).round(2)).to_markdown()+"\n\n")
        f.write("### Estadísticas descriptivas:\n ")
        try:
            f.write(df.describe(include = "all").to_markdown()+"\n\n")
        except Exception as e:
            f.write(f"Errores en los cálculos {e}")
        
        f.write("## Acciones del pipeline: ")
        if acciones:
            for a in acciones:
                f.write(f" - {a}\n")
        else:
            f.write("No se ejecutaron acciones en este archivo \n")
        
        f.write("## Errores encontrados: \n\n ")
        if errores:
            for e in errores:
                f.write(f" - {e}\n")
        else:
            f.write("_Archivo sin errores")
        return ruta_reporte
    
ejecutar_pipeline()
  
