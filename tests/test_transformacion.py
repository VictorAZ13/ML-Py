import pandas as pd
import python_automatizacion.datos.limpieza as limp

def test_transformar_numeros():
    df = pd.DataFrame({"edad":["20","30","40"]})
    df_out = limp.transformar_columnas(df.copy())
    assert df_out["edad"].dtype in ["int64","float64"]

def test_transformar_textos():
    df = pd.DataFrame({"nombre": ["jUAN","MARIA","jose"]})
    df_out = limp.transformar_columnas(df.copy())
    assert list(df_out["nombre"]) == ["Juan","Maria","Jose"]
    
