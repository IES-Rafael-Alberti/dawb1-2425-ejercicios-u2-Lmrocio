import pytest
from src.condicionales.ej21_09 import precio_por_edad

def test_precio_por_edad():
    assert precio_por_edad(3) == 0
    assert precio_por_edad(5) == 5
    assert precio_por_edad(19) == 10