#diccionario traduzca español a ingles 
diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')

"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente. El programa 
1.	Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2.	Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3.	Preguntar por el NIF del cliente y mostrar sus datos.
4.	Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5.	Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6.	Terminar el programa

"""
#menu de opciones 
opcion = 0
clientes = {}
while opcion != 6:
    print("""
    1. Introducir datos de un cliente
    2. Eliminar datos de un cliente
    3. Mostrar datos de un cliente
    4. Mostrar lista de clientes
    5. Mostrar clientes preferentes
    6. Salir
    """)
    opcion = int(input("Introduce una opción: "))
    if opcion == 1:
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            print("El cliente ya existe")
        else:
            nombre = input("Introduce el nombre del cliente: ")
            direccion = input("Introduce la dirección del cliente: ")
            telefono = input("Introduce el teléfono del cliente: ")
            correo = input("Introduce el correo del cliente: ")
            preferente = input("¿Es el cliente preferente? (S/N): ")
            if preferente.upper() == "S":
                preferente = True
            else:
                preferente = False
            clientes[nif] = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo, 'preferente': preferente} #crea un diccionario con los datos del cliente, clave:valor
    elif opcion == 2: 
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("El cliente no existe")
    elif opcion == 3:
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            print(clientes[nif])
        else:
            print("El cliente no existe")
    elif opcion == 4:
        print(clientes)
    elif opcion == 5:
        for i in clientes:
            if clientes[i]['preferente'] == True:
                print(clientes[i]) 


