import numpy as np 

scalar = np.arrray(42) 
print(scalar)
scalar.ndim #imprimo el número de dimensiones de scalar

vector = np.arrray([1,2,3,4,5,6,7,8,9,10]) 
print(vector)
vector.ndim #imprimo el número de dimensiones de vector 

matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
matriz.ndim #imprimo el número de dimensiones de matriz 

tensor=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]]) #declaramos un tensor de 2 dimensiones 
print(tensor)
tensor.ndim #imprimo el número de dimensiones de tensor 

#agregar o elmininar dimensiones
vector2=np.array([1,2,3,4,5,6,7,8,9,10], ndim=10) #vector2 es un array de 10 dimensiones 
print(vector2)
vector2.ndim #imprimo el número de dimensiones de vector2 

objeto=np.expand_dims(np.array([1,2,3]), axis=0) #agrega una dimension a vector, axis=0 es la primera dimension
print(objeto)
objeto.ndim #imprimo el número de dimensiones de objeto 

#eliminar dimensiones 
vector3=np.array([1,2,3,4,5,6,7,8,9,10]) #vector3 es un array de 1 dimension 
print(vector3, vector3.ndim)
vector3=np.squeeze(vector3) #elimina la dimension 0 de vector3
