"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
def crear_tabla(i):
    tabla = ""
    for j in range(1, 11, 1):
        tabla += str(i) + " x " + str(j) + " = " + str(j*i) + "\n" 
    return tabla


def main():
    for i in range(1, 11, 1):
        print(crear_tabla(i))
    
if __name__ == '__main__':
    main()