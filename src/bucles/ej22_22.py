"""
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
"""
def pedir_num() -> int:
    try:
        num = int(input("Introduce un número entero y positivo: "))
        num = comprobar_num(num)
        return num
    except:
        print("El valor introducido no es válido.")


def comprobar_num(num) -> int:
    while num < 0:
        print("***ERROR*** El número debe ser POSITIVO.")
        num = int(input("Introduzca un número POSITIVO: "))
    return num


def comprobar_pares_impares(num: int) -> int:
    par = 0
    impar = 0

    for i in range(0, len(str(num)), 1):
        if int(str(num)[i])%2 == 0:
            par += 1
        else:
            impar += 1
    return par, impar

def main():
    num = num = pedir_num()
    total_pares = 0
    total_impares = 0
    while num != 0:
        pares, impares = comprobar_pares_impares(num)
        print(f"Para el número {num}, se han encontrado un total de {pares} dígitos pares y {impares} dígitos impares.")
        total_pares += pares
        total_impares += impares
        num = pedir_num()
    print(f"En total se han contado {total_pares} dígitos pares y {total_impares} dígitos impares.")


if __name__ == '__main__':
    main()