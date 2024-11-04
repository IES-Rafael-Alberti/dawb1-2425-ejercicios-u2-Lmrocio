'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''

def pedir_edad() -> int:
    edad =int(input("Introduzca su edad: "))
    return edad


def mostrar_edad(edad: int) -> str:
    if edad >= 18 and edad <= 100:
        return "GENIAL, eres mayor de edad."
    elif edad >=0  and edad < 18:
        return "Lo siento, eres menor de edad."
    else:
        return "Creo que esa no es tu verdadera edad."


def main():
    edad = pedir_edad()
    print(mostrar_edad(edad))


if __name__ == '__main__':
    main()