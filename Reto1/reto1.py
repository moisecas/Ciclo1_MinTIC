
print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre=input("Por favor ingrese su nombre: ") #solicitamos el nombre del alumno
materia1=input("Ingrese el nombre de la materia: ") #solicitamos el nombre de la materia
n1=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas 
p1=float(input("Ingrese el porcentaje de la nota: "))#solicitamos al usuario el promedio de la nota 1
validacion1=input("¿Falta añadir notas? S/N: ") #solicitamos al usuario si desea ingresar otra nota
if validacion1=="S": #si el usuario ingresa S, seguira el ciclo 
    materia2=input("Ingrese el nombre de la materia: ")
    n2=float(input("Ingrese la nota obtenida: "))
    p2=float(input("Ingrese el porcentaje de la nota: "))
    validacion2=input("¿Falta añadir notas? S/N: ")
elif validacion1=="N": #si el usuario ingresa N, se rompe el ciclo
    n2=float(input("Ingrese la nota obtenida: "))
    p2=float(input("Ingrese el porcentaje de la nota: "))
    validacion2=input("¿Falta añadir notas? S/N: ")   
    if validacion2=="S":
        materia3=input("Ingrese el nombre de la materia: ")
        n3=float(input("Ingrese la nota obtenida: "))
        p3=float(input("Ingrese el porcentaje de la nota: "))
        validacion3=input("¿Falta añadir notas? S/N: ")
    elif validacion2=="N":
        n3=float(input("Ingrese la nota obtenida: "))
        p3=float(input("Ingrese el porcentaje de la nota: "))
        validacion3=input("¿Falta añadir notas? S/N: ")
        if validacion3=="S":
            materia4=input("Ingrese el nombre de la materia: ")
            n4=float(input("Ingrese la nota obtenida: "))
            p4=float(input("Ingrese el porcentaje de la nota: "))
            
sumapromedio=p1+p2+p3+p4 #sumamos los promedios

while sumapromedio == 100: #si la suma de los promedios es igual a 100, seguira el ciclo
    calcularnota=(n1*(p1/100))+(n2*(p2/100))+(n3*(p3/100)+n4*(p4/100)) #calculamos la nota final
    print("Hola ",nombre,"La nota final es: ", calcularnota)#mostramos el resultado al usuario 
    break #rompe el ciclo

while sumapromedio != 100: #si la suma de los promedios no es 100, seguira el ciclo 
    print("La suma de los porcentajes no es 100")
    materia1=input("Ingrese el nombre de la materia: ") #solicitamos el nombre de la materia
    n1=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas 
    p1=float(input("Ingrese el porcentaje de la nota: "))#solicitamos al usuario el promedio de la nota 1
    validacion1=input("¿Falta añadir notas? S/N: ") #solicitamos al usuario si desea ingresar otra nota
    if validacion1=="S": #si el usuario ingresa S, seguira el ciclo 
        materia2=input("Ingrese el nombre de la materia: ")
        n2=float(input("Ingrese la nota obtenida: "))
        p2=float(input("Ingrese el porcentaje de la nota: "))
        validacion2=input("¿Falta añadir notas? S/N: ")
    if validacion2=="S":
        materia3=input("Ingrese el nombre de la materia: ")
        n3=float(input("Ingrese la nota obtenida: "))
        p3=float(input("Ingrese el porcentaje de la nota: "))
        validacion3=input("¿Falta añadir notas? S/N: ")
        if validacion3=="S":
            materia4=input("Ingrese el nombre de la materia: ")
            n4=float(input("Ingrese la nota obtenida: "))
            p4=float(input("Ingrese el porcentaje de la nota: "))
    sumapromedio=p1+p2+p3+p4


    calcularnota=(n1*(p1/100))+(n2*(p2/100))+(n3*(p3/100)+n4*(p4/100)) #calculamos la nota final


    print("Hola ",nombre,"La nota final es: ", calcularnota)#mostramos el resultado al usuario 


