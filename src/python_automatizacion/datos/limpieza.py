from os import system
import pandas as pd
import numpy as np
from python_automatizacion.datos import utilidades

def analisis(df,con_batch = False):
    if not con_batch: #Para no pedir input en el batch
        print("Análisis del DataFrame:")
        while True:
            opcion = input("Menu de analisis de DataFrame:\n"
            "1. Ver descripción general\n"
            "2. Ver tipos de datos\n" 
            "3. Ver columnas y filas\n" 
            "4. Ver frecuencias de valores\n" 
            "5. Ver valores unicos de una columna\n" 
            "6. Ver estadísticas descriptivas\n" 
            "7. Calculo de la media/mediana/moda\n"
            "8. Porcentaje de valores nulos por columna\n"
            "9. Salir\n"
            "Seleccione una opción (1-9): ")
            if opcion == '1':
                print("Descripción general del DataFrame:\n")
                df.info()
                system("pause")
                system("cls")
            elif opcion == '2':
                print("Tipos de datos de cada columna:\n")
                print(df.dtypes)
                system("pause")
                system("cls")
            elif opcion == '3':
                print(f"Número de filas: {df.shape[0]}, Número de columnas: {df.shape[1]}")
                system("pause")
                system("cls")
            elif opcion == '4':
                print("Columnas disponibles:", df.columns)
                columna = input("Ingrese el nombre de la columna para ver las frecuencias de valores: ")
                if columna in df.columns:
                    print(f"Frecuencias de valores en la columna '{columna}':\n")
                    print(df[columna].value_counts().head())
                else:
                    print(f"La columna '{columna}' no existe en el DataFrame.")
                system("pause")
                system("cls")
            elif opcion == '5':
                print("Columnas disponibles:", df.columns)
                columna = input("Ingrese el nombre de la columna para ver los valores únicos: ")
                if columna in df.columns:
                    print(f"Valores únicos en la columna '{columna}':\n")
                    print(df[columna].unique())
                else:
                    print(f"La columna '{columna}' no existe en el DataFrame.")
                system("pause")
                system("cls")
            elif opcion == '6':
                print("Estadísticas descriptivas del DataFrame:\n")
                print(df.describe(include='all'))
                system("pause")
                system("cls")
            elif opcion == '7':
                print("Columnas disponibles:", df.select_dtypes(include=[np.number]).columns)
                while True:
                    columna = input("Ingrese el nombre de la columna para calcular media/mediana/moda: ")
                    if columna in df.select_dtypes(include=[np.number]).columns:
                        print(f"Media de '{columna}': {df[columna].mean()}")
                        print(f"Mediana de '{columna}': {df[columna].median()}")
                        print(f"Moda de '{columna}': {df[columna].mode()[0]}")
                        break
                    else:
                        print(f"La columna '{columna}' no existe en las opciones.")
                        system("pause")
                        system("cls")
                system("pause")
                system("cls")
            elif opcion == '8':
                print("Porcentaje de valores nulos por columna:\n")
                print((df.isnull().mean() * 100).round(2))
                system("pause")
                system("cls")

            elif opcion == '9':
                print("Saliendo del menú de análisis.")
                break
            elif opcion not in [str(i) for i in range(1,10)]:
                print("Por favor, ingresa un número entre 1 y 9.")
                system("pause")
                system("cls")
    else:
        print("Análisis del DataFrame:")
        print("Descripción general del DataFrame:\n")
        df.info()
        print("Tipos de datos de cada columna:\n")
        print(df.dtypes)
        print(f"Número de filas: {df.shape[0]}, Número de columnas: {df.shape[1]}")
        print("Estadísticas descriptivas del DataFrame:\n")
        print(df.describe(include='all'))
        print("Porcentaje de valores nulos por columna:\n")
        print((df.isnull().mean() * 100).round(2))
        for col in df.select_dtypes(include=[np.number]).columns:
            print(f"Media de '{col}': {df[col].mean()}")
            print(f"Mediana de '{col}': {df[col].median()}")
            print(f"Moda de '{col}': {df[col].mode()[0]}")
        system("pause")
        system("cls")

