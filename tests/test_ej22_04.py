import pytest
from src.bucles.ej22_04  import crear_cadena

def test_crear_cadena():
    assert crear_cadena(12) == '12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0'