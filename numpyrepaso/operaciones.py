import numpy as np 

lista=[1,2,3,4,5,6,7,8,9,10]
lista 
arr=np.arrange(0,10)
arr2=arr.copy()

#operaciones 
arr*2#multiplicacion de arr por 2
1/arr#division de 1 por arr
arr**2#potencia de arr
arr+arr2#suma de arr y arr2
arr-arr2#resta de arr y arr2
matriz=arr.reshape(2,5)#cambia el formato de arr a una matriz de 2 filas y 5 columnas
matriz 
matriz2=matriz.copy() 
matriz2+matriz2#suma de matriz y matriz2
matriz2-matriz2#resta de matriz y matriz2
matriz*matriz2#multiplicacion de matriz y matriz2 
np.matmul(matriz,matriz2)#multiplicacion de matriz y matriz2
matriz@matriz2.T#multiplicacion de matriz y matriz2 .T es para transponer la matriz 