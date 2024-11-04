import pytest
from src.condicionales.ej21_05 import comprobar_edad, comprobar_ingresos

def test_comprobar_edad():
    assert comprobar_edad(14) == False
    assert comprobar_edad(20) == True


def test_comprobar_ingresos():
    assert comprobar_ingresos(10) == False
    assert comprobar_ingresos(1000) == True
