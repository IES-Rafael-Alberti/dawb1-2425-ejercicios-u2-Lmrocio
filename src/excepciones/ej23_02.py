"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta 
ese número separados por comas.
"""

def pedir_num():
    valido = False

    while valido == False:
        try:
            num = int(input("Introduzca un número entero y positivo: "))
        
            if num < 0:
                raise ValueError ("El número debe ser positivo.")
            else:
                valido = True
        
        except ValueError as e:
            print(f"***ERROR*** El valor ingresado es incorrecto. {e}")

    return num

def num_impares(num):
    cadena = ""
    for i in range(1, num, 1):
        if i%2 != 0:
            cadena += str(i)
        else:
            cadena += ", "
    if num%2 != 0:
        cadena += str(num) + "."
    else:
        cadena += "."
    return cadena
    

def main():
    num = pedir_num()
    cadena = num_impares(num)
    print(f"Para el número {num}, encontramos los siguientes impares: {cadena}")


if __name__ == '__main__':
    main()