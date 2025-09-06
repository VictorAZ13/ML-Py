import pandas as pd
from python_automatizacion.datos import limpieza

def test_eliminar_filas_nulas():
    df = pd.DataFrame({"DNI_POSTULANTE": [123, None, 456]})
    df_out = limpieza.eliminar_filas_nulas(df.copy(), ["DNI_POSTULANTE"])
    assert df_out["DNI_POSTULANTE"].isnull().sum() == 0

def test_eliminar_duplicados():
    df = pd.DataFrame({"COD_ACAD": [1, 1, 2]})
    df_out = limpieza.eliminar_duplicados(df.copy(), ["COD_ACAD"])
    assert len(df_out) == 2