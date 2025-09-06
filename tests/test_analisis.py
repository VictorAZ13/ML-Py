import pandas as pd
from python_automatizacion.datos import estadisticas
from python_automatizacion.datos import limpieza

def test_analisis_numpy():
    df = pd.DataFrame({"x":[1,2,3,4,5]})
    resumen = estadisticas.analisis_numpy(df,["x"])
    assert resumen["x"]["media"] == 3
    assert resumen["x"]["mediana"] == 3

def test_analisis_pd(capsys):
    df = pd.DataFrame({"x":[1,2,3,4,5]})
    limpieza.analisis(df,con_batch=True)
    imprimio = capsys.readouterr()
    assert "Descripción general" in imprimio.out
    assert "Media de 'x': 3.0" in imprimio.out