def transformar_columnas(df):
    print("Transformar columnas de texto a formato nombre y edad a numeros (en base a muestra, se transforman todas las columnas de texto y numericas)")
    n = utilidades.obtener_muestra(df)
    print(f"Tamaño de la muestra calculado: {n}")
    muestra = df.sample(n=n, random_state=1)
    for col in df.columns:
        try:
            muestra_solo_num = pd.to_numeric(muestra[col], errors='coerce')
            ratio = muestra_solo_num.notnull().mean()
            if ratio >= 0.8:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            else:
                if muestra.astype(str)[col].str.contains(r"\d",na=False).any(): # Si contiene numeros no se capitaliza
                    df[col] = df[col].astype(str).str.strip()
                else:
                    df[col] = df[col].astype(str).str.strip().str.lower().str.capitalize()
        except:
            df[col] = df[col].astype(str).str.strip().str.lower().str.capitalize()
    print("Transformación completada.")
    print("DataFrame después de renombrar columnas y limpiar cadenas:")
    print(df)
    return df

def eliminar_filas_nulas(df, columnas_nulas = None):
    if columnas_nulas is None:
        print("Elimiar los valores nulos de la columna que selecciones")
        print("Columnas disponibles:", df.columns)
        while True:
            try:
                columna = str(input("Ingrese el nombre de la columna: "))
                if columna in df.columns:
                    break
                else:
                    print("Por favor, ingresa una columna del archivo .")
            except ValueError:
                print(f"Ingresa una columna válida.")
        print(f"Valores nulos en la columna '{columna}': {df[columna].isnull().sum()}")
        confirmacion = input("¿Desea eliminar las filas con valores nulos en esta columna? (s/n): ")
        while True:
            if confirmacion.lower() == 's':
                break
            elif confirmacion.lower() == 'n':
                print("No se eliminaron filas.")
                return df
            else:
                confirmacion = input("Entrada no válida. Por favor, ingrese 's' para sí o 'n' para no: ")
        
        print("Eliminando filas con valores nulos...")
        df_sin_nulos = df.dropna(subset=[columna])
        print(f"Se eliminaron {len(df) - len(df_sin_nulos)} filas con valores nulos.")
        system("pause")
        return df_sin_nulos
    else:
        for columna in columnas_nulas:
            if columna in df.columns:
                print(f"Eliminando filas con valores nulos en la columna '{columna}'...")
                df = df.dropna(subset=[columna])
                print(f"Se eliminaron filas con valores nulos en la columna '{columna}'.")
            else:
                print(f"La columna '{columna}' no existe en el DataFrame. No se eliminaron filas para esta columna.")
        system("pause")
        return df
    
