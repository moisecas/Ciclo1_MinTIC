"""
OPEN FUNCTION - Open a file for reading or writing. The mode argument is optional and defaults to 'r' for reading. 
The function returns a file object. If the file cannot be opened, an IOError exception is raised.
w - Write-only mode, truncates existing file to zero length or creates a new file for writing.
a - Write-only mode, appends to the end of the file if it exists, otherwise creates a new file for writing.

r=accedera al archivo para lectura 
w=accedera al archivo para escritura, se sobreescribe el archivo 
a=accedera al archivo para escritura y añadir al final del archivo 
"""
# Programa para crear un archivo desde python/lo abre/le incluye un texto /lo cierra.
from io import open
archivo1= open("MiArchivo.txt","w") #crea el archivo 
texto ="Moisés Castro\nDeveloper" #texto a escribir en el archivo
archivo1.write(texto) #escribe en el archivo, la relaciono con el archivo1 
archivo1.close() #cierra el archivo 

"""
construir un archivo de texto que contenga los siguientes datos: 
nombres, apellidos, pesos, estatura, fecha de nacimiento, empresa donde trabaja, 
ciudad donde vive, departamento donde vide y pais donde vive

"""
from io import open 
archivo2=open("MiArchivo2.txt","w")
texto2="Moisés \nCastro\n80k\n1.80\n15/11/1991\nUIS\nBucaramanga\nSantander\nColombia"
archivo2.write(texto2)
archivo2.close()

#programa que abre el archivo en modo lectura; lea su contenido y lo ponga en pantalla
from io import open #importa la libreria open
NombreArchivo ="MiArchivo.txt" #nombre del archivo
archivo1 =open(NombreArchivo,"r") #abre el archivo en modo lectura
texto =archivo1.read() #lee el archivo
archivo1.close() #cierra el archivo
print("ARCHIVO:",NombreArchivo) #imprime el nombre del archivo
print("Contenido:") #imprime el contenido del archivo
print(texto) #imprime el contenido del archivo, texto es la lectura del archivo 

#readline() lee una linea del archivo 
from io import open
NombreArchivo ="MiArchivo.txt"
archivo1 =open(NombreArchivo,"r")
texto =archivo1.readlines() #lee el archivo y lo guarda en una lista 
archivo1.close()
print("ARCHIVO:",NombreArchivo)
print("Contenido:")
print(texto)

