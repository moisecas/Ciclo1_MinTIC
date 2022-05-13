estudante1={"cedula": 12345, "nombre": "moises","nota_fundamentos": 4}
estudante2={"cedula": 6789,"nombre": "juan","nota_fundamentos": 3.2}
estudante3={"cedula": 1011,"nombre": "pancho","nota_fundamentos": 5}
estudante4={"cedula": 1213,"nombre": "pp","nota_fundamentos": 5}
estudante5={"cedula": 1415,"nombre": "paco","nota_fundamentos": 3.3}
estudante6={"cedula": 1617,"nombre": "pedro","nota_fundamentos": 4}
estudante7={"cedula": 1819,"nombre": "pancho","nota_fundamentos": 4}

grupo=[estudante1,estudante2,estudante3,estudante4,estudante5,estudante6,estudante7]

# grupo=[{"cedula": 12345, "nombre": "moises","nota_fundamentos": 4},
# {"cedula": 6789,"nombre": "juan","nota_fundamentos": 3.2},
# {"cedula": 1011,"nombre": "pancho","nota_fundamentos": 5},
# {"cedula": 1213,"nombre": "pp","nota_fundamentos": 5},
# {"cedula": 1415,"nombre": "paco","nota_fundamentos": 3.3},
# {"cedula": 1617,"nombre": "pedro","nota_fundamentos": 4},
# {"cedula": 1819,"nombre": "pancho","nota_fundamentos": 4},]


sumapromedios=0 #declaramos una variable para la suma de los promedios
contadorestudiantes=0 #declaramos una variable para el contador de estudiantes 

for sumapromedio in grupo:#recorremos la lista
    sumapromedios+=sumapromedio["nota_fundamentos"]#sumamos los promedios
    contadorestudiantes+=1#sumamos los estudiantes
    promedio=sumapromedios/contadorestudiantes#calculamos el promedio final
    print(promedio)#imprimimos los promedios 

#mostrar los estudiantes con mayor promedio de fundamentos 
for estudiante in grupo:#recorremos la lista
    if estudiante["nota_fundamentos"]==max(grupo, key=lambda x: x["nota_fundamentos"])["nota_fundamentos"]:#condicion para mostrar los estudiantes con mayor promedio
        print(estudiante["cedula"])#imprimimos el nombre del estudiante

#ordenar de mayor a menor por nota de fundamentos 
grupo.sort(key=lambda x: x["nota_fundamentos"], reverse=True)#ordenamos de mayor a menor por nota de fundamentos
print(grupo)#imprimimos la lista ordenada 


for cuadro in grupo:#recorremos la lista
    if cuadro["nota_fundamentos"]==[grupo[0]["cedula"]]:#condicion para mostrar los estudiantes con mayor promedio
        
        cuadro_honor=[(cuadro["cedula"])]#imprimimos el nombre del estudiante
        print(cuadro_honor)#imprimimos la cedula del estudiante en un diccionario  











#promedio sin contador  de estudiantes y sin suma de promedios 
# notas=((grupo[0]['nota_fundamentos']+grupo[1]['nota_fundamentos']+grupo[2]['nota_fundamentos']))
# promedio=notas/3
# print(dict(promedio))


