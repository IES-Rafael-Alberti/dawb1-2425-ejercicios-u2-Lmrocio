
#Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y entiendes su funcionamiento.


num = [8, 3, 1, 19, 14]


def burbuja_hijo(num: list, i: int) -> list:
    """
    Esta función ordena los números de la lista num, reemplazando el valor de dos posiciones a la vez, si la segunda posición es mayor
    que la primera, en cada vuelta del bucle.

    Args:
        num (list): lista con los cinco números a ordenar.
        i (int): valor enviado desde la función burbuja_padre() para controlar el rango.
    
    Return:
        num (list): lista de los cinco números ordenada, si hemos finalizado el bucle de la función burbuja_padre()
        o semiordenada.

    """
    for j in range(0, 5-i, 1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
    return num


def burbuja_padre(num: list) -> str:
    """
    Esta función crea la cadena ordenado con el resultado final de cada vuelta realizada en la función burbuja_hijo()

    Args:
        num (list): lista con los cinco números a ordenar.

    Return:
        ordenado (str): cadena con los números ordenados tras finalizar todos los bucles de la función.
    """
    ordenado = ""
    for i in range(1, 5, 1):
        ordenado = burbuja_hijo(num, i)
    return ordenado

def main():
    ordenado = burbuja_padre(num)
    print(ordenado)

if __name__ == '__main__':
    main()