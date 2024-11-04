"""
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) 
y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
"""

def datos_entrada() -> str:
    frase = input("Introduzca una frase: ")
    return frase


def comprobar_palabra(frase: list) -> int:
    contador_palabras = 0
    letras = 0
    letras2= 0
    palabra = ""
    for i in frase:
        letras = len(i)
        if letras > letras2:
            letras2 = letras
            palabra = i
        contador_palabras += 1
    return contador_palabras, palabra
    

def main():
    frase = datos_entrada().split(" ")
    contador_palabras, palabra = comprobar_palabra(frase)
    print(f"La palabra más larga es {palabra}, de un total de {contador_palabras} palabras ingresadas.")


if __name__ == '__main__':
    main()