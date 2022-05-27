#matrices 
#crear matriz usando numpy
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array(list(range(10)))
print(a)
print(b.shape)#tamaño de la matriz 
print(b.ndim)#dimensiones de la matriz
print(b.dtype)#tipo de dato de la matriz
print(b.size)#numero de elementos de la matriz
print(b.itemsize)#tamaño de cada elemento de la matriz
print(b.nbytes)#numero de bytes de la matriz
print(a[0], a[1],a[2])#imprimir filas

#crea un arreglo bidimensional de 3x3
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
#tamaño de la matriz
print(a.shape)
#dimensiones de la matriz
print(a.ndim)
#tipo de dato de la matriz
print(a.dtype)
#mostrar el contenido de una ubicacion de la matriz
print(a.item(0)) #imprime el primer elemento de la matriz 
#mostrar el contenido de una fila de la matriz
print(a.item(0,0)) #imprime el primer elemento de la primera fila de la matriz

#fila 1 columna 1, primero selecciona la fila y luego la columna 
print(a.item(1,1)) #imprime el primer elemento de la segunda fila de la matriz
#cambiar valor de una posicion de la matriz
a.itemset((1,1),100) #cambia el valor de la segunda fila y la segunda columna de la matriz

#suma de matrices 
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a+b) #suma de matrices 

#linspace crea un arreglo de n elementos entre dos valores 
a=np.linspace(0,10,5)
print(a) #linspace crea un arreglo de 5 elementos entre 0 y 10 

#matplotlib
import matplotlib.pyplot as plt
#dibuja un poligono 
plt.plot([1,2,3,4],[1,4,2,3]) #dibuja un poligono 

#diagrama de dispersion
plt.hist([1,2,3,4,5,6,7,8,9,10]) #dibuja un diagrama de dispersion 
