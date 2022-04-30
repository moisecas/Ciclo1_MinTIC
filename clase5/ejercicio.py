#Haga un programa que dados tres números diga cual es el mayor

n1=int(input("escriba el numero 1: "))
n2=int(input("escriba el numero 2: "))
n3=int(input("escriba el numero 3: "))
if n1 > n2 and n1 > n3:
  print("El numero 1 es el mayor es: ", n1)
elif n2 > n1 and n2 > n3:  
  print("El numero 2 es el mayor, es: ", n2)
elif n3 > n1 and n3 > n2:
  print("El numero 3 es el mayor, es: ", n3) 
else:
  print("Los numeros son iguales", n1,n2,n3) 

#Haga un programa que calcule el valor de un computador sabiendo que tienen 
#un precio de venta y se hace un descuento dependiendo de la forma de pago, 
#si es efectivo se le descuenta 30% del valor venta, 
#si es con tarjeta crédito se le descuenta 15% del valor venta y si es con tarjeta debito se le descuenta un 25% del valor venta.

pc=int(input("escriba el valor de la computadora: "))
pago=int(input("escriba 1 si es pago en efectivo o 2 si es pago con tarjeta de credito o 3 si es con tarjeta debito: "))
pago_efectivo=(pc-(pc*0.30))
pago_tarjeta_credito=(pc-(pc*0.15))
pago_tarjeta_debito=(pc-(pc*0.25))
if pago==1:
  print("Gracias por pagar en efectivo, el valor del pc con el 30% de descuento es: ", pago_efectivo)
elif pago ==2:
  print("Gracias por pagar con tarjeta de credito, el valor del pc con el 15% de descuento es: ", pago_tarjeta_credito)
else:
  print("Gracias por pagar con tarjeta debito, el valor del pc con el 25% de descuento es: ", pago_tarjeta_debito) 


#Haga un programa que calcule el salario neto de un empleado sabiendo que el salario básico de él se calcula de acuerdo 
#con número de horas trabajadas y la hora tiene un valor especifico, además si ese salario es menor que dos salarios 
#mínimos legales vigente (smlv) se le paga un subsidio de transporte equivalente a 55000.  (el smlv=565000).

horas=int(input("Horas trabajadas: ")) 
valor_hora=int(input("Acá va el valor de la hora: "))
transporte=55000
salario_neto=horas*valor_hora 
if salario_neto<1130000:
  print("Su salario requiere subsisio de transporte y el total es de: ", salario_neto+transporte) 
else:
  print("su salario neto es de: ", salario_neto)