'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''


def pedir_numeros() -> float:
    num1 = float(input("Introduzca un número: "))
    num2 = float(input("introduzca otro número: "))
    return num1, num2


def division(num1: float, num2: float) -> float:
    div = num1/num2
    return div
    


def  main():
    num1, num2 = pedir_numeros()
    div = division(num1, num2)
    print(f"La división entre el dividendo {num1} y el divisor {num2} da un cociente de {round(div, 3)}.")
    if num2 != 0:
        division(num1, num2)
    else:
        print("**ERROR** El divisor no puede valor 0.")



if __name__ == '__main__':
    main()