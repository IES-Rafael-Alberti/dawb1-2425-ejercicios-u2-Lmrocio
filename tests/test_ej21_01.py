import pytest
from src.condicionales.ej21_01 import mostrar_edad

def test_mostrar_edad():
    assert mostrar_edad(18) == "GENIAL, eres mayor de edad."
    assert mostrar_edad(15) == "Lo siento, eres menor de edad."
    assert mostrar_edad(-1) == "Creo que esa no es tu verdadera edad."