#funciones definidas arriba y se recomienda que devuelva un dato usando return 
def funcion():
    return "Hola"
   
def funcion2():
   return "Adios"
#puedo acceder a las variables globales definidas antes de invocar la función 


nombre= "Juan"
apellido="Perez"
print(f"El nombre es {nombre} y el apellido es {apellido}")

#se recomienda usar el print afuera de la función 
print(funcion())
print(funcion2())