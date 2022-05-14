estudiante1={"cedula": 10491, "nombre": "moises","nota_fundamentos": 4}
estudiante2={"cedula": 10848,"nombre": "juan","nota_fundamentos": 3.2}
estudiante3={"cedula": 58124,"nombre": "pancho","nota_fundamentos": 5}
estudiante4={"cedula": 24993,"nombre": "pp","nota_fundamentos": 5}
estudiante5={"cedula": 10959,"nombre": "paco","nota_fundamentos": 3.3}
estudiante6={"cedula": 12495,"nombre": "pedro","nota_fundamentos": 4}
estudiante7={"cedula": 10952,"nombre": "pancho","nota_fundamentos": 4}


grupo=[estudiante1, estudiante2,estudiante3,estudiante4,estudiante5,estudiante6,estudiante7]#declaramos una lista con diccionarios
sumapromedios=0 #declaramos una variable para la suma de los promedios
contadorestudiantes=0 #declaramos una variable para el contador de estudiantes 

for sumapromedio in grupo:#recorremos la lista
    sumapromedios+=sumapromedio["nota_fundamentos"]#sumamos los promedios
    contadorestudiantes+=1#sumamos los estudiantes
    promediofinal=sumapromedios/contadorestudiantes#calculamos el promedio final
    print(promediofinal)#imprimimos los promedios 

#mostrar los estudiantes con mayor promedio de fundamentos 
for estudiante in grupo:
    if estudiante["nota_fundamentos"]>promediofinal:
        print(estudiante["cedula"],estudiante["nombre"],estudiante["nota_fundamentos"])
#mostrar en un diccionario promediofinal y estudiantes con mayor nota de fundamentos
promediofinal={"promedio":promediofinal,"estudiantes":contadorestudiantes}

    #     for estudiante in grupo:#recorremos la lista
    # if estudiante["nota_fundamentos"]==max(grupo, key=lambda x: x["nota_fundamentos"])["nota_fundamentos"]:#condicion para mostrar los estudiantes con mayor promedio
        
    #     grupo(estudiante["cedula"])#imprimimos el nombre del estudiante
    #     print(grupo(estudiante["cedula"]))#imprimimos el nombre del estudiante

         
      

        