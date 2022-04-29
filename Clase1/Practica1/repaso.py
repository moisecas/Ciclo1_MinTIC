#variables

x = 10 #asignar variable
print('el numero es: ', x) #mensaje con x
print(x) #print de x  

#valores asignados por el usuario
nombre = input('escriba un nombre: ') 
print(nombre) 

m=8
print(type(m))#type, para saber el tipo de dato 

#si quiero guardar un numero uso eval
a = eval(input("ingrese un numero"))
print(a) 

#casting, asegurar que recibo el tipo de dato que necesito
b = input('num')
b = float(b) #se sobreescribre la variable, anticipo la variable con el tipo de dato que deseo 
print(type(x),x) 