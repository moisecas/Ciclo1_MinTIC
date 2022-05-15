estudiante1={"cedula": 10491, "nombre": "moises","nota_fundamentos": 4}
estudiante2={"cedula": 10848,"nombre": "juan","nota_fundamentos": 3.2}
estudiante3={"cedula": 58124,"nombre": "pancho","nota_fundamentos": 5}
estudiante4={"cedula": 24993,"nombre": "pp","nota_fundamentos": 5}
estudiante5={"cedula": 10959,"nombre": "paco","nota_fundamentos": 3.3}
estudiante6={"cedula": 12495,"nombre": "pedro","nota_fundamentos": 4}
estudiante7={"cedula": 10952,"nombre": "pancho","nota_fundamentos": 4}

grupo=[estudiante1, estudiante2,estudiante3,estudiante4,estudiante5,estudiante6
,estudiante7]#declaramos una lista con diccionarios
#tamaño de grupo
tamaño=len(grupo)
sumapromedios=0 #declaramos una variable para la suma de los promedios

#sumamos los promedios 
for sumapromedio in grupo:
    sumapromedios+=sumapromedio["nota_fundamentos"] 
promedio = sumapromedios/tamaño

listanotas=grupo["nota_fundamentos"] #declaramos una lista con las notas de fundamentos
#ordenar de mayor a menor lista de notas
listanotas.sort(reverse=True) 
#extraer los primeros 3 elementos de la lista de notas 
primeros3=listanotas[:3]

#mayor nota de fundamentos 
mayor=max(grupo, key=lambda x: x["nota_fundamentos"])

#agregar a una lista los estudiantes con mayor nota de fundamentos 
for estudiante in grupo:
    if estudiante["nota_fundamentos"]==mayor["nota_fundamentos"]:
        #crear una lista con los estudiantes con mayor nota de fundamentos
        listaestudiantes=[]
