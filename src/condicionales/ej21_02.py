'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte 
al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide 
con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas
'''

def pedir_contrasenas() -> str:
    contrasena = input("Introduzca una contraseña: ")
    segunda_contrasena = input("Introduzca la contraseña de nuevo: ")
    return contrasena, segunda_contrasena



def comprobar_contrasenas(contrasena: str, segunda_contrasena: str) -> bool:
    contrasena = contrasena.upper()
    segunda_contrasena = segunda_contrasena.upper()

    if contrasena == segunda_contrasena:
        return True
    else:
        return False




def main():
    contrasena, segunda_contrasena = pedir_contrasenas()
    
    if comprobar_contrasenas(contrasena, segunda_contrasena):
        print("¡CORRECTO!, has introducido la contraseña.")
    else:
        print("***ERROR*** No has introducido correctamente la contraseña.")



if __name__ == '__main__':
    main()