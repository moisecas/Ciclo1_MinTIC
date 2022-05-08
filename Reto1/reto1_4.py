print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")

nombre=input("Por favor ingrese su nombre: ")
materia=input("Ingrese el nombre de la materia: ") #solicitamos el nombre de la materia

notas=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas
promedio=int(input("Ingrese el porcentaje de la nota: "))
validar=input("¿Falta añadir notas? S/N: ") 

sumapromedio=0
sumapromedio=promedio+sumapromedio
nota=0
nota=nota+notas


aprobado=("Aprobado")
noaprobado=("No aprobado")
validar="S"


while sumapromedio<promedio:
    notas=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas
    promedio=int(input("Ingrese el porcentaje de la nota: "))
    validar=input("¿Falta añadir notas? S/N: ") 
    promedio=sumapromedio+sumapromedio
    sumapromedio+=1
    
    if sumapromedio==100 or validar=="N":
        nota_final=nota*(sumapromedio/100) 
        

    if nota_final<3:
        
        print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_final} resultando en no {aprobado}.")  
                                    
    elif nota_final>=3:
        print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_final} resultando en {aprobado}.") 



        



        

    


        