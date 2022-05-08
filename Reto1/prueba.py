print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre=input("Por favor ingrese su nombre: ")
materia=input("Ingrese el nombre de la materia: ") #solicitamos el nombre de la materia
notas=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas
promedio=int(input("Ingrese el porcentaje de la nota: "))
validar=input("¿Falta añadir notas? S/N: ")  
nota=0
sumapromedio=0
notas+=nota
sumapromedio+=promedio

for i in range(0,100):
    if validar=="S":
        notas=float(input("Ingrese la nota obtenida: "))
        promedio=int(input("Ingrese el porcentaje de la nota: "))
        validar=input("¿Falta añadir notas? S/N: ")
    elif validar=="N":
        nota_final=notas*(sumapromedio/100)
    elif sumapromedio>100:
        print("El porcentaje de las notas no puede ser mayor a 100%")
        break
    if nota_final<3:
        print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_final} resultando en no aprobado.")
        break
    else:
        print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_final} resultando en aprobado.")
        break
    