"""
Variable global y local 
global y local son dos palabras reservadas que se usan para definir variables globales y locales.
Variable global: se define fuera de una función y se puede usar en cualquier parte del programa.
Variable local: se define dentro de una función y se puede usar dentro de la función.
"""
#Definir una variable global
print("fuera de la función")
nombre="Juan" #Definir una variable global para que sea accesible en toda la función
print("soy varaible global", nombre)
def mostrar_nombre():
    nombre="Pedro" #Definir una variable local para que sea accesible en la función
    print("adentro de la función")
    print(f"El nombre es {nombre} y soy variable local")
    global website #Definir una variable global para que sea accesible en la función
    website="https://www.google.com"
    print(f"El website es {website} y etoy adentro de la función")
#invocar la función
mostrar_nombre()
print("pero también estoy afuera", website)

