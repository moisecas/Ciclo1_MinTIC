n1=float(input("intro numero 1: "))

n2=float(input("intro numero 2: "))#captura de datos con input 

suma=n1+n2 

print("la suma es: ", suma)

#calcule el area de un triangulo
print("area de un triangulo")
b=float(input("escriba la base: "))
h=float(input("escriba la altura: "))
area=(b*h)/2
print("el area es: ", area) 

#salario de una persona y descuente el 20%
print("salario -20%")
salario=int(input("digite el salario: "))
descuento=float(input("escriba el descuento, por ejemplo si es del 20% escribe 0.2 y así  : "))
salariototal=salario - (salario*descuento)  
print("el salario es: ", salariototal) 

#calcular la nota final que cada corte tiene un valor del 30%,30% y 40%
print("promedio de notas")
nota1=3
nota2=2
nota3=5
notafinal=(nota1+nota2+nota3)/3
print("la nota final es: ", notafinal) 

#salario del empleado - descuentos 4% salud 4%pensión 1% riesgos