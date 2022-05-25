"""
función solución jugar(baraja) entrada una baraja de cartas,
además, debe de retornar los
puntajes del jugador 1 y 2 respectivamente
"""
baraja=[    ]
def jugar(baraja):
    jugador1=0
    jugador2=0
    while len(baraja)>0:
        jugador1+=baraja.pop()
        jugador2+=baraja.pop()
    return jugador1,jugador2
jugar()

"""
la función juego le entra una baraja de longitud 52 de tipo tupla
y le salen los puntajes de los jugadores 1 y 2 respectivamente
"""
def juego(baraja):
    jugador1=0
    jugador2=0
    while len(baraja)>0:
        jugador1+=baraja.pop()
        jugador2+=baraja.pop()
    return jugador1,jugador2
#invocar la función juego 
juego() 
