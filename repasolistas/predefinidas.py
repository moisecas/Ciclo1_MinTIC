cantantes=["2pac", "nas", "drake", "2pac"] #declaramos una lista con los cantantes
numeros=[1,2,3,4,5,6,7,8,9,10] #declaramos una lista con los numeros

#ordenar una lista
numeros.sort() #ordena la lista de manera ascendente menor a mayor
print(numeros) #imprimo la lista 

#agregar elemnentos a una lista 
cantantes.append("rescate") #añadimos un elemento a la lista
cantantes.insert(1, "maluma") #añadimos un elemento a la lista en la posicion 1 de la lista 

#eliminar elementos 
cantantes=["2pac", "nas", "drake", "2pac"]
print(cantantes)
cantantes.remove("drake") #eliminamos un elemento de la lista por el nombre
cantantes.pop(1) #eliminamos un elemento de la lista de la posicion 1 de la lista 
print(cantantes)

#dar la vuelta 
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
numeros.reverse() #dar la vuelta a la lista 
print(numeros) 

#contar y buscar elementos 
numeros = [1,2,3,4,5,6,7,8,9,10] 
print(1 in numeros) #imprime si el elemento 1 esta en la lista
print(len(numeros)) #imprime la longitud de la lista 

#cuantas veces aparece un elemento en la lista 
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros.count)

#conseguir indice 
print(numeros.index(1)) #el indice en el cual esta el 1 es 0 

#unir listas 
numeros = [1,2,3,4,5,6,7,8,9,10]
cantantes = ["2pac", "nas", "drake", "2pac"]    
cantantes.extend(numeros) #unimos la lista cantantes con la lista numeros 
print(cantantes) #imprimo la lista 

