from ast import For


def calcularnota(n1,n2,n3,p1,p2,p3): #definimos la función con los parametros que va a recibir
    return (n1*p1)+(n2*p2)+(n3*p3)

nombre=input("escriba el nombre del alumno: ") #solicitamos el nombre del alumno
n1=float(input("escriba la nota 1: ")) #solictamos al usuario las notas 
p1=float(input("escriba promedio nota 1, por ejemplo si es 20%, escribe 0.20: "))
n2=float(input("escriba la nota 2: "))
p2=float(input("escriba promedio nota 2, por ejemplo si es 30%, escribe 0.30: "))
n3=float(input("escriba la nota 3: "))
p3=float(input("escriba promedio nota 3, por ejemplo si es 15%, escribe 0.15: "))
sumapromedio=p1+p2+p3 #sumamos los promedios

notafinal=calcularnota(n1,n2,n3,p1,p2,p3) #invocamos la función con los parametros que le pasamos, recibidos en el input
print("Hola ",nombre,"La nota final es: ", notafinal)#mostramos el resultado al usuario 


