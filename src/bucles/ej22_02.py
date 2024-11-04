'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

def datos_entrada() -> int:
    edad = int(input("Introduzca su edad: "))
    return edad


def mostrar_anos(edad):
    for i in range(1, edad+1):
        print(f"-{i}")

        

def main():
    edad = datos_entrada()
    print("Usted ha cumplido los años: ")
    mostrar_anos(edad)


if __name__ == '__main__':
    main()
