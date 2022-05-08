print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre=input("Por favor ingrese su nombre: ") #solicitamos el nombre del alumno
materia=input("Ingrese el nombre de la materia: ") #solicitamos el nombre de la materia
validar="S"
nota_acumulada=0
porcentaje=0
porcentajes=0
aprobado=("Aprobado")
repobrado=("Reprobado")
while validar == "S":
    if porcentajes<100:
        nota_acumulada+=float(input("Ingrese la nota obtenida: "))
        porcentaje+=float(input("Ingrese el porcentaje de la nota: "))
        porcentajes+=porcentaje
        nota=nota_acumulada*(porcentajes/100)
        nota_acumulada=nota_acumulada+nota
        if porcentajes==100:
            validar="N"
            break
        if porcentajes>100:
            print("El porcentaje evaluado de una materia no puede ser mayor a 100")
            porcentajes=porcentajes-porcentaje
            nota_acumulada=nota_acumulada-nota
        if porcentajes==100:
            validar="N"
            break
        validar=input("¿Falta añadir notas? S/N: ")
if nota_acumulada>=3:
    print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobado}.")
elif nota_acumulada<3:
    print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {repobrado}.")
