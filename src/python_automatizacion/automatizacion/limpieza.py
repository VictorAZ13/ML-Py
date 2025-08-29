from os import system
def analisis(df):
    while True:
        opcion = input("Menu de analisis de DataFrame:\n"
        "1. Ver descripción general\n"
        "2. Ver tipos de datos\n" 
        "3. Ver columnas y filas\n" 
        "4. Ver frecuencias de valores\n" 
        "5.Ver valores unicos de una columna\n" 
        "6. Ver estadísticas descriptivas\n" 
        "7. Salir\n"
        "Seleccione una opción (1-7): ")
        if opcion == '1':
            print("Descripción general del DataFrame:\n",df.info())
            system("pause")
            system("cls")
        elif opcion == '2':
            print("Tipos de datos de cada columna:\n")
            print(df.dtypes)
            system("pause")
            system("cls")
        elif opcion == '3':
            print("Descripción de columnas y filas:\n")
            print(df.shape)
            system("pause")
            system("cls")
        elif opcion == '4':
            print("Columnas disponibles:", df.columns)
            columna = input("Ingrese el nombre de la columna para ver las frecuencias de valores: ")
            if columna in df.columns:
                print(f"Frecuencias de valores en la columna '{columna}':\n")
                print(df[columna].value_counts())
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
            print("Saliendo del menú de análisis.")
            break

def transformar_columnas(df):

    df['nombre'] = df['nombre'].astype(str)  # Asegurarse de que la columna es de tipo string
    df['nombre'] = df['nombre'].str.upper()
    df['edad'] = df['edad'].astype(int)

    return df
def eliminar_filas_nulas(df):
    print("Eliminando filas con valores nulos...")
    df_sin_nulos = df.dropna()
    print(f"Se eliminaron {len(df) - len(df_sin_nulos)} filas con valores nulos.")
    system("pause")
    return df_sin_nulos

def filtrar_datos(df):
    print("Filtrar datos por columna y valor")
    print("Columnas disponibles:", df.columns)
    columna = input("Ingrese el nombre de la columna para filtrar: ")
    print("Valores únicos en la columna seleccionada:", df[columna].unique())
    valor = input("Ingrese el valor para filtrar: ")
    df_filtrado = df.loc[df[columna] == valor]
    print("Vista previa de los datos filtrados: ",df_filtrado.head())
    confirmacion = input("¿Desea guardar los datos filtrados? (s/n): ")
    while True:
        if confirmacion.lower() == 's':
            break
        elif confirmacion.lower() == 'n':
            print("No se guardaron los datos filtrados.")
            return df
        else:
            confirmacion = input("Entrada no válida. Por favor, ingrese 's' para sí o 'n' para no: ")
    
    return df_filtrado

def eliminar_duplicados(df):
    print("Eliminando filas duplicadas...")
    df_sin_duplicados = df.drop_duplicates()
    print(f"Se eliminaron {len(df) - len(df_sin_duplicados)} filas duplicadas.")
    system("pause")
    return df_sin_duplicados

def renombrar_columnas(df):
    print("Columnas actuales:", df.columns)
    while True:
        columna = input("Ingrese el nombre de la columna que desea renombrar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre para la columna: ")
        df = df.rename(columns={columna: nuevo_nombre})
        print("Columnas actualizadas:", df.columns)
        otra = input("¿Desea renombrar otra columna? (s/n): ")
        if otra.lower() != 's':
                break
    return df