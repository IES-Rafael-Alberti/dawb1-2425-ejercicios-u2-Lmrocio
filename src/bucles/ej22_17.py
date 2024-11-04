"""
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
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

def main():
    num = pedir_num()
    suma = suma_digitos(num)
    print(f"La suma de los dígitos de {num} es {suma}.")


if __name__ == '__main__':
    main()