import matplotlib.pyplot as plt 
import pandas as pd
import python_automatizacion.datos.utilidades as utilidades

def menu_graficos():
    print("Menú de opciones de gráficos:")
    print("1. Gráfico de barras")
    print("2. Gráfico de series temporales")
    print("3. Gráfico de dispersión")
    print("4. Histograma")
    print("5. Gráfico de pastel")
    print("6. Salir")
    opcion = int(input("Seleccione una opción (1-6): "))
    while opcion < 1 or opcion > 6:
        print("Por favor, ingresa un número entre 1 y 6.")
        opcion = int(input("Seleccione una opción (1-6): "))
    return opcion

def hacer_graficos(df, opcion):
    if opcion == 1:
        print("Gráfico de barras de la columna seleccionada:")
        
        if df.select_dtypes(include=['object','category']).empty:
            print("No hay columnas categóricas en el DataFrame.")
            utilidades.pausa()
            return df
        else:
            print("Columnas disponibles:")
            print(df.select_dtypes(include=['object','category']).columns)
            columna = input("Ingrese el nombre de la columna categórica para el eje X: ")
            while columna not in df.select_dtypes(include=['object','category']).columns:
                print("Columna inválida. Inténtalo de nuevo.")
                columna = input("Ingrese el nombre de la columna categórica para el eje X: ")
            conteo = df[columna].value_counts()
            conteo.plot(kind='bar', color='green')
            plt.title(f'Conteo de {columna}')
            plt.xlabel(columna)
            plt.ylabel('Frecuencia')
            plt.savefig(f'exports/grafico_barras_{columna}.png')
            plt.show()
            utilidades.pausa()
    elif opcion == 2:
        print("Gráfico de series temporales de la columna seleccionada:")
        if df.select_dtypes(include=['datetime']).empty:
            print("No hay columnas de tipo fecha en el DataFrame.")
            utilidades.pausa()
            return df
        else:
            print("Columnas disponibles:")
            print(df.select_dtypes(include=['datetime','object']).columns)
            columna_fecha = input("Ingrese el nombre de la columna de fecha para el eje X: ")
            while columna_fecha not in df.select_dtypes(include=['datetime']).columns:
                print("Columna inválida. Inténtalo de nuevo.")
                columna_fecha = input("Ingrese el nombre de la columna de fecha para el eje X: ")
            print("Columnas numéricas disponibles:")
            print(df.select_dtypes(include=['number']).columns)
            columna_valor = input("Ingrese el nombre de la columna numérica para el eje Y: ")
            while columna_valor not in df.select_dtypes(include=['number']).columns:
                print("Columna inválida. Inténtalo de nuevo.")
                columna_valor = input("Ingrese el nombre de la columna numérica para el eje Y: ")
            df_ordenado = df.sort_values(by=columna_fecha)
            plt.plot(df_ordenado[columna_fecha], df_ordenado[columna_valor], marker='o', linestyle=':',color = 'skyblue')
            plt.title(f'Serie Temporal de {columna_valor} sobre {columna_fecha}')
            plt.xlabel(columna_fecha)
            plt.ylabel(columna_valor)
            plt.grid(True)
            plt.savefig(f'exports/grafico_series_temporales_{columna_fecha}_{columna_valor}.png')
            plt.show()
            utilidades.pausa()
    elif opcion == 3:
        print("Gráfico de dispersión entre dos columnas numéricas:")
        if len(df.select_dtypes(include=['number']).columns) < 2:
            print("No hay suficientes columnas numéricas en el DataFrame.")
            utilidades.pausa()
            return df
        else:
            print("Columnas numéricas disponibles:")
            print(df.select_dtypes(include=['number']).columns)
            columna_x = input("Ingrese el nombre de la columna numérica para el eje X: ")
            while columna_x not in df.select_dtypes(include=['number']).columns:
                print("Columna inválida. Inténtalo de nuevo.")
                columna_x = input("Ingrese el nombre de la columna numérica para el eje X: ")
            columna_y = input("Ingrese el nombre de la columna numérica para el eje Y: ")
            while columna_y not in df.select_dtypes(include=['number']).columns or columna_y == columna_x:
                print("Columna inválida o igual a la columna X. Inténtalo de nuevo.")
                columna_y = input("Ingrese el nombre de la columna numérica para el eje Y: ")
        
            plt.scatter(df[columna_x], df[columna_y], color='purple', alpha=0.6)
            plt.title(f'Dispersión entre {columna_x} y {columna_y}')
            plt.xlabel(columna_x)
            plt.ylabel(columna_y)
            plt.grid(True)
            plt.savefig(f'exports/grafico_dispersion_{columna_x}_{columna_y}.png')
            plt.show()
            utilidades.pausa()
    elif opcion == 4:
        print("Histograma de la columna numérica seleccionada:")
        if df.select_dtypes(include=['number']).empty:
            print("No hay columnas numéricas en el DataFrame.")
            utilidades.pausa()
            return df
        else:
            print("Columnas numéricas disponibles:")
            print(df.select_dtypes(include=['number']).colums)
            columna = input("Ingrese el nombre de la columna numérica para el histograma: ")
            while columna not in df.select_dtypes(include=['number']).columns:
                print("Columna inválida. Inténtalo de nuevo.")
                columna = input("Ingrese el nombre de la columna numérica para el histograma: ")

            plt.hist(df[columna].dropna(), bins=10, color='orange', edgecolor='black', alpha=0.7)
            plt.title(f'Histograma de {columna}')
            plt.xlabel(columna)
            plt.ylabel('Frecuencia')
            plt.grid(axis='y', alpha=0.75)
            plt.savefig(f'exports/histograma_{columna}.png')
            plt.show()
            utilidades.pausa()
    elif opcion == 5:
        print("Gráfico de pastel de la columna categórica seleccionada:")
        if df.select_dtypes(include=['object','category']).empty:
            print("No hay columnas categóricas en el DataFrame.")
            utilidades.pausa()
            return df
        else:
            print("Columnas disponibles:")
            print(df.select_dtypes(include=['object', 'category']).columns)
            columna = input("Ingrese el nombre de la columna categórica para el gráfico de pastel: ")
            while columna not in df.select_dtypes(include=['object','category']).columns:
                print("Columna inválida. Inténtalo de nuevo.")
                columna = input("Ingrese el nombre de la columna categórica para el gráfico de pastel: ")
            conteo = df[columna].value_counts()
            plt.pie(conteo, labels=conteo.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
            plt.title(f'Gráfico de Pastel de {columna}')
            plt.axis('equal')  # Igualar los ejes para que el pastel sea un círculo
            plt.savefig(f'exports/grafico_pastel_{columna}.png')
            plt.show()
            utilidades.pausa()
    elif opcion == 6:
        print("Saliendo del menú de gráficos.")
        