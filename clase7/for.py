#Listas
#Una lista en Python es una estructura de datos formada por una secuencia ordenada de objetos

lista = [1, 2, 3, 4] #elementos de lista separador por ,
print(lista)
print("tamaño de lista: ", len(lista)) #conocer el numero de elementos que compone la lista diferente a posiciones

mercado=["carne","arroz","huevos","pan"]
print(mercado)

mercados=["carne","arroz","huevos","pan"]
print(mercados)

numeros=[1,2,3,4,5]

listas=mercado+numeros
print(listas) #concatenar 

#Agregar elementos a una lista, append
lista.append([5,6,7,8])
print(lista)

#ciclo for 
list1=[1,2,3,4,5,6,7,8,9, "a"]
for moises in list1: #acá moises itera la lista, la recorre hasta mostrar lo elementos 
  print(moises)

list1=[1,2,3,4,5,6,7,8,9, "a"]
for moises in list1: #acá moises itera la lista, la recorre hasta mostrar lo elementos 
  print(moises,end=" ") #imprimir de forma horizontal 

list1=[1,2,3,4,5,6,7,8,9]
for num in list1: #para num busque los pares 
    if num % 2 == 0: #cuando se divida x 2 de 0 
        print(num)


#agregar elementos 
list1=[1,2,3,4,5,6,7,8,9]
list1.insert(2,"4") #en la posición 2 agrega 4 
print(list1)  
list1.remove(4) #remover posición 4
print(list1)

list=[1,2,3,4,5,6,7,8,9,10] #encontrar los impares 
for num in list:
    if num % 2 != 0:
        print(num)
 

#range, me repite lo mismo la cantidad de veces que quiera 
word = input("introduce una palabra")
for i in range(5): #imprima 5 veces lo contenido en word 
    print(word)

num = input("introduce un numero: ")
for i in range(1000):
    print(num) 

list1 = ["A","B","C","D"]
for num in list1:
    print(num, end=".") #separando las cosas, lo que esta entre "" o entre elemento y elemente va a estar separada por ese elemento

#Tabla de multiplicar del 2 usando for 

for f in range(0,5):
	multiplicacion = 2 * f #hacemos la multiplicación por cada numero que itera en el rango de f hasta llegar a la posición 5
	print(f'2 x {f} = {multiplicacion}') #mostramos el resultado

#Cuantas veces aparece una letra en una frase 
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador = contador + 1
print("La cantidad de letras es: ",contador )


#Escribir un programa que almacene la cadena de caracteres `contraseña` en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password = input('introduce una contraseña')
verify = input('introduce de nuevo')
contador = 0
for i in password:
    if i == verify:
        contador = contador + 1
print ('la contraseña se ha creado exitosamente')