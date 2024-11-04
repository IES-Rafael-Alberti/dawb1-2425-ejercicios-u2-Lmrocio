'''
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
'''
#CAMBIARLO A QUE SOLO ACEPTE VALORES ENTRE 0-1; SI ESTA ENTRE 0.0 Y 0.4 ES 0, SI ESTÁ ENTRE 0.4 Y 0.6 ES 0.4

def datos_entrada() -> float:
    try:
        puntuacion = float(input("Introduzca su puntuación obtenida: "))
        if 0.0 <= puntuacion <= 1.0:
            return puntuacion
        else:
            raise ValueError("***ERROR*** No ha introducido un valor válido.")
        
    except ValueError as e:
        print(e)

    

def nivel_rendimiento(puntuacion:float) -> str:
    if 0.0 <= puntuacion < 0.4:
        nivel = 'Inaceptable'
    elif 0.4 <= puntuacion < 0.6:
        nivel = 'Aceptable'
    elif 0.6 <= puntuacion:
        nivel = 'Meritorio'
    return nivel


def cantidad_dinero(puntuacion):
    if 0.0 <= puntuacion < 0.4:
        cantidad = 2400 * 0.0
    elif 0.4 <= puntuacion < 0.6:
        cantidad = 2400 * 0.4
    elif 0.6 <= puntuacion:
        cantidad = 2400 * puntuacion
    return cantidad

def main():
    puntuacion = datos_entrada()
    nivel = nivel_rendimiento(puntuacion)
    cantidad = cantidad_dinero(puntuacion)
    print(f"Su puntuación es de {puntuacion}, obteniendo el nivel de rendimiento {nivel} y será premiado con {cantidad} euros.")


if __name__ == '__main__':
    main()
