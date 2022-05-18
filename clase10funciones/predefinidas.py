from typing import TextIO


nombre="moises castro"
#funciones generales
print(nombre)
print(type(nombre)) #type es una función predefinida que devuelve el tipo de dato de una variable
print(nombre.upper()) #upper es una función predefinida que convierte todo a mayúsculas
print(nombre.lower()) #lower es una función predefinida que convierte todo a minúsculas
print(nombre.split()) #split es una función predefinida que convierte una cadena en una lista
print(nombre.split(" ")) #split es una función predefinida que convierte una cadena en una lista

#detectar el tipado 
comprobar=isinstance(nombre,str) #isinstance es una función predefinida que devuelve True si la variable es del tipo especificado
if comprobar:
    print("es un string")
else:
    print("no es un string")
if not isinstance(nombre,float): #not es un operador que devuelve True si la variable es distinta de del tipo especificado
    print("no es un string")

#Limpiar espacios de uns string 
nombre="   moises castro   "
print(nombre.strip()) #strip es una función predefinida que elimina los espacios en blanco de una cadena

#eliminar variables 
year=2020
print(year)
del year #elimina la variable year

#comprobar variable vácia 
text="hola mundo"
if len(text) <= 0:
    print("la variable está vacía")
else:
    print("la variable no está vacía: ", len(text))  #len es una función predefinida que devuelve la longitud de una cadena

#encontrar caracteres de un string
frase="la vida en familia es mejor, Dios es bueno" 
print("Esta en la posición: ", frase.find("Dios")) #find es una función predefinida que devuelve la posición de un caracter en una cadena

#reemplazar palabras en un string 
frase="la vida en familia es mejor, Dios es bueno"
frase2=frase.replace("Dios","Jesus") #replace es una función predefinida que reemplaza una palabra por otra en una cadena, en este caso reemplaza Dios por Jesus. 
print(frase2)

