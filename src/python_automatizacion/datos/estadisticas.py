import numpy as np
import pandas as pd
import json
import os

##Este sera el lugar para nuevas estadisticas con python y guardarlas en json pues son mas rapidas para tener información a la mano

def analisis_numpy(df, columnas = None,ruta_guardado_json = None):
    
    if columnas is not None:

        columnas = [col for col in columnas if df[col].dtype != "O"]
        resumen = {
            col:{
                "media": float(np.mean(df[col])),
                "mediana": float(np.median(df[col])),
                "desviacion" : float(np.std(df[col]))
            }
            for col in columnas
        }
        if ruta_guardado_json:
            with open(ruta_guardado_json,"w",encoding="utf-8") as f:
                json.dump(resumen,f,indent=4,ensure_ascii=False)
        return resumen
    else:

        col = input(f"Seleccione la columma de la siguiente lista: \n {df.select_dtypes(include =[np.number]).columns}")
        print(f"Media de la columna: {np.mean(df[col])}")
        print(f"Mediana de la columna: {np.median(df[col])}")
        print(f"Desviación de la columna: {np.std(df[col])}")
        resumen = {
            col:{
                "media": float(np.mean(df[col])),
                "mediana": float(np.median(df[col])),
                "desviacion" : float(np.std(df[col]))
            }
        }
        nombre = input("Escriba el nombre del archivo json a guardar")
        ruta_guardado_json = os.path.join("exports",f"{nombre}.json")
        with open(ruta_guardado_json,"w",encoding="utf-8") as f:
            json.dump(resumen,f,indent=4,ensure_ascii=False)

        return resumen
