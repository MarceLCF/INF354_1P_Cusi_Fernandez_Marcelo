import numpy as np
import pandas as pd

datos = pd.read_csv("vgsales.csv")
datos2 = pd.read_csv("vgsales2.csv")

#********************************************************+
def imputacion(columna):
	print("\n********** Columna: ",columna,"***************************")
	data = datos[columna]
	#***media
	media = round(data.mean(),4)
	print("Media:",media)
	
	print("Antes de la imputacion:".upper())
	print(datos2[columna])

	print("\nDespues de la imputacion:".upper())
	datos2[columna] = datos2[columna].fillna(media)
	print(datos2[columna])
	

imputacion("NA_Sales")
#imputacion("EU_Sales")
#imputacion("JP_Sales")
imputacion("Other_Sales")
