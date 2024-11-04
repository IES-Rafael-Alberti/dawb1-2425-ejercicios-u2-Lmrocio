"""
Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). 
Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. 
Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros
 que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
"""

def pedir_titulo() -> str:
        titulo = input("Introduzca el título del libro: ")
        return titulo


def comprobar_digitos(titulo:str, digitos: int) -> int:
    for i in range(0, len(titulo), 1):
        if titulo[i].isdigit():
            digitos += 1
    return digitos



def main():
    titulo = pedir_titulo()
    digitos = 0
    lineas = 0
    while titulo != '*':
        digitos = comprobar_digitos(titulo, digitos)
        if titulo == '/':
            print(f"Línea completa. Aparecen {digitos} dígitos numéricos.")
            digitos = 0
            lineas += 1
        titulo = pedir_titulo()
    print (f"Fin. Se leyeron {lineas} completas.")

if __name__ == '__main__':
    main()