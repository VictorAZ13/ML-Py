import pandas as pd
import os


def obtener_nombre_archivo():
    print("Por favor, ingresa el nombre de: ")
    print(os.listdir("data"))
    while True:
        try:
            nombre_archivo = str(input("Nombre del archivo (con extensión .csv o .xlsx): "))
            if nombre_archivo.endswith(('.csv','.xlsx')):
                if nombre_archivo in os.listdir("data"):
                    break
                else:
                    print("El archivo no existe en el directorio 'data'. Inténtalo de nuevo.")
            else:
                print("Por favor, ingresa un archivo con extensión .csv o .xlsx.")
            
        except Exception as e:
            print(f"Error al ingresar el nombre del archivo: {e}")
    print("Obteniendo nombre del archivo...")
    return nombre_archivo

def obtener_ruta_archivo(nombre_archivo):
    print("Obteniendo ruta del archivo...")
    # Obtener el nombre del archivo a partir de la ruta completa
    ruta_archivo = os.path.join("data",nombre_archivo)
    return ruta_archivo
 

def leer_archivo(input_file):
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        df = pd.read_excel(input_file)
    
    print(f"Archivo {input_file} leído correctamente")
    return df

def guardar_archivo(df):
    output_file = os.path.join("data",input("Nombre del archivo de salida (con extensión .csv o .xlsx): "))
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
    print(f"Archivo guardado como {output_file}")
    
    return output_file

