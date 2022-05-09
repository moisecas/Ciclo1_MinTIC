print ("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre= input("Por favor ingrese su nombre: ").capitalize()
materia= input("Ingrese el nombre de la materia: ").capitalize()
porcentaje=0
nota_suma=0
validar= "S"
while validar=="S":
    nota2= float (input("Ingrese la nota obtenida: "))
    porcentaje2= float (input("Ingrese el porcentaje de la nota: "))
    porcentaje=porcentaje2 + porcentaje
    nota_suma= nota_suma + (nota2*(porcentaje2/100))
    if porcentaje == 100:
        validar= "N"
    elif porcentaje < 100:
            validar= str (input("¿Falta añadir notas? S/N "))
    else:

        print("El porcentaje evaluado de una materia no puede ser mayor a 100")
        porcentaje= porcentaje-porcentaje2
        nota_suma=nota_suma-(nota2*(porcentaje2/100))
        validar= "S"
        
    if nota_suma >= 3.0:
        aprobacion="aprobado"
    else:
        aprobacion="reprobado"
    
    nota_suma=round(nota_suma,2)
    
print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_suma} resultando en {aprobacion}')