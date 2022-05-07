print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre=input("Por favor ingrese su nombre: ") #solicitamos el nombre del alumno
materia=input("Ingrese el nombre de la materia: ") #solicitamos el nombre de la materia
notas=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas 
promedio=float(input("Ingrese el porcentaje de la nota: "))
validacion=input("¿Falta añadir notas? S/N: ")
contadorpromedio=0
contadornotas=0
if validacion=="S":
    notas=float(input("Ingrese la nota obtenida: ")) #solictamos al usuario las notas 
    promedio=float(input("Ingrese el porcentaje de la nota: "))
    validacion=input("¿Falta añadir notas? S/N: ") 
    contadorpromedio=contadorpromedio+promedio
    for i in range (int(promedio)):

        if i <=100:
            contadorpromedio=contadorpromedio+1
            


            for j in range(int(notas)):
                if j >0:
                    contadornotas=contadornotas+1
                    calcularnota=(contadornotas*(contadorpromedio/100))
                    print("su nota es: ", calcularnota)

elif validacion=="N":
    print("Gracias por su colaboración")



    

    



