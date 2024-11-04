"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
def datos_entrada():
    entrada = input("Introduzca aquello que quiera: ")

    return entrada


def mostrar_eco(entrada):
    while entrada != 'salir':
        print(entrada)
        entrada = input()

def main():
    entrada = datos_entrada()
    mostrar_eco(entrada)


if __name__ == '__main__':
    main()