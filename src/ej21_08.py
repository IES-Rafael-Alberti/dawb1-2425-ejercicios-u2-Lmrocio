'''
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
'''

def datos_entrada():
    puntuacion = float(input("Introduzca su puntuación obtenida: "))
    return puntuacion


def nivel_rendimiento(puntuacion:float):
    if puntuacion == 0.0:
        nivel = 'Inaceptable'
    elif puntuacion == 0.4:
        nivel = 'Aceptable'
    elif puntuacion == 0.6 or puntuacion > 0.6:
        nivel = 'Meritorio'
    return nivel


def cantidad_dinero(puntuacion):
    if puntuacion == 0.0:
        cantidad = 2400 * 0.0
    elif puntuacion == 0.4:
        cantidad = 2400 * 0.4
    elif puntuacion == 0.6 or puntuacion > 0.6:
        cantidad = 2400 * puntuacion
    return cantidad

def main():
    puntuacion = datos_entrada()
    nivel = nivel_rendimiento(puntuacion)
    cantidad = cantidad_dinero(puntuacion)
    print(f"Su puntuación es de {puntuacion}, obteniendo el nivel de rendimiento {nivel} y será premiado con {cantidad} euros.")


if __name__ == '__main__':
    main()
