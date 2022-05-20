"""
Escribir un programa que permita revolver las balotas de un bingo y retornar el mínimo de balotas para ganar 
revueltas en una tupla

"""
import random
from pickle import TRUE


allNum=[]
for i in range(1,76):
    allNum.append(i)
b_list=[]
i_list=[]
n_list=[]
g_list=[]
o_list=[]
B=[]
I=[]
N=[]
G=[]
O=[]

for allNum in range(1,16):
    b_list.append(allNum)
for allNum in range(16,31):
    i_list.append(allNum)
for allNum in range(31,46):
    n_list.append(allNum)
for allNum in range(46,61):
    g_list.append(allNum)
for allNum in range(61,76):
    o_list.append(allNum)

while TRUE: 
    draw=input("Random number(Y/N): ")
    draw=draw.capitalize
    if draw=="Y":
        B=random.sample(b_list,5)
        I=random.sample(i_list,5)
        N=random.sample(n_list,5)
        G=random.sample(g_list,5)
        O=random.sample(o_list,5)
        print(B,I,N,G,O)



