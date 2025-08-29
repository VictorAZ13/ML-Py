import pandas as pd
import os 
from os import system

def pausa():
    system("pause")
    system("cls")

def limpiar_pantalla():
    system("cls")

def obtener_nombre_archivo():
    print("Lista de archivos guardados: ")
    print(os.listdir("data"))
    while True:
        try:
            nombre_archivo = str(input("Nombre del archivo a procesar (con extensión .csv o .xlsx): "))
            if nombre_archivo.endswith(('.csv','.xlsx')):
                if nombre_archivo in os.listdir("data"):
                    break
                else:
                    print("El archivo no existe en el directorio 'data'. Inténtalo de nuevo.")
            else:
                print("Por favor, ingresa un archivo de la lista con extensión .csv o .xlsx.")
            
        except Exception as e:
            print(f"Error al ingresar el nombre del archivo: {e}")
    print("Obteniendo nombre del archivo...")
    return nombre_archivo

def obtener_ruta_archivo(nombre_archivo):
    print("Obteniendo ruta del archivo...")
    system("pause")
    # Obtener el nombre del archivo a partir de la ruta completa
    ruta_archivo = os.path.join("data",nombre_archivo)
    return ruta_archivo
 

def leer_archivo(input_file):
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        df = pd.read_excel(input_file)
    
    print(f"Archivo {input_file} leído correctamente")
    system("pause")
    return df

def guardar_archivo(df):
    output_file = os.path.join("exports",input("Nombre del archivo de salida (con extensión .csv o .xlsx): "))
    while True:
        try:
            if output_file.endswith(('.csv','.xlsx')):
                break
            else:
                output_file = os.path.join("exports",input("Por favor, ingresa un archivo con extensión .csv o .xlsx: "))
        except Exception as e:
            print(f"Error al ingresar el nombre del archivo: {e}")
    
    if output_file.endswith('.xlsx'):
        #Guardar el DataFrame en un nuevo archivo Excel
        df.to_excel(output_file, index=False)
    elif output_file.endswith('.csv'):
        #Guardar el DataFrame en un nuevo archivo CSV
        df.to_csv(output_file, index=False)
    elif os.path.exists(output_file):
        opcion = input("El archivo ya existe. ¿Deseas sobrescribirlo? (s/n): ")
        if opcion.lower() == 's':
            if output_file.endswith('.xlsx'):
                df.to_excel(output_file, index=False)
            elif output_file.endswith('.csv'):
                df.to_csv(output_file, index=False)
            print(f"Archivo sobrescrito como {output_file}")
            system("pause")
            return output_file
        else:
            print("No se guardó el archivo.")
            system("pause")
            return None
    
    print(f"Archivo guardado como {output_file}")

    return output_file

