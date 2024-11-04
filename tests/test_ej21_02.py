import pytest
from src.condicionales.ej21_02 import comprobar_contrasenas

def test_comprobar_contrasenas():
    assert comprobar_contrasenas('hola', 'hola') == True
    assert comprobar_contrasenas('hola', 'hoola') == False