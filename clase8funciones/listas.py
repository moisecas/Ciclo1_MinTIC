 

#listas
text=["cien", "años", "de", "soledad"]
print(text) #imprimo la lista

#imprimo el primer elemento de la lista
print(text[0]) #imprimo el primer elemento de la lista 

#metodos de la lista 
nombres=["juan", "pedro", "maria", "jose"]
nombres.append("jose") #añado un elemento a la lista
print(nombres) #imprimo la lista

#insertar un elemento en una posición específica
nombres.insert(1, "jose") #inserto un elemento en la posición 1, recibe dos parámetros, la posición y el elemento a insertar
print(nombres) #imprimo la lista

#cambiando de posición un elemento de la lista
nombres =["Antonio","Johan","Maria"]
nombres.insert(1, "Guttag")
print(nombres)

#ordenar una lista 
nombres =["Antonio","Johan","Maria"]
nombres.sort() #ordena la lista de manera ascendente menor a mayor 

numeros=[1,2,3,4,5,6,7,8,9,10]
numeros.sort() #ordena la lista de manera ascendente menor a mayor
print(numeros)

numeros.sort(reverse=True) #ordena la lista de manera descendente mayor a menor
print(numeros) 

num=[1,2,3,4,5,6,7,8,9,10]
num.sort(reverse=True) #ordena la lista de manera descendente mayor a menor
print(num)

#lista vacia 
n=[] #declaramos una lista vacia
for i in range(0,10): #iteramos 10 veces
    n.append(i) #añadimos un elemento a la lista, para que sea al lado de otro, i es el elemento que se va a añadir
print(n) #imprimo la lista  
n.sort(reverse=True) #ordeno la lista de manera descendente mayor a menor
print(n) #imprimo la lista 

#numero de vocales en una lista
vocales = ["a", "e", "i", "o","u"] #declaramos una lista con las vocales

palabra = input("Ingrese la palabra: ") #solicitamos la palabra

palablist = [] #declaramos una lista vacia
for i in palabra: #iteramos por cada letra de la palabra
  palablist.append(i)#añadimos el elemento a la lista   

conta= 0 #declaramos un contador para cada vocal que se encuentre en la palabra
conte= 0
conti= 0
conto=0
contu=0

for i in palablist: #iteramos por cada letra de la palabra
  if i == "a" :
    conta += 1 #si la letra es a, sumamos 1 al contador
  if i == "e" :
    conte += 1 #si la letra es e, sumamos 1 al contador
  if i == "i" :
    conti += 1 #si la letra es i, sumamos 1 al contador
  if i == "o" :
    conto += 1 #si la letra es o, sumamos 1 al contador
  if i == "u" :
    contu += 1   #si la letra es u, sumamos 1 al contador

print (f"la vocal a aparece {conta} veces") #imprimo el contador de la vocal a

print (f"la vocal e aparece {conte} veces") #imprimo el contador de la vocal e

print (f"la vocal i aparece {conti} veces") #imprimo el contador de la vocal i

print (f"la vocal o aparece {conto} veces") #imprimo el contador de la vocal o

print (f"la vocal u aparece {contu} veces")     #imprimo el contador de la vocal u

#otra solución 
word = input("Introduce una palabra: ")     #solicitamos la palabra
vocals = ['a', 'e', 'i', 'o', 'u']       #declaramos una lista con las vocales
for vocal in vocals:                    #iteramos por cada vocal de la lista
    times = 0                         #declaramos un contador
    for letter in word:             #iteramos por cada letra de la palabra
        if letter == vocal:     #si la letra es igual a la vocal
            times += 1        #sumamos 1 al contador
    print("La vocal " + vocal + " aparece " + str(times) + " veces") #imprimo el contador de la vocal

#otra solución
z = input("Ingrese una palabra: ")  #solicitamos la palabra
print("La letra a se repite: ", z.count("a"))   #imprimo el contador de la vocal a
print("La letra a se repite: ", z.count("e"))   #imprimo el contador de la vocal e
print("La letra a se repite: ", z.count("i"))   #imprimo el contador de la vocal i
print("La letra a se repite: ", z.count("o"))   #imprimo el contador de la vocal o
print("La letra a se repite: ", z.count("u"))   #imprimo el contador de la vocal u

# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas 
# y muestre por pantalla su producto escalar.

#multipicando posiciones de dos listas 
a = [1, 2, 3] # vector 1
b = [-1, 0, 2] # vector 2
product = 0 # producto escalar
for i in range(len(a)): # iteramos sobre los elementos de la lista
    product += a[i]*b[i] # sumamos el producto de cada elemento 
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))  # imprimimos el producto escalar

#otra solución
v1 = [1,2,3] # vector 1
v2 = [-1,0,2] # vector 2
r = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2] #multiplcacion de los elementos de las listas para obtener el producto escalar
print(r) #imprimo el producto escalar de los vectores 

#usando librerías 
import numpy as np #importamos la librería numpy como np que es un alias para numpy 
a=np.array([1,2,3]) 
b=np.array([-1,0,2])
np.dot(a,b) #multiplicacion de los elementos de las listas para obtener el producto escalar  








