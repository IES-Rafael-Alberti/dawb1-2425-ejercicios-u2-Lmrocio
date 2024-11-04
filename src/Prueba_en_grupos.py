def datos_entrada(num_maximo) -> int:
    num = False 
    while num == False:
        try:
            num = int(input("Introduzca un número positivo: "))
            comprobar_num(num, num_maximo)
        except ValueError as e:
            print(f"La entrada introducida no es correcta. {e}. Intentelo de nuevo.")
            num = False
    return num


def comprobar_num(num, num_maximo):
    if num < 0:
        raise ValueError ("Debe ser un número positivo")
    if num > num_maximo:
        raise ValueError (f"Debe estar en el rango 1-{num_maximo}")
    if not str(num).isdigit():
        raise ValueError ("Debe ser un número")


def hacer_fila_1(i:int) -> str:
    fila = ""
    final = i + 1
    suma = 0
    for i in range(0, final, 1):
        fila += str(i)
        suma += i
        if i < final-1:
            fila += " + "
        if i == final-1:
            fila += " = "
    fila += str(suma)
    
    return fila    


def hacer_piramide_1(num: int) -> str:
    piramide1 = ""
    for i in range(num, -1, -1):
        piramide1 += str(i) + " => " + hacer_fila_1(num, i)
        if i != 0:
            piramide1 += "\n"
    
    return piramide1


def hacer_fila_2(j: int) -> str:
    fila = ""
    suma = 0
    for j in range(j, -1, -1):
        fila += str(j)
        suma += j
        if j > 0:
            fila += " + "
        if j == 0:
            fila += " = "
    fila += str(suma)
    
    return fila  

def hacer_piramide_2(num: int) -> str:
    piramide2 = ""
    for j in range(1, num+1, 1):
        piramide2 += str(j) + " => " + hacer_fila_2(num, j) + "\n"
    
    return piramide2


def main():
    num_maximo = 20
    num = datos_entrada(num_maximo)
    opcion = "s"
    while opcion == "s":
        print(hacer_piramide_1(num))
        print(hacer_piramide_2(num))
        opcion = input("¿Quiere hacer otra pirámide? (s/n): ").lower()
        num = datos_entrada(num_maximo)
    print("¡¡HASTA PRONTO!!")


if __name__ == '__main__':
    main()