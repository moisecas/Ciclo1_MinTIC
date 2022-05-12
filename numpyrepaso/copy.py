#copy para modificar elementos de un array o una matriz o un tensor copia del original, se recomienda usarlo para hacer operaciones sin modificar el original
import numpy as np 

arr=np.arrange(1,11) #declaramos un array de números del 1 al 10
arr 
parte_arr=arr[0:6]
parte_arr[:]=0 #asignamos 0 a todos los elementos del array
parte_arr 
arr_copy=arr.copy() #copiamos el array
arr_copy[:]=0 #asignamos 0 a todos los elementos del array

