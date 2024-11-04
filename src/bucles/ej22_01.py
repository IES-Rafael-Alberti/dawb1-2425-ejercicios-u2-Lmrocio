'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

def datos_entrada():
    palabra = input("Introduzca una palabra: ")
    return palabra


def mostrar_palabra(palabra):
    for i in range(1, 11):
        print(f"{i}.-{palabra}\n")


def main():
    palabra = datos_entrada()
    mostrar_palabra(palabra)


if __name__ == '__main__':
    main()