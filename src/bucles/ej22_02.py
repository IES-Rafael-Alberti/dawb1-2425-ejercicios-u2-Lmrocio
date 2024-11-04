'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

def datos_entrada() -> int:
    edad = int(input("Introduzca su edad: "))
    return edad


def crear_anos(edad: int):
    cadena = ""
    for i in range(1, edad+1):
        cadena += str(i) + " "
    return cadena

        

def main():
    edad = datos_entrada()
    cadena = crear_anos(edad)
    print(f"Usted ha cumplido los años: {cadena}")
    


if __name__ == '__main__':
    main()
