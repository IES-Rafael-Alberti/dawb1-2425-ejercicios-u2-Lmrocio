'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''

def pedir_edad():
    edad =int(input("Introduzca su edad: "))
    return edad


def mostrar_edad(edad):
    if edad >= 18 and edad <= 100:
        print("GENIAL, eres mayor de edad.")
    elif edad >=0  and edad < 18:
        print("Lo siento, eres menor de edad.")
    else:
        print("Creo que esa no es tu verdadera edad.")


def main():
    edad = pedir_edad()
    mostrar_edad(edad)


if __name__ == '__main__':
    main()