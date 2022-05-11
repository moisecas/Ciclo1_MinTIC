#almacena, indices alfanumericos, como un objeto json, clave valor 

personas={"moises": "moises@.com", "juan": "juan@.com", "pedro": "perdro@.com"} #declaramos un diccionario con las personas
print(personas)
print(personas.keys()) #imprimo las claves del diccionario
print(personas,[ "moises"]) #imprimo el valor de la clave moises 
print(personas.values()) #imprimo los valores del diccionario 

#listas con diccionarios 
contactos=[
    {"nombre": "moises", "correo": "moises@.com"},
    {"nombre": "juan", "correo": "juan@.com"},
    {"nombre": "pedro", "correo": "pedro@.com"}
]
print(contactos) 
contactos[0]["nombre"]="moiso" #cambio el nombre de moises por moiso, de contactos la posición 0 del campo nombre cambiar por moiso 
print(contactos[0]["nombre"]) #imprimo el primer diccionario de la lista y el primer campo nombre
print("\n Listado de contactos \n")
for contacto in contactos: #recorro la lista contactos
    print(f"nombre del contacto: {contacto['nombre']}") #imprimo el campo nombre de cada diccionario de la lista contactos
    print(f"correo del contacto: {contacto['correo']}") #imprimo el campo correo de cada diccionario de la lista contactos
    print("\n") #imprimo un salto de linea para que no se superpongan los datos de los contactos