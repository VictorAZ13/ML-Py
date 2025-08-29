def df_describe(df):
    print(df.info())
    return df.describe()

def transformar_columnas(df):

    df['nombre'] = df['nombre'].astype(str)  # Asegurarse de que la columna es de tipo string
    df['nombre'] = df['nombre'].str.upper()
    df['edad'] = df['edad'].astype(int)

    return df