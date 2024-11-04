"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

def pedir_num() -> int:
    try: 
        num = int(input("Introducir número entero: "))
        return num
    
    except:
        print("El valor introducido no es válido.")

def comprobar_num(num):
    for i in range(2, num, 1):
        if num%i == 0:
            primo = False
            return primo
        else:
            primo = True
            return primo

def main():
    num = pedir_num()
    primo = comprobar_num(num)
    if primo == True:
        print(f"El número {num} SÍ es primo.")
    else:
        print(f"El número {num} NO es primo.")

if __name__ == '__main__':
    main()