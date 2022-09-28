import pandas as pd
import numpy as np

raw = r'https://raw.githubusercontent.com/PosgradoMNA/Actividades_Aprendizaje-/main/default%20of%20credit%20card%20clients.csv'
print(raw)
df = pd.read_csv(raw)
# conversion to CSV
# print(df)
df = pd.read_csv(raw, index_col=0)
# print(df)
print(df.isnull().values.any())
# vamos a verificar si los datos no estan
print(df.isnull().any())
# verificamos por linea
# print(df)

# Apliquemos la solucion 1
ds1 = df.copy()
ds1.dropna(inplace=True)
print(ds1.isna().values.any())
print(ds1.isnull().any())  # verificamos por linea
print(ds1)
# nos damos cuenta de que esta solucion no funciona ya que perdemos datos los cuales son necesarios#
# Verificamos si la tecnica funciona en columnas
Copy = df.copy()
Copy.dropna(axis=1, inplace=True)  # axis 1 is columns / axis 0 is rows.
print(Copy)
# Tampoco funciona ya que perdemos todas las columnas menos una
# utlizamos otra tecnica donde solo dejamos 2 valores de cada nan
treshold = df.copy()
treshold.dropna(how='all', inplace=True)
treshold.dropna(thresh=4, inplace=True)  # en este sistema estamos probando que pása si pedimos almenos 4 valores
print(treshold)  # esta tecnica nos ayuda ya que perdemos menos elementos sin embargo aun seguimos perdiendo 1 fila
print(treshold.isna().values.any())
print(treshold.isnull().any())  # verificamos por linea y vemos que aun perdemos datos
# eliminemos columnas no necesarias
col = df.copy()
col.dropna(thresh=4,   # if there is not 5 nan values, the column will be eliminated
           axis=1,
           inplace=True)
print(col)
# con esto estams verificando que ninguna columna tiene mas de 5 datos faltantes  con esto podemos
# proceder a la solucion numero 2
# Solucion 2 #
ndf=df.copy()
wm=ndf.X1.mean()
print(wm)
#para fines de esta prueba usaremos los valores de media para