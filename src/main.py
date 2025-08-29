import python_automatizacion
from python_automatizacion.datos import utilidades
from python_automatizacion.automatizacion import limpieza

nombre_archivo = utilidades.obtener_nombre_archivo()

ruta_archivo = utilidades.obtener_ruta_archivo(nombre_archivo)

df = utilidades.leer_archivo(ruta_archivo)

print("Descripción del DataFrame original:")
print(limpieza.df_describe(df))

df_transformado = limpieza.transformar_columnas(df)

print("Descripción del DataFrame transformado:")
print(limpieza.df_describe(df_transformado))

output_file = utilidades.guardar_archivo(df_transformado)

print("Proceso completado. Archivo guardado en:", output_file)