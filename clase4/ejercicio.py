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
