import pytest
from src.condicionales.ej21_06 import comprobar_nombre, comprobar_sexo

def test_comprobar_nombre():
    assert comprobar_nombre('maria') == True
    assert comprobar_nombre('zahira') == False


def test_comprobar_sexo():
    assert comprobar_sexo('mujer') == True
    assert comprobar_sexo('hombre') == False