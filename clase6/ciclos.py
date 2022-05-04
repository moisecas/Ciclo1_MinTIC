#ciclo while, contador y aumantador, contador numero de veces 
i=0 #contador inicia en 0 
while i <3: #mientras sea menor a 3 haga 
  print (i)
  i=i+1

#
i=0
suma=0
while i<10:
  print(i)
  suma=suma+i
  i=i+1 #va aumentando de a 1 en la suma
print(suma)

#
num=int(input("escrib un numero"))
while num < 0:
  print("numero negativo, intente de nuevo")#lo solicita nuevamente hasta que escriba un num positivo
  num=int(input("escrib un numero"))
print("gracias por esribir")#al hacer lo que el codigo me pide se sale del ciclo y muestra mensaje 

#numeros del o al 20 pero de dos en dos 
i=0 #contador inicia en 0 
while i <=20: #mientras sea menor a 3 haga 
  print(i)
  i=i+2 

#imprimir 5 veces el nombre
nombre=str(input("ingresa el nombre: "))
i=0 #contador
while i<=4: #va hasta 4 debido a que inicia en 0 para que imprima 5 veces, si lo llevo hasta 5 me imprime 6 veces, debo tener en cuenta donde inicia el contador
  print(nombre)
  i=i+1 #corte del bucle hasta

#otra opción 
#imprimir 5 veces el nombre
nombre=str(input("ingresa el nombre: "))
i=0 #contador
while i<5: #va hasta menor que 5 
  print(nombre)
  i=i+1 #corte del bucle hasta

#tabla de multiplicar del 3 
i = 1
x = 0
while i <= 10:
  print(f"3 *{i}={3*i}")
  x = x + (3*i)
  i = i + 1
 
print(x) 

#los multiplos de 3 comprendidos en 3 y 15 
i = 3 #contador iniciando en 3
while i <= 15: #mientras i sea menor o igual a 15 haga
  print ("este es un multiplo de 3: ",i) #muestra i
  i = i + 3 #hasta que llegue a 15, aumentamos de 3 en 3 


#Para mañana verenos break  