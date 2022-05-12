import numpy as np 

np.arrange(0,10) # array de 0 a 10 
np.arange(0,10,2) # array de 0 a 10 con paso de 2
np.zeros(10) # array de 10 zeros 
np.ones(10) # array de 10 unos 
np.linspace(0,10,10) # array de 10 valores entre 0 y 10 y la cantidad de datos que quiero ver, array de 0 a 10 con 10 valores
np.linspace(0,10,10).reshape(5,2) # array de 10 valores entre 0 y 10 con paso de 2 y 5 filas y 2 columnas 
np.eye(10) # matriz identidad de 10x10 
np.random.rand(10) # array de 10 valores aleatorios entre 0 y 1 
np.random.randint(0,10,10) # array de 10 valores aleatorios entre 0 y 10
np.random.randint(0,10,(5,5)) # array de 5x5 valores aleatorios entre 0 y 10
np.random.randint(1,15) # valor aleatorio entre 1 y 15 

#shape me permite obtener la cantidad de filas y columnas de una matriz
#reshape me permite cambiar la cantidad de filas y columnas de una matriz 

array3=np.random.randint(1,15).shape # obtengo la cantidad de filas y columnas de una matriz
array3.reshape(3,3) # cambio la cantidad de filas y columnas de una matriz
#debe considerar el tamaño de la matriz para que funcione correctamente no puede ser mayor a la matriz original 
