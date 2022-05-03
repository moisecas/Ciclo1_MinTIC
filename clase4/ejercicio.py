gi=int(input("Digite el peso de Gi: "))
ale=int(input("Digite el peso de Ale: "))

peso_ale=int((gi-4)*2)
print("el peso de Ale es: ", peso_ale) 
peso_nico=gi+peso_ale*5 
if peso_nico <=20:
  print("Nico, esta en etapa 1")
elif peso_nico >20 and peso_nico<=40:
  print("Nico,esta en etapa 2")
elif peso_nico >=41 and peso_nico<=80:
  print("Nico,esta en etapa 3")
else:
  print("Nico,esta en tapa 4") 
  print("el peso de nico es: ", peso_nico) 

#solución dos
ale=int(input("Digite el peso de Ale: "))
gil=(ale*2)+4
nico=int((ale+gil)/5)

print("El peso de Ale es: ", ale, "El peso de Gil es: ", gil, "el peso de Nico es: ", nico)

if nico>=20:
  print("Nico se encuentra en etapa 1 y su peso es de: ", nico)
elif nico >=21 and nico <= 40:
  print("Nico se encuentra en etapa 2 y su peso es de: ", nico)
else:
  print("Nico se encuentra en etapa 3 y su peso es de: ", nico)   
