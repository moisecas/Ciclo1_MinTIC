print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre=input("Por favor ingrese su nombre: ")
materia=input("Ingrese el nombre de la materia: ") #solicitamos el nombre de la materia
sumapromedio=0
nota=0
aprobado=("Aprobado")
noaprobado=("No aprobado")
validar="S"
contador=0
contador2=0


while contador < 100 and validar=="S":
    notas=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas
    promedio=int(input("Ingrese el porcentaje de la nota: "))
    validar=input("¿Falta añadir notas? S/N: ")     
    sumapromedio=promedio+contador
    nota=contador2+notas
    
    
    
    if sumapromedio==100 or validar=="N":
        nota_final=nota*(sumapromedio/100)
        if nota_final<3:
        
          print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_final} resultando en no {aprobado}.")  
                  
                                    
    elif nota_final>=3:
        print(f"El Estudiante {nombre} cursó la materia {materia} y obtuvo {nota_final} resultando en {aprobado}.") 


        



        

    


        