estudiante1={"cedula": 1095810491, "nombre": "moises","nota_fundamentos": 4}
estudiante2={"cedula": 1084810493,"nombre": "juan","nota_fundamentos": 3.2}
estudiante3={"cedula": 1095812499,"nombre": "pancho","nota_fundamentos": 5}

grupo=[estudiante1, estudiante2,estudiante3]#declaramos una lista con diccionarios

notas=((grupo[0]['nota_fundamentos']+grupo[1]['nota_fundamentos']+grupo[2]['nota_fundamentos']))
promedio=notas/3
print(promedio)

