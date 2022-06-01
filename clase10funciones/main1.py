"""
función resta multiplicación división
"""
def resta_multiplicacion_div(num1, num2):
    
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    return resta, multiplicacion, division
print(resta_multiplicacion_div(10, 5)) #muestra la resta, la multiplicacion y la division de los numeros 10 y 5 


"""
promedio de 3 notas ingresadas por el usuario 
"""
nombre=input("Ingrese su nombre: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
def promedio_notas(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio
print ('Hola ' + nombre + ' tu promedio es: ' + str(promedio_notas(nota1, nota2, nota3))) #muestra el promedio de las 3 notas ingresadas por el usuario
