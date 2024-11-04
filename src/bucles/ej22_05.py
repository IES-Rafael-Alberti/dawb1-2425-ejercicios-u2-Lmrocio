"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión
Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
En donde:
 - amount: Cantidad a invertir
 - interest: Interes porcentual anual 
"""

def datos_entrada():
    amount = float(input("Introduzca la cantidad a invertir: "))
    interest = float(input("Introduzca el interés anual: "))
    anos = int(input("Introduzca el número de años: "))

    return amount, interest, anos

def calcular_capital(amount, interest, anos):
    for i in range(1, anos+1, 1):
        amount *= i + (interest/100)
        print(f"Para el {i}º años de inversión, el capital es de: {round(amount, 3)}€.")

def main():
    amount, interest, anos = datos_entrada()
    calcular_capital(amount, interest, anos)

if __name__ == '__main__':
    main()