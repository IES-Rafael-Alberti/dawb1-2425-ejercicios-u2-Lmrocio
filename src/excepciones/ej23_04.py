"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje 
"La entrada no es correcta" y lanzará la excepción capturada.
"""

def pedir_num():
    valido = False
    while valido == False:
        try:
            num = input("Escribe un número entero: ")

            if num[0].isdigit():
                if '.' in num:
                    raise NameError ("Debe ser un número entero.")
                else:
                    valido = True
            else:
                raise NameError("No puede ser un caracter, debe ser un número.")

        except NameError as e:
            print(f"La entrada no es correcta. {e}")



def main():
    pedir_num()

if __name__ == '__main__':
    main()