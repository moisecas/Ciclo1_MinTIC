"""
función solución jugar(baraja) entrada una baraja de cartas,
además, debe de retornar los
puntajes del jugador 1 y 2 respectivamente

Si el jugador toma una carta A y la siguiente carta en la baraja no es una
carta alta, gana 1 punto.
Si el jugador toma una carta J y ninguna de las dos cartas que siguen en
la baraja son una carta alta, gana 2 puntos.
Si el jugador toma una carta Q y ninguna de las tres cartas que siguen
en la baraja son una carta alta, gana 3 puntos.
Si el jugador toma una carta K y ninguna de las cuatro cartas que siguen
en la baraja son una carta alta, gana 4 puntos.
"""
import random 
valor=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
color=("corazon","diamante","trebol","pica")
baraja = [] 

def jugar (baraja):
    for v in valor:
        for c in color:
            carta = "{}  de  {}".format(v,c)
            baraja.append(carta)
    random.shuffle(baraja)
    print(baraja)

"""
la función juego le entra una baraja de longitud 52 de tipo tupla
y le salen los puntajes de los jugadores 1 y 2 respectivamente
"""

#crear tupla de cartas 
baraja=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
def juego(baraja):
    jugador1=0
    jugador2=0
    while len(baraja)>0:
        jugador1+=baraja.pop()
        jugador2+=baraja.pop()
    return jugador1,jugador2
#invocar la función juego 
juego() 
