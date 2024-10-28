'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
''' 

def datos_entrada() -> int:
    num = 0
    
    while num == 0:
        try: 
            num =int(input("Introduzca un número entero: "))
        except ValueError:
            print("Introduzca un número, y que sea distinto de 0.")
        else:
            return num



def obtener_triangulo(num) -> str:
    cadena = ''
    triangulo = ''
    if num%2 != 0:
        for i in range(1, num+1, 2):
            cadena += str(i) + ' '
            triangulo += cadena[::-1] + '\n'
    else: 
        for i in range(0, num+1, 2):
            cadena += str(i) + ' '
            triangulo += cadena[::-1] + '\n'

    return triangulo



def main():
    num = datos_entrada()
    triangulo = obtener_triangulo(num)
    if num < 0:
        print("El número debe ser mayor o igual que cero.")
    else:
        print(triangulo)



if __name__ == '__main__':
    main()



