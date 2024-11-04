"""
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, 
la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, 
no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, 
informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
"""
def pedir_monto():
    try:
        monto = int(input("Introduzca el monto a añadir: "))
        monto = comprobar_monto(monto)
        return monto
    except:
        print(f"El valor ingresado no es válido.")
       

def comprobar_monto(monto):
    while monto < 0:
        print(f"***ERROR*** El número introducido es negativo.")
        monto = int(input("Introduzca un número POSITIVO: "))
    return monto

def suma_monto(res, monto):
    res += monto
    return res

def main():
    res = 0
    monto = pedir_monto()
    while monto != 0:
        res = suma_monto(res, monto)
        monto =pedir_monto()

    if res > 1000:
        res = res - (res*0.1)
    
    print(f"El total a pagar es: {res}")


if __name__ == '__main__':
    main()