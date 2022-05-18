"""
Funciones: Son bloques de código que se pueden ejecutar de manera repetitiva.
Reciben parámetros y devuelven valores.
Instrucciones agrupadas en una función se llaman bloques de código.
Se crean con la palabra reservada def. 
"""

#Definir una función mostrar nombre
from ast import Lambda


nombre="Juan" #Definir una variable global para que sea accesible en toda la función
def mostrar_nombre(nombre):
    print(f"El nombre es {nombre}")
#invocar la función 
mostrar_nombre(nombre) #nombre es un parámetro de la función

#Parametros por valor y por referencia, parametro valor que paso desde fuera a la función 
def suma(a,b):
    a = a + b
    return a
#invocar la función
a = 10
b = 20
print(f"La suma de {a} y {b} es {suma(a,b)}") #a y b son parámetros de la función 

#función que reciba parametro y nombre
def mostrar_nombre(nombre, edad):
    print(f"El nombre es {nombre}")
    if edad > 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
#invocar la función
nombre=input("ingresa nombre: ")
edad=int(input("ingresa edad: "))
mostrar_nombre(nombre,edad) #nombre y edad son parámetros de la función

#Tablas de multiplicar con función 
def tabla(numero): #numero es un parámetro de la función
    for i in range(1,11): #bucle for para que se repita 10 veces para que se muestre la tabla del 1 al 10 
        print(f"{numero} x {i} = {numero*i}") #multiplicar numero por i
#invocar la función
numero=int(input("ingresa un número: "))
tabla(numero) #numero es un parámetro de la función
#La puedo usar las veces que quiera siempre y cuando la invoque con el mismo nombre de la función 

#todas las tablas de multiplicar 
for numero in range(1,11): #bucle for para que se repita 10 veces para que se muestre la tabla del 1 al 10 
    tabla(numero) #imprime la tabla del 1 al 10 

#Parametros opcionales 
def getempleado(nombre, dni=False): #dni es un parámetro opcional, si no se le pasa un valor, por defecto es False
    print("empleado")
    print(f"nombre: {nombre}")
    if dni != False:
        print(f"dni: {dni}")
#invocar la función
getempleado("Juan", 1234) #nombre y dni son parámetros de la función

#Parametros opcionales y return
#calculadora que devuelve un string con el resultado de la operación 
def calculadora(num1, num2, operacion=False): #operacion es un parámetro opcional, si no se le pasa un valor, por defecto es suma
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        return num1 / num2
    else:
        return "Operación no válida" #rturn es una palabra reservada para devolver un valor similar al print 
#invocar la función
print(calculadora(10,20,"multiplicacion")) #num1 y num2 son parámetros de la función

#otra forma 
def calculadora(num1, num2, operacion=False):
    
       
    suma=num1 + num2
    resta=num1 - num2
    
    multiplicacion=num1 * num2
    division=num1 / num2
    text=""
    if operacion == True:
        text+= "suma: " + str(suma) + "\n"
        text+= "resta: " + str(resta) + "\n"
    else:
        text+= "multiplicacion: " + str(multiplicacion) + "\n"
        text+= "division: " + str(division) + "\n"
    return text #devuelva un string con todas las operaciones
#invocar la función
print(calculadora(10,20)) #num1 y num2 son parámetros de la función, si esta en true solo muestra suma y resta, en false muestra todas las operaciones multiplicacion y division

#Funciones dentro de otras funciones 
def getnombre(nombre):
    texto=f"El nombre es {nombre}"
    return texto
def getedad(edad):
    texto=f"La edad es {edad}"
    return texto
print(getnombre("Juan"), getedad(20)) #nombre y edad son parámetros de la función

def nombreedad(nombre,edad):
    texto=getnombre(nombre) + "\n" + getedad(edad)
    return texto #devuelva un string con el nombre y la edad 
print(nombreedad("Juan",20)) #nombre y edad son parámetros de la función

#funciones lambda o anonimas 
#funciones que no tienen nombre, se crean con la palabra reservada lambda, para tareas sencillas y repetitivas 
Lambda=lambda num1, num2: num1 + num2
print(Lambda(10,20)) #num1 y num2 son parámetros de la función





