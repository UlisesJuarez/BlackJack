############### Blackjack Project #####################
#Author:Ulises Juarez Espinoza
import random 
import os
from figura import*
cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def repartir_carta():
    """Devuelve una carta al azar"""
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta=random.choice(cartas)
    return carta

def calculaPuntuacion(cartas):
    """Toma un conjunto de cartas y devuelve la puntuacion calculada de ellas"""
    if sum(cartas)==21 and len(cartas)==2:
        return 0
    if 11 in cartas and sum(cartas)>21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def compara(puntuacionUsuario,puntuacionOrdenador):
    if puntuacionUsuario==puntuacionOrdenador:
        return "Empate :)"
    elif puntuacionOrdenador==0:
        return "Perdite :(, el oponente tiene un BlackJack"
    elif puntuacionUsuario==0:
        return "Ganaste con un BlackJack! :)"
    elif puntuacionUsuario>21:
        return "Te pasaste. Has perdido :("
    elif puntuacionOrdenador>21:
        return "El oponente se paso. Has ganado!"
    elif puntuacionUsuario>puntuacionOrdenador:
        return "Ganaste :)"
    else:
        return "Perdiste :("

def jugar():
    print(logo)
    cartas_usuario = []
    cartas_computadora = []
    juegoTerminado=False

    for i in range(2):
        cartas_usuario.append(repartir_carta())
        cartas_computadora.append(repartir_carta())

    while not juegoTerminado:
        puntuacion_usuario=calculaPuntuacion(cartas_usuario)
        puntuacion_computadora=calculaPuntuacion(cartas_computadora)

        print(f"Tus cartas: {cartas_usuario}, puntacion actual: {puntuacion_usuario}")
        print(f"Primera carta del ordenador: {cartas_computadora[0]}")
        print("****************************************************************")
        if puntuacion_usuario==0 or puntuacion_computadora==0 or puntuacion_usuario>21:
            juegoTerminado=True
        else:
            eleccion=input("Escribe\n\t'si' para obtener otra carta\n\t'no' para pasar\n\t: ").lower()
            if eleccion=="si":
                cartas_usuario.append(repartir_carta())
            else:
                juegoTerminado=True

    while puntuacion_computadora!=0 and puntuacion_computadora<17:
        cartas_computadora.append(repartir_carta())
        puntuacion_computadora=calculaPuntuacion(cartas_computadora)
    print("*******************************************************************")
    print(f"Tu mano final es: {cartas_usuario}, puntuacion final: {puntuacion_usuario}")
    print(f"Mano final ordenador: {cartas_computadora}, puntuacion final: {puntuacion_computadora}")
    print(compara(puntuacion_usuario,puntuacion_computadora))
    print("--------------------------------------------------------------------------")


while input("Te gustaria jugar BlackJack\n\t'si' para jugar\n\t'no' para salir\n\t: ").lower()=="si":
    os.system("cls")
    jugar()

