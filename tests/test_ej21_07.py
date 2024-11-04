import pytest
from src.condicionales.ej21_07 import tipo_impositivo

def test_tipo_impositivo():
    assert tipo_impositivo(9000) == '5%'
    assert tipo_impositivo(15000) == '15%'
    assert tipo_impositivo(25000) == '20%'
    assert tipo_impositivo(40000) == '30%'
    assert tipo_impositivo(60001) == '45%'