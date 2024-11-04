"""
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""
def datos_entrada():
    try:
        num = int(input("Introduzca un número entero: "))
        return num
    except:
        print("El valor introducido no es válido.")


def main():
    num = datos_entrada()
    num2 = datos_entrada()
    while num != 0:
        if num > num2:
            num2 = num
        num = datos_entrada()

    print(f"La suma de todos los números introducidos es {num2}.")

    
if __name__ == '__main__':
    main()