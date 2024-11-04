'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
def pedir_edad():
    valido = False

    while valido == False:
        try:
            edad = int(input("Introduzca su edad: "))
            
            if edad < 0:
                raise NameError("La edad debe ser un número positivo.")
        
            elif edad == 0:
                raise NameError ("La edad debe ser superior a 1.")
            
            elif edad > 125:
                raise NameError ("La edad no puede ser mayor de ese número,¡pero enhorabuena, te conservas bien!")

            else:    
                valido = True
                
        except NameError as e:
            print(f"***ERROR*** El valor introducido no es válido. {e}")
        
    return edad 
        
        


def main():
    edad = pedir_edad()
    
    print("Usted ha cumplido los años: ")

    for i in range(1, edad+1, 1):
        print(f"- {i}.")


if __name__ == '__main__':
    main()