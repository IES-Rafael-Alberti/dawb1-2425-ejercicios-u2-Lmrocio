"""
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa.
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error.
El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
"""
def pedir_opcion() -> int:
    try:
        opcion = int(input("Introduzca una opción: "))
        comprobar_opcion(opcion)
        return opcion
    except ValueError as e:
        print("***ERROR*** El valor introducido no es válido.")
    


def comprobar_opcion(opcion):
    if opcion <= 0 or opcion > 3:
        raise ValueError("La opción selecionada no está disponible.") 
  


def mostrar_menu():
    print("1.- Comenzar programa. \n 2.- Imprimir listado. \n 3.- Finalizar programa.")


def main():
    mostrar_menu()
    opcion = pedir_opcion()

    while opcion !=3:
        if opcion == 1:
           print("Has eleigo la opción 1.")
        elif opcion == 2:
            print("Has elegido la opción 2.")
        mostrar_menu()
        opcion = pedir_opcion()
    print("BYE BYE")



if __name__ == '__main__':
    main()