#Dataframe
#Dataframe a partir de un diccionario
import pandas as pd
datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
'edad':[18, 22, 20, 21],
'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
}
df = pd.DataFrame(datos)
print(df)

import pandas as pd 
from google.colab import files 
uploaded = files.upload() #subir archivos 

import pandas as pd
from collections import Counter
ventasdf =pd.read_csv("SalesJan2009.csv")
ventasdf.head(3)

import pandas as pd
from collections import Counter
ventasdf =pd.read_csv("SalesJan2009.csv")
#print(ventas)
cp =Counter(ventasdf["Country"])#contar los valores de una columna
print(cp.most_common(3))
cv =Counter(ventasdf["Payment_Type"]) #cuenta las ocurrencias de cada valor de la columna Payment_Type  
print(cv.most_common(3)) #muestra los 3 mas comunes united states repetidos 462 veces

# Pandas y otras librerias
# Adicionalmente esposiblerealizarconsultasyoperacionessobrelos
# *.csv. A continuacion se grafican las ventas porfecha.
import pandas as pd
import datetime #datetime se utiliza para convertir fechas 
import matplotlib.pyplot as plt #matplotlib.pyplot se utiliza para graficar
#Reporte porfecha
ventasdf["Transaction_date"]=pd.to_datetime(ventasdf["Transaction_date"]) #convertir fecha a datetime
A = (ventasdf["Transaction_date"] #seleccionar la columna Transaction_date
.dt.floor("d") #el entero mas grande, devuelve el mayor de una serie de datos
.value_counts() #cuenta las ocurrencias de cada dia
.rename_axis("date") #renombrar la columna
.reset_index(name="num ventas")) #renombrar la columna
G=A.plot(x="date",y="num ventas",color="green",title="Ventasporfecha") #graficar
plt.show() #mostrar el grafico 
