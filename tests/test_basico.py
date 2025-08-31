import pandas as pd
import numpy as np
import os
from os import system
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Nombre": ['Ana', 'Luis', 'Carlos', 'Ana'],
    "Edad": ['25', None, '35', '25'],
    "Ciudad": ['Tacna', 'Piura', 'Arequipa', 'Lima']
})

df = pd.concat([df,df.iloc[[2]]], ignore_index=True)

df.to_csv("data/test_data.csv", index=False)

print("Archivo de prueba 'test_data.csv' creado en la carpeta 'data'.")

print("Probando cosas")

print("DataFrame original:")
print(df)

print("Probando head():")
print(df.head())

print("Probando info():")
print(df.info())

print("Probando rename():")

#print("Columnas actuales:", df.columns)
#while True:
 #       columna = input("Ingrese el nombre de la columna que desea renombrar: ")
  #      nuevo_nombre = input("Ingrese el nuevo nombre para la columna: ")
   #     df = df.rename(columns={columna: nuevo_nombre})
    #    print("Columnas actualizadas:", df.columns)
     #   otra = input("¿Desea renombrar otra columna? (s/n): ")
      #  if otra.lower() != 's':
 #               break
        
#for col in df.select_dtypes(include=['object']).columns:
#   df[col] = df[col].str.strip().str.lower().str.capitalize()
#print("DataFrame después de renombrar columnas y limpiar cadenas:")
#print(df)

print("Probando KPIs:")
print(f"Número de filas: {df.shape[0]}, Número de columnas: {df.shape[1]}")

print("% de valores nulos por columna:")
print(df.isnull().mean() * 100)

if 'Edad' in df.columns:
    df['Edad'] = pd.to_numeric(df["Edad"], errors='coerce')
    print("Promedio de Edad:",df["Edad"].mean())
    print("Mediana de Edad:",df["Edad"].median())
    print("Moda de Edad:",df["Edad"].mode()[0])

if 'Ciudad' in df.columns:
      df['Ciudad'] = df['Ciudad'].astype(str)  # Asegurarse de que la columna es de tipo string
      print(df['Ciudad'].value_counts().head())


system("cls")

print("Probando groupby():")
agrupado = df.groupby("Ciudad").agg({
      "Edad": ["mean", "min", "max"],
      "Nombre": "count"
}).reset_index()
print("DataFrame original:")
print(df)
print("Estadísticas agrupadas por Ciudad:")
print(agrupado)

system("pause")
system("cls")

print("Probando gráficos:")
print("Gráfico de barras del conteo de ciudades:")
conteo = df['Ciudad'].value_counts()
conteo.plot(kind='bar', color='skyblue')
plt.title('Conteo de Ciudades')
plt.xlabel('Ciudad')
plt.ylabel('Número de ocurrencias')
plt.show()

print("Histograma de Edades:")
df['Edad'].dropna().plot(kind='hist', bins=10, color='lightgreen')
plt.title("Frecuencia de Edades")
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()
system("pause")
system("cls")

