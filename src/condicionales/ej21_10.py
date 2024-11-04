'''
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta 
le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella
y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

def datos_entrada() -> str:
    pizza = input("¿Desea una pizza vegetariana? (Sí o No): ")
    return pizza


def mostrar_ingredientes(pizza:str) -> str:
    if pizza == 'si' or pizza == 'sí':
        print("Puede elegir un ingrediente de los siguientes ingredientes:\n-Pimiento.\n-Tofu.")
        ingrediente = input("INGREDIENTE: ")
        pizza = 'vegetariana'

    elif pizza == 'no':
        print("Puede elegir un ingrediente de los siguientes ingredientes:\n-Peperoni.\n-Jamón.\n-Salmón.")
        ingrediente = input("INGREDIENTE: ")
        pizza = 'no vegetariana'
    else: 
        print("NO ES UNA RESPUESTA VÁLIDA, GRACIAS.")

    return ingrediente, pizza


def main():
    pizza = datos_entrada().lower()
    ingrediente, pizza = mostrar_ingredientes(pizza)
    print(f"Usted a pedido una pizza {pizza}, con los ingredientes:\n-Tomate.\n-Mozzarella.\n-{ingrediente}.\nGRACIAS")



if __name__ == '__main__':
    main()