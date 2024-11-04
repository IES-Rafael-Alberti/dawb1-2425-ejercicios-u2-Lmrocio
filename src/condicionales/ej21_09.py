'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática 
el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''

def datos_entrada() -> int:
    edad = int(input("Introduzca su edad: "))
    return edad

def precio_por_edad(edad: int) -> int:
    if edad < 4:
        precio = 0
    elif edad >= 4 and edad < 18:
        precio = 5
    elif edad >= 18:
        precio = 10
    return precio


def main():
    edad = datos_entrada()
    precio = precio_por_edad(edad)
    print(f"Usted tiene {edad} años, por lo que debe abonar {precio} euros.")




if __name__ == '__main__':
    main()