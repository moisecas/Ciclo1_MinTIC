"""
final
"""

import random

balotas = ["B1", "B2", "B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13","B14","B15", "I16", "I17", "I18","I19","I20","I21","I22"
,"I23","I24","I25","I26","I27","I28","I29", "I30", "N31", "N32", "N33","N34","N35","N36","N37","N38","N39","N40","N41","N42","N43","N44",
 "N45", "G46", "G47", "G48","G49","G50","G51","G52","G53","G54","G55","G56","G57","G58","G59","G60", "O61", "O62","O63","O64","O65","O66"
 ,"O67","O68","O69","O70","O71","O72","O73","O74","O75"]

dicc={}
claves=[]
for i in range(len(balotas)):
    dicc[i+1]=balotas[i]
    claves.append(i+1)
    
clavesB5 = random.sample(range(1, 15), 5)
clavesI5 = random.sample(range(16, 30), 5)
clavesN4 = random.sample(range(31, 45), 4)
clavesG5 = random.sample(range(46, 60), 5)
clavesO5 = random.sample(range(61, 75), 5)

claves=clavesB5+clavesI5+clavesN4+clavesG5+clavesO5

listakeys=list(dicc.keys())
listavalores=list(dicc.values())

balotas_revueltas=[]

for i in claves:
    balotas_revueltas.append(dicc[i])

balotas_revueltas