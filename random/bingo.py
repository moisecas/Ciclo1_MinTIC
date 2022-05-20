"""
Juego de Bingo 
"""
from random import shuffle 
numberlist=list(range(1,76))
calleednumbers=[]
shuffle(numberlist) 

for i in range(10): 
    chosenumber=numberlist.pop()
    calleednumbers.append(chosenumber) 


print(calleednumbers)  

for i in range(10): 
    check=int(input("Ingrese un número: "))
    if check in calleednumbers: 
        print("Ganaste")
    else: 
        print("Perdiste")


