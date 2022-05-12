


import numpy as np  

array=np.random.randint(1,15,(5,5)) #array de 5x5 valores aleatorios entre 1 y 15
matriz=array.random.randint(1,15,(5,5)) #matriz de 5x5 valores aleatorios entre 1 y 15

array.max() #maximo de la matriz
array.min() #minimo de la matriz
array.mean() #promedio de la matriz
array.std() #desviacion estandar de la matriz
array.sum() #suma de la matriz
array.sum(axis=0) #suma de la matriz por filas
array.sum(axis=1) #suma de la matriz por columnas
array.sum(axis=1,keepdims=True) #suma de la matriz por columnas y conserva las dimensiones de la matriz

arr= np.random.randint(1,20,10)#array de 10 valores aleatorios entre 1 y 20
matriz=arr.reshape(2,5) #matriz de 2 filas y 5 columnas
matriz 
arr.max() #maximo de la matriz
matriz.max() #maximo de la matriz
matriz.max(1)#maximo de la matriz por columnas 
arr.armax()#maximo de la matriz 
arr.armax(0)#maximo de la matriz por filas
matriz.min() #minimo de la matriz
matriz.min(0) #minimo de la matriz por filas
arr.ptp()#maximo y minimo de la matriz
matriz.ptp(0)#maximo y minimo de la matriz por filas 
arr.percentile(75)#valor 75% de la matriz
arr.sort()#ordena la matriz de menor a mayor
np.median(arr)#valor medio de la matriz
np.median(arr,axis=0)#valor medio de la matriz por filas
np.std(arr)#desviacion estandar de la matriz 
np.var(arr)#varianza de la matriz
np.mean(arr)#promedio de la matriz
a=np.array([1,2,3,4,5])#array de 5 valores
b=np.array([6,7,8,9,10])#array de 5 valores
np.concatenate((a,b))#concatena los dos arrays
