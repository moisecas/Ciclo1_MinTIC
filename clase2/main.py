#Segunda semana del ciclo 1 de programación mintic 2022 
print("hola mundo") #palabra reservada print, para mostrar al usuario. "" comillas para un dato de tipo string 
print("otro mensaje")
print('mensaje con comillas simples') #comillas sencillas o dobles, tecnicamente es lo mismo

print(5) #imprimir un numero sin el uso de variables

print("dos") #cadena de texto 
print(2) #numero
print("2" + str(2)) #concatenar y conversion

print(type("2")) #type, saber el tipo de dato que tenemos al lado 
print(type("3.14")) #type float 

#tipos de datos, por consola nos muestra el tipo de dato
print(type(10))
print(type(3.14))
print(type(-8))
print(type(1e3)) 
print(type(True)) 
print(type(False))  

#operaciones matematicas 
print(1 + 2) #sin variables
a = 5 #variable, espacio en memoria para guardar info
b = 2
print(a+b) #con variables

#ejercicio práctico 

print(9 - 3) #resta 
print(6 * 3) #multiplicación 
print(15 / 3) #da un resultado float 
print(int(15 / 3)) #de esta forma, nos da un float sin la conversión con el int

print(int(3.4)) #imprime parte entera, output 3 por consola 
print(7 % 2) #residuo de algo 
print(7**3) #potencia, 7 elevado a la 3

#ejercicio de tipo de datos 
print(type("i_am_an_integer"))
print(type(3.54))
print(type(7 // 8))
print(type(1))
print(type("hola" + "adiós"))  
print(type(4e4))
print(type(12 / 3))

#operaciones
print((3*2)+1)

#9 elevado a la 3
print(9**3)

#parte entera y residuo 26 entre 4 
print("la parte entera es: ", int(26/4)) 
print("el residuo es: ", 26%4) 

#calcule el cuadrado, cubo, el doble, triple
num = 2 
print("el cuadrado es: ",num**2)
print("el cubo es: ",num**3)
print("el doble es: ",num*2)
print("el triple es: ",num*3) 


