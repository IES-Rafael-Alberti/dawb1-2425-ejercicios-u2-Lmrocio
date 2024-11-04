"""
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, 
indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
"""
def datos_entrada():
    frase = input("Introduzca una frase: ")
    letra = input("Introduzca una letra: ")
    return frase, letra


def comprobar_letra(frase, letra):
    for i in range(0, len(frase), 1):
        if letra == frase[i]:
            return i
        else:
            print(f"No se ha encontrado una coincidencia en la posición {i}.")


def main():
    frase, letra = datos_entrada()
    i = comprobar_letra(frase, letra)
    print(f"Se ha encontrado una coincidencia en la posición {i}")


if __name__ == '__main__':
    main()