"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene, 
lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""

def pedir_contrasena():
    contra = input("Introduzca una contraseña: ").lower()

    return contra

def comprobar_contrasena(contra):
    acierto = False

    while acierto == False:
        try:
            contra2 = input("Introduzca la contreseña: ").lower()
            if contra != contra2:
                raise NameError ("INCORRECT PASSWORD!!")
            else:
                acierto = True
        except NameError as e:
            print(f"{e}")


def main():
    contra = pedir_contrasena()
    comprobar_contrasena(contra)

if __name__ == '__main__':
    main()