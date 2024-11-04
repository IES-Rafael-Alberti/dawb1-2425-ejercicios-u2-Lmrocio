"""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números 
pares.
"""

def pedir_num():
    try:
        num = int(input("Introduzca un número entero: "))
        return num
    except:
        print("El valor introducido no es válido.")


def suma_digitos(num: int) -> int:
    suma = 0
    for i in range(0, len(str(num)), 1):
        suma += int(str(num)[i])
    return suma

def comprobar_pares(num, pares):
    if num%2 == 0:
        pares += str(num) + " "

    return pares

def main():
    num = pedir_num()
    pares = ""
    while num != -1:
        suma = suma_digitos(num)
        print (f"La suma de los dígitos es: {suma}")
        pares = comprobar_pares(num, pares)
        num = pedir_num()

    print(f"De los números introducidos, los pares son: {pares}.")


if __name__ == '__main__':
    main()