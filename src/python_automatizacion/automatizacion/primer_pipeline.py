import glob
import os
import pandas as pd
import python_automatizacion.datos.utilidades as utilidades
import python_automatizacion.datos.limpieza as limpieza
import python_automatizacion.datos.graficos as graficos


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
        print("Iniciando validación de datos...")

        errores = utilidades.validar_dataset(df,COLUMNAS_OBLIGATORIAS)

        if errores:
            print(f"El archivo {archivo} no paso la validacion se omitira, errores encontrados:")
            for e in errores:
                print(" ",e)
            continue
        else:
            print(f"Archivo validado")
        print("Iniciando limpieza de datos...")
        errores = []
        try: 
            df = limpieza.transformar_columnas(df)
        except Exception as e:
            errores.append(f"Ocurrió un error procesando el archivo {archivo} :  {e}")
        try:
            df = limpieza.eliminar_filas_nulas(df,COLUMNAS_NULAS)
        except Exception as e:
            errores.append(f"Ocurrio un error al eliminar filas nulas en el archivo {archivo} : {e}")  
        try:    
            df = limpieza.eliminar_duplicados(df,COLUMNAS_DUPLICADAS)
        except Exception as e:
            errores.append(f"Ocurrio un error inesperado al eliminar duplicados en {archivo}: {e}")
        if errores:
            print("Se tuvo errores en la limpieza:")
            for err in errores:
                print("  -",err)
        else:
            print("Limpieza de datos completada.")

        print("Realizando análisis de datos...")
        try:
            limpieza.analisis(df,batch)
            print("Análisis de datos completado.")
        except Exception as e:
            print("Error en el analisis de datos ",e)
            
        print("Generando gráficos...")
        errores_graf = []
        for opcion,columnas in graficos_columnas.items():
            for col in columnas:
                try:
                    df_graficos = graficos.hacer_graficos(df,opcion,col,ruta_guardado)
                except Exception as e:
                    errores_graf.append(
                        f"Error en el grafico de la columna {col}"
                    )
                    continue
        if errores_graf:
            print(errores_graf)
            print("Graficos parcialmente generados")
        else:
            print("Gráficos generados.")
        nombre_salida = os.path.basename(archivo).rsplit('.', 1)[0] + "_procesado." + archivo.rsplit('.', 1)[1]
        utilidades.guardar_archivo(df, nombre_salida,ruta_guardado)

    print("Iniciando el proceso...")

    utilidades.pausa()
    utilidades.limpiar_pantalla()

ejecutar_pipeline()
  
