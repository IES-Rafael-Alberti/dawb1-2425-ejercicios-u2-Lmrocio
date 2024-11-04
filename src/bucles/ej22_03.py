'''
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas
'''


def datos_entrada():
    num = int(input("Introduzca un número entero positivo: "))
    return num

def crear_impares(num):
    cadena = '1 '
    for i in range(2, num):
        resto = i%2
        if resto != 0:
            cadena += str(i)
        
        else:
            cadena += ', '
            
    return cadena

def main():
    num = datos_entrada()
    print(f"Para el número {num} encontramos los impares: ")
    cadena = crear_impares(num, cadena)
    if num%2 == 0:
        cadena += '.'
        print (cadena)
        
    else:
        cadena += str(num)
        print (f"{cadena}.")
       


if __name__ == '__main__':
    main()