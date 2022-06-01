import pandas as pd 
#cargar archvivos 
pd.read_csv('C:\Users\moise\OneDrive\Desktop\MisiónTIC2022Programación1\pandas\data2.csv', sep=',') #cargar archivo csv 
#sep = separador 
#header
pd.read_csv('C:\Users\moise\OneDrive\Desktop\MisiónTIC2022Programación1\pandas\data2.csv', sep=',', header=0) #header, posicion 0	

df_books=pd.read_csv('C:\Users\moise\OneDrive\Desktop\MisiónTIC2022Programación1\pandas\data2.csv', sep=',', header=0) #header, posicion 0
df_books.head() #muestra los primeros 5 registros
df_books.tail() #muestra los ultimos 5 registros
df_books.info() #muestra informacion del dataframe
df_books.describe() #muestra informacion estadistica del dataframe
df_books.columns #muestra las columnas del dataframe
df_books.dtypes #muestra los tipos de datos de cada columna
df_books.shape #muestra el numero de filas y columnas del dataframe
df_books.index #muestra el indice del dataframe
df_books.values #muestra los valores del dataframe
df_books.loc[0] #muestra el primer registro del dataframe
df_books.loc[0:2] #muestra los primeros 3 registros del dataframe
df_books.loc[0:2, 'title'] #muestra los primeros 3 registros del dataframe, solo muestra la columna title
df_books.loc[0:2, ['title', 'author']] #muestra los primeros 3 registros del dataframe, solo muestra las columnas title y author
df_books.loc[0:2, ['title', 'author']] #muestra los primeros 3 registros del dataframe, solo muestra las columnas title y author
df_books.loc[0:2, ['title', 'author']] #muestra los primeros 3 registros del dataframe, solo muestra las columnas title y author
df_books.loc[0:2, ['title', 'author']] #muestra los primeros 3 registros del dataframe, solo muestra las columnas title y author
df_books.loc[0:2, ['title', 'author']] #muestra los primeros 3 registros del dataframe, solo muestra las columnas title y author 

#leer json
pd.read_json('C:\Users\moise\OneDrive\Desktop\MisiónTIC2022Programación1\pandas\data2.json') #leer json

#loc y iloc
df_books[0:4] #muestra los primeros 4 registros del dataframe
df_books['Name'] #muestra la columna title del dataframe
df_books[['Name', 'Author']] #muestra las columnas title y author del dataframe 

df_books.loc[0:4, ['Name', 'Author']] #muestra los primeros 4 registros del dataframe, solo muestra las columnas title y authorque estan en la posicion 0 y 1

df_books.loc[:,['Author']] == 'JJ Smith' #muestra los registros que tengan el valor de author = JJ Smith 

#iloc
df_books.iloc[0:4, [0,1]] #muestra los primeros 4 registros del dataframe, solo muestra las columnas name y author que estan en la posicion 0 y 1
#la busqueda es por el index del dataframe

