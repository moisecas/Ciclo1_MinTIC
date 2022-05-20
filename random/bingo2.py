"""
Función revolver numeros de un bingo y mostrar el mínimo de balotas para ganar
"""
import random
lista=[]
for i in range(0,15):
    lista.append(random.randint(1,75))  #genera un número aleatorio entre 1 y 75
print(lista)
