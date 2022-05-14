estudiante1={"cedula": 10491, "nombre": "moises","nota_fundamentos": 4}
estudiante2={"cedula": 10848,"nombre": "juan","nota_fundamentos": 3.2}
estudiante3={"cedula": 58124,"nombre": "pancho","nota_fundamentos": 5}



grupo=[estudiante1, estudiante2,estudiante3]#declaramos una lista con diccionarios
sumapromedios=0 #declaramos una variable para la suma de los promedios
contadorestudiantes=0 #declaramos una variable para el contador de estudiantes 

#promedio notafundamentos
notas=grupo[0]["nota_fundamentos"]+grupo[1]["nota_fundamentos"]+grupo[2]["nota_fundamentos"]
promedio=notas/3

#ordenar por nota de fundamentos de mayor a menor 
grupo.sort(key=lambda x: x["nota_fundamentos"], reverse=True)
cuadro_honor=grupo 
#print(cuadro_honor)
print(promedio,cuadro_honor)


# for sumapromedio in grupo:#recorremos la lista
#     sumapromedios+=sumapromedio["nota_fundamentos"]#sumamos los promedios
#     contadorestudiantes+=1#sumamos los estudiantes
#     promedio=sumapromedios/contadorestudiantes#calculamos el promedio final
    

# #mostrar los estudiantes con mayor promedio de fundamentos 
# for estudiante in grupo:
#     if estudiante["nota_fundamentos"]>promedio:
#         cuadro_honor=(estudiante["cedula"])
# #mostrar en un diccionario promediofinal y estudiantes con mayor nota de fundamentos
# promediofinal=({"promedio":promedio} ["estudiantes":cuadro_honor])