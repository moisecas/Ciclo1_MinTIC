"""
Librería random
import random, para usarla debe empezar con random.
"""
#simular el lanzamiento de un dado 
import random 
n=random.randint(1,6) #random.randint(1,6) genera un número aleatorio entre 1 y 6
print(n) 


estudiantes=["Juan","Pedro","Ana","Maria","Luis","Jorge"]
indice=random.randrange(0,len(estudiantes)) 
estudiante=estudiantes[indice] 
print(indice,estudiante) #imprime el indice y el nombre del estudiante 

#retorna lista de elementos aleatorios sin que se repita
import random
lista=["Juan","Pedro","Ana","Maria","Luis","Jorge"]
lista=random.sample(lista,2) #len(lista) es la cantidad de elementos de la lista
print(lista) 

