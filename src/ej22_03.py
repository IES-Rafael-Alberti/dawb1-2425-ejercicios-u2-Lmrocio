'''
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas
'''

# NO ESTÁ TERMINADO
def datos_entrada():
    num = int(input("Introduzca un número entero positivo: "))
    return num

def mostrar_impares(num):
    cadena = ''
    for i in range(2, num):
        resto = i%2
        if resto != 0:
            candena = cadena + i
            print(f"{i}") #ME QUEDÉ AQUI
        else:
            print(", ")


def main():
    num = datos_entrada()
    print(f"Para el número {num} encontramos los primos:\n 1")
    mostrar_impares(num)
    if num%2 == 0:
        print(".")
    else:
        print(f", {num}.")


if __name__ == '__main__':
    main()