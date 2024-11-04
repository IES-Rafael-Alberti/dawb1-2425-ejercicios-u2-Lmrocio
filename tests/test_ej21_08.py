import pytest
from src.condicionales.ej21_08 import nivel_rendimiento, cantidad_dinero

def test_nivel_rendimiento():
    assert nivel_rendimiento (0.0) == 'Inaceptable'
    assert nivel_rendimiento (0.5) == 'Aceptable'
    assert nivel_rendimiento (0.6) == 'Meritorio'


def test_cantidad_dinero():
    assert cantidad_dinero (0.0) == 0.0
    assert cantidad_dinero (0.5) == 960.0 
    assert cantidad_dinero (0.6) == 1440.0