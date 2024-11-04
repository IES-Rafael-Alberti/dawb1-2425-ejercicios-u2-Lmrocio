"""
Escribir un programa que pida al usuario un número entero positivo y muestre 
por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
Deberá solicitar el número hasta introducir uno correcto.
"""
def pedir_num():
    valido = False

    while valido == False:
        try:
            num = int(input("Introduzca un número entero y positivo: "))
        
            if num < 0:
                raise NameError("El número debe ser positivo.")
            else:
                valido = True
        
        except ValueError as e:
            print(f"***ERROR*** El valor ingresado es incorrecto. {e}")

    return num

def cuenta_atras(num):
    cadena = ""
    for i in range(num, 0, -1):
        cadena += str(i) + ", "
    cadena += "0."

    return cadena


def main():
    num = pedir_num()
    cadena = cuenta_atras(num)

    print(cadena)



if __name__ == '__main__':
    main()