'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

def datos_entrada():
    sexo = input("Introduzca su sexo: ")
    nombre = input("Introduzca su nombre: ")
    return sexo, nombre

def comprobar_sexo(sexo):
    if sexo == 'mujer':
        valor_sexo = True
    if sexo == 'hombre':
        valor_sexo = False
    return valor_sexo

def comprobar_nombre(nombre):
    if nombre[0] ==


def main():
    sexo, nombre = datos_entrada()
    sexo = sexo.upper()


if __name__ == '__main__':
    main()