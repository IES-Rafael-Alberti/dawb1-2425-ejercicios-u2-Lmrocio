"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje 
"La entrada no es correcta" y lanzará la excepción capturada.
"""

def pedir_num():
    valido = False
    while valido == False:
        try:
            num = int(input("Escribe un número entero: "))
            valido = comprobar_num(num)

        except ValueError as e:
            print(f"***ERROR*** El valor introducido no es válido. {e}")


def comprobar_num(num):
    if type(num) == str:
        raise NameError ("Debe ser un número.")
    if type(num) == float:
        raise NameError ("Debe ser un número entero.")
    if type(num) == int:
        valido = True

    return valido


def main():
    pedir_num()

if __name__ == '__main__':
    main()