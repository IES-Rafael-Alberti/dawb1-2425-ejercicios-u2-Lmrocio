'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''

def datos_entrada():
    edad = int(input("Introduzca su edad: "))
    ingresos = float(input("Introduzca su ingreso mensual: "))
    return edad, ingresos


def comprobar_edad(edad):
    if edad >= 16:
        valor_edad = True
    else:
        valor_edad = False
    return valor_edad


def comprobar_ingresos(ingresos):
    if ingresos >= 1000:
        valor_ingresos = True
    else:
        valor_ingresos = False
    return valor_ingresos


def main():
    edad, ingresos = datos_entrada()
    if comprobar_edad(edad) and comprobar_ingresos(ingresos):
        print("Usted debe tributar el impuesto.")
    elif comprobar_edad(edad) and not comprobar_ingresos(ingresos):
        print(f"Su ingreso mensual es de {ingresos}, que no es suficiente para tributar.")
    elif not comprobar_edad(edad) and comprobar_ingresos(ingresos):
        print(f"Su edad es de {edad} años, que no es suficiente para tributar.")
    else:
        print("Para tributar debe tener al menos 16 años y un ingreso mensual igual o superior a 1000€.")

if __name__ == '__main__':
    main()