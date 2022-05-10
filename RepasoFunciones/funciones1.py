"""
conjunto de instrucciones agregadas por el usuario para la ejecucion del programa 
usamos def para crearla def nombre_funcion(parametros): para crear una funcion 
nombre_funcion es el nombre de la funcion 
Este es un comentario de bloque 
nombre_funcion(parametros) así la invocamos 
"""

#ejemplo1 
print("ejemplo 1") #declaramos una funcion 
def muestra_nombre(nombre): #acá adentro de la función puedo tener toda la lógica que quiera 
    #defino las líneas de código que se van a ejecutar
    print("Hola", nombre) #imprimo el nombre que se le pasa como parámetro
muestra_nombre("moises")#invocamos la función con el parámetro que se le pasa
muestra_nombre("david") 

#ejemplo2 
print("ejemplo 2")

def mostrartunombre(nombre, edad): #dos parametros 
    print(f"Hola: {nombre}") #imprimo el nombre que se le pasa como parámetro
    if edad >= 18: #si la edad es mayor o igual a 18
        print("Eres mayor de edad") #imprimo que eres mayor de edad
nombre=input("Ingrese su nombre: ") #solicitamos el nombre
edad=int(input("Ingrese su edad: ")) #solicitamos la edad uso int para convertirla a entero
mostrartunombre(nombre,edad)#invocamos la función con los parámetros que se le pasa 
