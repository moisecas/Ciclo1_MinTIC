import numpy as np 

arr=np.linspace(1,10,10,dtype='int8') #imprime un array de 10 elementos con valores entre 1 y 10
arr 
indiciescond=arr > 5 #imprime un array de 10 elementos con valores mayores a 5

arr[indiciescond] #imprime los elementos mayores a 5
matriz = arr([[19,  4, 43],
       [ 8, 96, 80],
       [ 6, 99, 35]])

np.where(matriz > 50, 0, 1)
