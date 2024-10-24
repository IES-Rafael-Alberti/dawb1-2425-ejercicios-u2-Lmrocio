'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''

def pedir_num():
    num = int(input("Introduzca un número: "))
    return num


def comprobar_num(num):
    if num%2 == 0:
        par = True
    else: 
        par = False
    return par

def main():
    num = pedir_num()
    if comprobar_num(num) == True:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")
        

if __name__ == '__main__':
    main()