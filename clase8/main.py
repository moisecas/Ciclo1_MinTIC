# Metodo Update
dict_ports1 ={22:"SSH",80:"Http"}
dict_ports2 ={53:"DNS",443:"https"}
print(dict_ports1)
dict_ports1.update(dict_ports2)
print(dict_ports1) 


dict_ports1 ={22:"SSH",80:"Http"}
dict_ports2 ={53:"DNS",443:"https"}
dict_ports3 ={25:"JKL",90:"htt"}
print(dict_ports1)
dict_ports1.update(dict_ports2)
print(dict_ports1)
dict_ports1.update(dict_ports3)
print(dict_ports1)

#Imprimir diccionarios seguidos
#Se usa diccionario.update(Nombre del diccionario)

#{22:'SSH', 23:'Telnet',80:'HTTP',3306:'MySQL'}

#x ={} #Esto es un diccionario vacio

puertos = {22:'SSH',23:'Telnet',80:'HTTP',3306:'MySQL'}
print (puertos)
# Metodo Update
dict_ports1 ={22:"SSH",80:"Http"}
dict_ports2 ={53:"DNS",443:"https"}
dict_ports3 ={54:"SSS",444:"hSS"}
print(dict_ports1)
x = {**dict_ports1, **dict_ports2, **dict_ports3}   #Concatenar diccionarios
print(x)

#acceder al valor de un item con la clave dada // sino existe se genera error
puertos ={22:"SSH",23:"Telnet",80:"HTTP",3306:"MySQL"}
protocolo =puertos[22]
print(protocolo)
#puertos[443]


# eliminando elementos del diccionario con el comando del
puertos ={22:"SSH",23:"Telnet",80:"HTTP",3306:"MySQL"}
print(puertos)
del puertos[23] #elimino la clave y valor 
print(puertos)


#Es posible determinar si en un diccionario existe un item que tenga asociada una clave
puertos ={80:"HTTP",23:"SMTP",443:"HTTPS"}
if 80 in puertos:
  print("yes")
if 110 not in puertos:
    print("no")
else:
  print("yes")


#Iterando un Diccionario usando ciclo for para obtener las claves
dict_ports ={22:"SSH",23:"telnet",80:"Http"}
for key in dict_ports:
  print(key)

#Metodo Len para un Diccionario
puertos ={80:"HTTP",23:"SMTP",443:"HTTPS"}
print(len(puertos))

# Obteniendo valores get
# Se puede obtener el valor de un item a partir de la llave con el metodo get.
# Se puede decir que retornar sino se encuentra un item con dicha clave

dict1 ={"a":1,"b":2,"c":3}
print(dict1.get("a"))
print(dict1.get("d", "clavenoencontrada."))

# Maximo y Minimo de un Diccionario
#Metodo Max/Min obtiene la maxima y minima clave de los items de un diccionario
puertos ={80:"HTTP",23:"SMTP",443:"HTTPS"}
print(max(puertos))
print(min(puertos)) 

#Listas de las claves de un diccionario
#Metodo Key : obtiene una lista con todas las claves
#Metodo Values: Obtiene una lista con todos los valores
dict1 ={"a":1,"b":2,"c":3}
print(list(dict1.keys()))
print(list(dict1.values()))

# Metodo dict
#Permite convertir listas de listas  y listas de tuplas a diccionarios

puertos =[[80,"http"],[20,"ftp"],[23,"telnet"]]
d_port =dict(puertos)
print(d_port)
puertos =[(20,"ftp"),(80,"http"),(23,"telnet")]
d_port =dict(puertos)
print(d_port)

#copiar diccionario
port ={80:"HTTP",23:"SMTP",443:"HTTPS"}
copy_port =port.copy()
false_copy =port
print(port)
print(copy_port)
print(false_copy)

#Desarrollar un algoritmo que verifique si todas las clave:valor de un diccionario se encuentran en otro diccionario.
persona={1:"bucaramanga", 2:"trabajador", 3:"ingeniero de sistemas"}
persona2={1:"bucaramanga", 2:"trabajador", 3:"ingeniero de sistemas"}
if persona2==persona:
  print("coinciden las personas")
else:
    print("las personas son diferentes")

persona={"ciudad":"bucaramanga", "dedica":"trabajador", "profesion":"ingeniero de sistemas"}
persona2={1:"bucaramanga", 2:"trabajador", 3:"ingeniero de sistemas"}
if persona2==persona:
  print("coinciden las personas")
else:
    print("las personas son diferentes")

persona={"ciudad":"bucaramanga", "dedica":"trabajador", "profesion":"ingeniero de sistemas"}
persona2={1:"bucaramanga", 2:"trabajador", 3:"ingeniero de sistemas"}
if persona2!=persona:
  print("las personas son diferentes")
else:
    print("coinciden las personas")

