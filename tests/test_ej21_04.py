import pytest
from src.condicionales.ej21_04 import comprobar_num

def test_comprobar_num():
    assert comprobar_num(2) == True
    assert comprobar_num(3) == False