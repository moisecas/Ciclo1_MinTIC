"""
Juego de cartas 

1. El jugador 1 comienza sacando una carta, luego el jugador 2 continúa y
así sucesivamente hasta que no quede ninguna carta en la baraja
2. La baraja estándar tiene 13 tipos de cartas: ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
'J', 'Q', 'K'] donde cada tipo aparece 4 veces
3. La baraja estándar tiene 4 tipos de cartas: ['corazon', 'diamante', 'trebol', 'pica']
4. La baraja estándar tiene 52 cartas
5. Cuando un jugador toma una carta alta, tiene la
posibilidad de ganar puntos de la siguiente manera:
● Si el jugador toma una carta A y la siguiente carta en la baraja no es una
carta alta, gana 1 punto.
● Si el jugador toma una carta J y ninguna de las dos cartas que siguen en
la baraja son una carta alta, gana 2 puntos.
● Si el jugador toma una carta Q y ninguna de las tres cartas que siguen
en la baraja son una carta alta, gana 3 puntos.
● Si el jugador toma una carta K y ninguna de las cuatro cartas que siguen
en la baraja son una carta alta, gana 4 puntos
4. función solución jugar(baraja) tendrá como entrada una baraja de cartas,
debe de retornar los puntajes del jugador 1 y 2.
5. En su función solución debe de invocar una función booleana
llamada tiene_cartas_altas(cartas_siguientes) 


"""
import random 
corazon=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
diamante=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
trebol=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
pica=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
baraja=[]

#cuando la carta sea una carta alta, el jugador tiene la posibilidad de ganar puntos
#Puntajes jugador 1 y 2 
def juego(baraja):
    jugador1=0
    jugador2=0
    while len(baraja)>0:
        jugador1+=baraja.pop()
        jugador2+=baraja.pop()
    return jugador1,jugador2
juego(baraja) 

def tiene_cartas_altas(cartas_siguientes):
    if cartas_siguientes[0]=="A":
        return True
    elif cartas_siguientes[0]=="J" and cartas_siguientes[1]=="J":
        return True
    elif cartas_siguientes[0]=="Q" and cartas_siguientes[1]=="Q" and cartas_siguientes[2]=="Q":
        return True
    elif cartas_siguientes[0]=="K" and cartas_siguientes[1]=="K" and cartas_siguientes[2]=="K" and cartas_siguientes[3]=="K":
        return True
    else:
        return False
tiene_cartas_altas(baraja) 