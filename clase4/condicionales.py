#Condicionales 
print("Segunda semana ciclo 1 python")

x = int(input("¿Cuál es el primer número?")) #Preguntamos al usuario qué número quiere
y = int(input("¿Cuál es el segundo número?"))

if x>y:
  print('El primer número es mayor.')
elif x<y:
  print('El primer número es menor.') #para mas de dos condiciones se usa el elif 
else:
  print('Es el mismo número.') #si cierra el ciclo, siempre que haya un if debe haber un else, un si no, para cortar el ciclo. 


#Si es mayor de edad o no 
edad = int(input("escriba su edad"))
if edad>=18:
  print("es mayor de edad")
else:
    print("es menor de edad")

#promedio de notas para 3 notas, si el promedio es menor a 3, el estudiante perdio la asignatura
nota1=float(input("escriba primera nota: "))
nota2=float(input("escriba segunda nota: "))
nota3=float(input("escriba tercera nota: "))
promedio=float((nota1+nota2+nota3)/3)
if promedio <3:
  print("perdio la materia, repita la asignatura")
else:
  print("ha pasado la asignatura, felicitaciones")

#un programa que dado un número, si este es mayor que 5 calcule el cubo, en caso contrario calcule el cuadrado e imprimir el resultado.
numero=float(input("escribe el numero a calcular: "))
if numero >5:
  print("el cubo de ese numero es: ", numero**3)
else:
  print("el cuadrado de ese numero es: ", numero**2)

#otra solución 
a = float(input("escriba un numero"))
b = a**3
c = a**2

if a>5:
  print(b)
else:
  print(c) 

#Haga un programa que calcule el promedio de notas para 3 notas.  
#Si el promedio es menor a tres aparezca un mensaje el estudiante perdió, 
#si el promedio es mayor o igual a tres y menor que cuatro aparezca  un mensaje bien es estudiante gano, 
#si el promedio es mayor o igual a cuatro el mensaje diga excelente promedio superior.

nota1=float(input("escriba primera nota: "))
nota2=float(input("escriba segunda nota: "))
nota3=float(input("escriba tercera nota: "))
promedio=float((nota1+nota2+nota3)/3)
if promedio <3:
  print("perdio la materia, repita la asignatura")
elif promedio >=3 and promedio<4:
  print("bien es estudiante gano") 
else: 
  print("excelente promedio superior")



 











