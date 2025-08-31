import python_automatizacion
from python_automatizacion.datos import utilidades, graficos,vistas
from python_automatizacion.automatizacion import limpieza
print("Bienvenido al programa de automatización de datos.")
print("Asegúrate de tener tus archivos en la carpeta 'data'.")
print("Los archivos procesados se guardarán en la carpeta 'exports'.")
print("Antes de empezar selecciona el archivo que deseas procesar de la carpeta 'data'.")
nombre_archivo = utilidades.obtener_nombre_archivo()

ruta_archivo = utilidades.obtener_ruta_archivo(nombre_archivo)

df = utilidades.leer_archivo(ruta_archivo)

print("Iniciando el proceso...")
utilidades.pausa()
utilidades.limpiar_pantalla()
print("Menu de opciones de limpieza y transformación de datos:")

while True:
    try:
        opcion = int(input(
        "1. Analizar archivos\n" 
        "2. Graficos\n"        
        "3. Transformar columnas (cambia edad a numeros y formato a nombres)\n" 
        "4. Filtrar datos\n" 
        "5. Eliminar filas con valores nulos\n" 
        "6. Eliminar duplicados\n" 
        "7. Renombrar columnas\n" 
        "8. Salir y guardar el programa\n" 
        "Seleccione una opción (1-8): "))
        if opcion < 1 or opcion > 8:
            print("Por favor, ingresa un número entre 1 y 7.")
            raise ValueError
        if opcion == 1:
            utilidades.limpiar_pantalla()
            limpieza.analisis(df)
            utilidades.limpiar_pantalla()
        elif opcion == 2:
            utilidades.limpiar_pantalla()
            opcion_grafico = graficos.menu_graficos()
            df = graficos.hacer_graficos(df, opcion_grafico)
            utilidades.pausa()
        elif opcion == 3:
            utilidades.limpiar_pantalla()
            df = limpieza.transformar_columnas(df)
            print("Transformación de columnas completada.")
            utilidades.pausa()
        elif opcion == 4:
            utilidades.limpiar_pantalla()
            df = limpieza.filtrar_datos(df)
            print("Filtrado de datos completado.")
            utilidades.pausa()
        elif opcion == 5:
            utilidades.limpiar_pantalla()
            df = limpieza.eliminar_filas_nulas(df)
            print("Eliminación de filas con valores nulos completada.")
            utilidades.pausa()
        elif opcion == 6:
            utilidades.limpia_pantalla()
            df = limpieza.eliminar_duplicados(df)
            print("Eliminación de duplicados completada.")
            utilidades.pausa()
        elif opcion == 7:
            utilidades.limpiar_pantalla()
            df = limpieza.renombrar_columnas(df)
            print("Renombrado de columnas completado.")
            utilidades.pausa()
        elif opcion == 8:
            print("Saliendo del programa.")
            utilidades.guardar_archivo(df)
            break
    
    except ValueError:
        print("Por favor, ingresa un número válido entre 1 y 7.")
        continue


