"""
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. 
Imprimir la cantidad de números primos ingresados.
"""
def pedir_num() -> int:
    try:
        num = int(input("Introduzca un número mayor que 1: "))
        num = comprobar_num(num)
        return num
    except:
        print("El valor ingresado es inválido.")

def comprobar_num(num: int) -> int:
    while num < 0:
        print("***ERROR*** El número introducido debe ser mayor de 1.")
        num = int(input("Introduzca de nuevo el valor: "))
    return num

def comprobar_primos(num: int, primos: int) -> int:
    if num%2 != 0:
        primos += 1
    return primos            

def main():
    num = pedir_num()
    primos = 0
    while num != 0:
        num = pedir_num()
        primos = comprobar_primos(num, primos)
    print(f"El total de números primos ingresados es: {primos}")    



if __name__ == '__main__':
    main()