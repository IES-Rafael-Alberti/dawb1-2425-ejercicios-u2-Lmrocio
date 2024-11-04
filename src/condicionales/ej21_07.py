'''
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''

def datos_entrada():
    renta = float(input("Introduzca su renta anual: "))
    return renta

def tipo_impositivo(renta):
    if renta < 10000:
        tipo = '5%'
    elif renta >= 10000 and renta < 20000:
        tipo = '15%'
    elif renta >= 20000 and renta < 35000:
        tipo = '20%'
    elif renta >= 35000 and renta < 60000:
        tipo = '30%'
    else:
        tipo = '45%'
    return tipo


def main():
    renta = datos_entrada()
    tipo = tipo_impositivo(renta)
    print(f"Usted tiene una renta anual de {renta} euros, por lo que le corresponde un tipo impositivo de {tipo}.")


if __name__ == '__main__':
    main()
