"""
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
def pedir_num() -> int:
    try:
        num = int(input("Introduzca un número entero: "))
        comprobar_num(num)   
        return num
    except NameError as e:
        print(f"***ERROR*** El valor introducido no es válido. {e}")      
        return None  
    

def comprobar_num(num: int):
    if num < 0:
        raise NameError("El número debe ser positivo.")

def crear_cadena(num) -> str:
    cadena = ""
    for i in range(num, -1, -1):
        cadena += str(i) 
        if i > 0:
            cadena += ", "
    return cadena

def main():
    num = pedir_num()
    if num != None:
        cadena = crear_cadena(num)
        print(f"Para el número {num}, la cuenta atrás sería: {cadena}.")

if __name__ == '__main__':
    main()