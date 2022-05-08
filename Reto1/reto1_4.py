print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre=input("Por favor ingrese su nombre: ") #solicitamos el nombre del alumno
materia=input("Ingrese el nombre de la materia: ") #solicitamos el nombre de la materia
notas=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas
promedio=(input("Ingrese el porcentaje de la nota: ")) 
notas=0
sumapromedio=0

while notas >=0:
    notas=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas
    promedio=(input("Ingrese el porcentaje de la nota: "))
    notas=notas+1
    sumapromedio+=promedio

    if sumapromedio>=100:
        print("El porcentaje evaluado de una materia no puede ser mayor a 100") 
        promedio=float(input("Ingrese el porcentaje de la nota: "))
        validar=input("¿Falta añadir notas? S/N: ")
        if validar == "N" and sumapromedio=="100":
            nota_final=notas*(sumapromedio/100)
        if validar == "N" and sumapromedio<"100":
            promedio=float(input("Ingrese el porcentaje de la nota: "))

    
            if nota_final<3:
                print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_final} resultando en no aprobado.")

    
        else:
            print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_final} resultando en aprobado.") 

        