import numpy as np 

lista=[1,2,3,4,5,6,7,8,9,10]
arr=np.array(lista) #convertimos la lista en un array 
type(arr) #imprimo el tipo de dato de arr 

matriz=[[1,2,3],[4,5,6],[7,8,9]] #declaramos una matriz
matriz=np.array(matriz) #convertimos la matriz en un array
matriz #imprimo la matriz 

arr[0] #imprimo el primer elemento de la lista 
arr[0]+arr[1] #imprimo la suma de los dos primeros elementos de la lista

#ahora con las matrices 
matriz [0][0] #imprimo el primer elemento de la primera fila de la matriz
matriz [0]#imprimo la primera fila de la matriz 
matriz[0,2] #imprimo el tercer elemento de la primera fila de la matriz, 0 es la fila y 2 es el elemento de esa fila

arr2=([1,2,3,4,5,6,7,8,9,10]) #declaramos una lista
arr2[0:2] #imprimo los dos primeros elementos de la lista, seleccionar valores en el array 

arr2[:2] #imprimo los dos primeros elementos de la lista, seleccionar valores en el array
arr2[1:] #imprimo los dos ultimos elementos de la lista, seleccionar valores en el array
arr2[::2] #imprimo los elementos de la lista en posiciones pares, seleccionar valores en el array

arr2[-1] #imprimo el ultimo elemento de la lista 
arr2[-2] #imprimo el penultimo elemento de la lista 
arr2[-3] #imprimo el antepenultimo elemento de la lista

#ahora con las matrices 
matriz=[[1,2,3],[4,5,6],[7,8,9]] #declaramos una matriz
matriz=np.array(matriz) #convertimos la matriz en un array
matriz[1:2] #imprimo la segunda fila de la matriz
matriz[1][1] #imprimo el segundo elemento de la segunda fila de la matriz
matriz[1,0:2] #imprimo el tercer elemento de la segunda fila de la matriz






