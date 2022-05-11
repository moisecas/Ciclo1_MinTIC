#arrays o arreglos en python son una colección de datos que se puede manipular como una lista

from operator import index


pelicula= "batman" #declaramos una variable con la pelicula
peliculas=["batman", "superman", "batman vs superman", "batman forever"] #declaramos una lista con las peliculas
#cada elemento de la lista es una pelicula tiene una posición en la lista

cantantes = list("2pac", "nas", "drake", "2pac") #declaramos una lista con los cantantes
print(cantantes) #imprimo la lista 

years=list(range(2020,2050)) #declaramos una lista con los años 
print(years) #imprimo la lista 

variada=["moises", 30, True, "batman", "superman", "batman vs superman", "batman forever"] #declaramos una lista con varias cosas   
print(variada) #imprimo la lista 

#indices en listas 
#para acceder a un elemento de la lista, se declara un 
print(peliculas[0]) #imprimo la pelicula en la posición 0 de la lista peliculas
print(peliculas[1]) #imprimo la pelicula en la posición 1 de la lista peliculas
print(peliculas[-2]) #imprimo la pelicula en la posición -2 de la lista peliculas 
print(cantantes[1:3]) #imprimo los cantantes en la posición 1 y 3 de la lista cantantes 
print(peliculas[:3]) #imprimo las peliculas en la posición 0, 1 y 2 de la lista peliculas
print(peliculas[2:]) #imprimo las peliculas en la posición 2 y siguientes de la lista peliculas

#actualizar 
peliculas=["batman", "superman", "batman vs superman", "batman forever"]
print(peliculas)
peliculas[1]="terminator" #actualizo la pelicula en la posición 1 de la lista peliculas 
print(peliculas)

#añadir elementos a lista 
cantantes.append("2pac") #añado el cantante 2pac a la lista cantantes
print(cantantes) 

#recorrer listas 
print("Listado de peliculas")
nuva_pelicula=""
peliculas2=["batman", "superman", "batman vs superman", "batman forever"]
while nuva_pelicula!="salir": #mientras la pelicula no sea salir
    nuva_pelicula=input("¿Que pelicula quieres añadir?: ") #pido una pelicula
    if nuva_pelicula!="salir": #si la pelicula no es salir

        peliculas2.append(nuva_pelicula) #añado la pelicula a la lista peliculas



for peliculas in peliculas2: #recorro la lista peliculas2 iterando sobre ella 
    print(f"{peliculas2.index(peliculas)}.{peliculas}") #imprimo cada pelicula de la lista peliculas2 y su indice 

#Listas multidemensionales 
print("listado de contactos")
contactos=[
    ["moises", "moises@.com"],
    ["juan", "juan@.com"],
    ["pedro", "pedro@.com"]
]
for contacto in contactos: #recorro la lista contactos iterando sobre ella
    print(f"{contacto[0]} tiene el correo {contacto[1]}") #imprimo cada contacto de la lista contactos y su correo
print(contactos) #imprimo la lista contactos 

   