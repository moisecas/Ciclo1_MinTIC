print ("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre= input("Por favor ingrese su nombre: ").capitalize()
materia= input("Ingrese el nombre de la materia: ").capitalize()
porcentaje=0
nota_acumulada=0
Añadir= "S"
while Añadir=="S":
    nota2= float (input("Ingrese la nota obtenida: "))
    porcentaje2= float (input("Ingrese el porcentaje de la nota: "))
    porcentaje=porcentaje2 + porcentaje
    nota_acumulada= nota_acumulada + (nota2*(porcentaje2/100))
    if porcentaje == 100:
        Añadir= "N"
    elif porcentaje < 100:
            Añadir= str (input("¿Falta añadir notas? S/N "))
    else:

        print("El porcentaje evaluado de una materia no puede ser mayor a 100")
        porcentaje= porcentaje-porcentaje2
        nota_acumulada=nota_acumulada-(nota2*(porcentaje2/100))
        Añadir= "S"
        
    if nota_acumulada >= 3.0:
        aprobacion="aprobado"
    else:
        aprobacion="reprobado"
    
    nota_acumulada=round(nota_acumulada,2)
    
print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobacion}')