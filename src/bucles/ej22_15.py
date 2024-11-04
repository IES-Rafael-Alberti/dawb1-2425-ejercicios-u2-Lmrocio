"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, 
mostrar la sumatoria de todos los números positivos ingresados.
"""
def datos_entrada():
    try:
        num = int(input("Introduzca un número entero: "))
        return num
    except:
        print("El valor introducido no es válido.")


def main():
    num = datos_entrada()
    suma = 0
    while num != 0:
        if num > 0:
            suma += num
        num = datos_entrada()

    print(f"La suma de todos los números positivos es {suma}.")

    
if __name__ == '__main__':
    main()