'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

def datos_entrada():
    sexo = input("Introduzca su sexo: ")
    nombre = input("Introduzca su nombre: ")
    return sexo, nombre


def comprobar_sexo(sexo: str):
    if sexo == 'mujer':
        valor_s = True
    if sexo == 'hombre':
        valor_s = False
    return valor_s


def comprobar_nombre(nombre: str):
    antes_m = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm')
    despues_n = ('n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    
    for n in antes_m:
        if nombre.startswith(antes_m):
            valor_n = True
        else:
            valor_n = False

    return valor_n


def grupo(valor_s: bool, valor_n: bool):
    if (valor_s and valor_n) or (not valor_s and not valor_n):
        print("Perteneces al grupo A.")
    else: 
        print("Perteneces al grupo B.")


def main():
    sexo, nombre = datos_entrada()
    sexo = sexo.lower()
    nombre = nombre.lower()
    valor_s = comprobar_sexo(sexo)
    valor_n = comprobar_nombre(nombre)
    grupo(valor_s, valor_n)



if __name__ == '__main__':
    main()