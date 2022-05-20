"""
Función que Solicite el ingreso de una dirección email. Imprimir un mensaje indicando si la 
dirección es válida o no, haciendo uso de una función. Una dirección se considerará 
válida si contiene el símbolo "@".

"""
def validar_email(email):
    if "@" in email:
        return True
    else:
        return False
validar_email(input("Ingrese su email: ")) 

#2
def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c==caracterBuscado:
            return True
    return False

 
direccion=input("Tu email: ")
if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")

#3 
def validador(email):
  cont=0
  email=list(email)
  for i in email:
    if i=="@":
      cont+=1
  if cont==1:
    value="es valido"
  else:
    value="no es valido"
  return value

correo=input("dime el correo")
validador(correo)

"""
Funcion si un numero es primo o no

"""
#1
def es_primo(numero):
    if numero==1:
        return False
    elif numero==2:
        return True
    else:
        for i in range(2,numero):
            if numero%i==0:
                return False
        return True
es_primo(int(input("Ingrese un numero: ")))

#2
from sympy  import * 
def numeroprimo(a):
  primo=isprime(a)
  return primo 
a=input("ingresa un numero entero: ")
print(numeroprimo(a)) 

#3
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

 
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")


"""
Funcion que suma los digitos de un numero hasta que digite un 0 

"""
#1 
numero=int(input("Ingrese un numero: "))

def suma_digitos(numero):
    if numero<10:
        return numero
    else:
        return numero%10+suma_digitos(numero//10)
print(suma_digitos(numero))

#2
def suma(): 
    num=1
    suma=0
    while num!=0:
        num=int(input("Ingrese un numero: "))
        if num !=0:
            for i in num:
                suma+=int(i)
            print(suma)
            suma=0
    return "fin"
suma()

#3
def sumaDigitos(numero_suma):
    suma = 0
    while numero_suma != 0:
        digito = numero_suma % 10
        suma = suma + digito
        numero_suma = numero_suma // 10
    return suma

sumaTotal = 0
numero = int(input("Número a procesar: "))
while numero != 0:
    print("Suma:", sumaDigitos(numero))
    numero = int(input("Número a procesar: "))

print("Fin de la función!")



        



