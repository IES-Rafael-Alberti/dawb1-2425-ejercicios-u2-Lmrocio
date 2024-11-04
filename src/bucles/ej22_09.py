"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña 
hasta que introduzca la contraseña correcta.
"""

def pedir_contrasena() -> str:
    contra = input("Introduzca una contraseña: ")
    return contra

def comprobar_contrasena(contra):
    comprobar = False
    while not comprobar:
        contra2 = input("Introduzca la contraseña de nuevo: ")
        if contra2 != contra:
            print("***ERROR*** La contraseña introducida no es válida, pruebe de nuevo.")
        else:
            print("Contraseña válida.")
            comprobar = True


def main():
    contra = pedir_contrasena()
    comprobar_contrasena(contra)
    

if __name__ == '__main__':
    main()