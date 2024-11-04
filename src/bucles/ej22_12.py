"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
def datos_entrada() -> str:
    frase = input("Introduzca una frase: ")
    letra = input("Introduzca una letra: ")

    return frase, letra

def contar_letra(frase: str, letra: str) -> int:
    num = frase.count(letra)

    return num


def main():
    frase, letra = datos_entrada()
    num = contar_letra(frase, letra)

    print(f"En la frase '{frase}' aparece la letra '{letra}' un total de {num} veces.")


if __name__ == '__main__':
    main()