def filtrar_datos(df):
    print("Filtrar datos por columna y valor")
    print("Columnas disponibles:", df.columns)
    while True:
        try:
            columna = str(input("Ingrese el nombre de la columna: "))
            if columna in df.columns:
                break
            else:
                print("Por favor, ingresa una columna del archivo .")
        except ValueError:
            print(f"Ingresa una columna válida.")
    
    print("Valores únicos en la columna seleccionada:", df[columna].unique())
    if df[columna].dtype == 'object':
        while True:
            try:
                valor = str(input("Ingrese el valor para filtrar: "))
                if valor in df[columna].astype(str).values:
                    df_filtrado = df.loc[df[columna] == valor]
                    break
                else:
                    print("El valor no existe en la columna. Inténtalo de nuevo.")
            except ValueError:
                print("Ingresa un valor válido.")
    elif df[columna].dtype in ['int64', 'float64']:
        while True:
            try:
                opcion = int(input("Filtrar por condicion numerica\n"
                "1. Mayor que\n"
                "2. Menor que\n"))
                if opcion not in [1,2]:
                    print("Por favor, ingresa 1 o 2.")
                    continue
                elif opcion == 1:
                    valor = float(input("Ingrese el valor para filtrar (mayor que): "))
                    df_filtrado = df.loc[df[columna] > valor]
                    break
                elif opcion == 2:
                    valor = float(input("Ingrese el valor para filtrar (menor que): "))
                    df_filtrado = df.loc[df[columna] < valor]
                    break
            except ValueError:
                print("Ingresa un valor numérico válido.")
    elif np.issubdtype(df[columna].dtype, np.datetime64):
        while True:
            try:
                opcion = int(input("Filtrar por condicion de fecha\n"
                "1. Antes de una fecha\n"
                "2. Después de una fecha\n"))
                if opcion not in [1,2]:
                    print("Por favor, ingresa 1 o 2.")
                    continue
                elif opcion == 1:
                    valor = input("Ingrese la fecha en formato AAAA-MM-DD para filtrar (antes de): ")
                    fecha = pd.to_datetime(valor, format='%Y-%m-%d', errors='coerce')
                    if pd.isna(fecha):
                        print("Formato de fecha inválido. Inténtalo de nuevo.")
                        continue
                    df_filtrado = df.loc[df[columna] < fecha]
                    break
                elif opcion == 2:
                    valor = input("Ingrese la fecha en formato AAAA-MM-DD para filtrar (después de): ")
                    fecha = pd.to_datetime(valor, format='%Y-%m-%d', errors='coerce')
                    if pd.isna(fecha):
                        print("Formato de fecha inválido. Inténtalo de nuevo.")
                        continue
                    df_filtrado = df.loc[df[columna] > fecha]
                    break
            except ValueError:
                print("Ingresa una fecha válida en formato AAAA-MM-DD.")
        

    print("Vista previa de los datos filtrados: ")
    print(df_filtrado.head())
    
    while True:
        confirmacion = input("¿Desea guardar los datos filtrados? (s/n): ")
        if confirmacion.lower() == 's':
            break
        elif confirmacion.lower() == 'n':
            print("No se guardaron los datos filtrados.")
            return df
        else:
            confirmacion = input("Entrada no válida. Por favor, ingrese 's' para sí o 'n' para no: ")
    
    return df_filtrado

def eliminar_duplicados(df,columnas_duplicadas = None):
    if columnas_duplicadas is None:
        print("Eliminar duplicados de la columna que selecciones")
        print("Columnas disponibles:", df.columns)
        while True:
            try:
                columna = str(input("Ingrese el nombre de la columna: "))
                if columna in df.columns:
                    break
                else:
                    print("Por favor, ingresa una columna del archivo .")
            except ValueError:
                print(f"Ingresa una columna válida.")

        print(f"Valores duplicados de '{columna}': {df[columna].duplicated().sum()}")
        confirmacion = input("¿Desea eliminar las filas con valores duplicados en esta columna? (s/n): ")
        while True:
            if confirmacion.lower() == 's':
                break
            elif confirmacion.lower() == 'n':
                print("No se eliminaron filas.")
                return df
            else:
                confirmacion = input("Entrada no válida. Por favor, ingrese 's' para sí o 'n' para no: ")
        
        print("Eliminando filas duplicadas...")
        df_sin_duplicados = df.drop_duplicates(subset=[columna])
        print(f"Se eliminaron {len(df) - len(df_sin_duplicados)} filas con valores duplicados.")
        system("pause")
        return df_sin_duplicados
    else:
        for columna in columnas_duplicadas:
            if columna in df.columns:
                print(f"Eliminando filas duplicadas en la columna '{columna}'...")
                df = df.drop_duplicates(subset=[columna])
                print(f"Se eliminaron filas duplicadas en la columna '{columna}'.")
            else:
                print(f"La columna '{columna}' no existe en el DataFrame. No se eliminaron filas para esta columna.")
        system("pause")
        return df

def renombrar_columnas(df):
    print("Columnas actuales:", df.columns)
    while True:
        try:
            columna = str(input("Ingrese el nombre de la columna: "))
            if columna not in df.columns:
                continue
            else:
                print("Por favor, ingresa una columna del archivo .")
        except ValueError:
            print(f"Ingresa una columna válida.")
        
        nuevo_nombre = input("Ingrese el nuevo nombre para la columna: ")
        df = df.rename(columns={columna: nuevo_nombre})
        print("Columnas actualizadas:", df.columns)
        otra = input("¿Desea renombrar otra columna? (s/n): ")
        if otra.lower() != 's':
                break
    return df
