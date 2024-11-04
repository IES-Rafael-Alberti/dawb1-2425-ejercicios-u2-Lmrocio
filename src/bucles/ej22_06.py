"""
Escribir un programa que pida al usuario un número entero y
muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""

def pedir_num() -> int:
    try:
        num = int(input("Introduzca un número entero: "))
        return num
    except:
        print ("El valor introducido no es válido.")

def crear_fila(i):
    fila = ""
    for i in range(1, i+1, 1):
        fila += "* "
    return fila

def crear_triangulo(num) -> str:
    triangulo =""
    for i in range(1, num+1, 1):
        triangulo += crear_fila(i) + "\n"
    return triangulo

def main():
    num = pedir_num()
    triangulo = crear_triangulo(num)
    print(triangulo)



if __name__ == '__main__':
    main()