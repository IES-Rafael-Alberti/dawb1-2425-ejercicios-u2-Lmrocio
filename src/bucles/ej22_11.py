"""
Escribir un programa que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

def pedir_palabra() -> str:
    try:
        palabra = input("Introduzca una palabra: ")
        return palabra
    except:
        print("El valor introducido no es válido.")

def crear_cadena(palabra: str):
    cadena = ""
    for i in range(len(palabra)-1,-1, -1):
        cadena += palabra[i] + " "
    return cadena

def main():
    palabra = pedir_palabra()
    cadena = crear_cadena(palabra)
    print(cadena)


if __name__ == '__main__':
    main()