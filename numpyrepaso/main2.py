import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])
arr 
arr.dtype #imprimo el tipo de dato de arr 

arr=np.array([1,2,3],dtype="float64") 
arr.dtype #imprimo el tipo de dato de arr 

arr=arr.astype(np.float64) #convertimos el array a un tipo de dato diferente 
arr=arr.astype(np.string) #convertimos el array a un tipo de dato string 
arr 

arr2=np.array(["1","2","3","4","5","6","7","8","9","10"])
arr2=arr2.astype(np.int64) #convertimos el array a un tipo de dato int
arr 

#el array de numpy solo puede manejar un único tipo de dato 
