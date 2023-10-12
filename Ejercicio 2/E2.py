import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("vgsales.csv")

#********************************************************+
def grafica_columna(columna):
	print("\n********** Columna: ",columna,"***************************")
	data = datos[columna]
	#***media
	media = round(data.mean(),4)
	print("Media:",media, "[millones] de ventas")

	#***moda
	moda = data.mode()[0]
	print("Moda:",moda,"[millones] de ventas\n")
	
	
	#***Calcula cuartiles y percentiles
	q1 = np.percentile(data, 25)
	q2 = np.percentile(data, 50)  #Mediana
	q3 = np.percentile(data, 75)
	
	p10 = np.percentile(data, 10)
	p90 = np.percentile(data, 90)
	
	print("-CUARTILES")
	print(f"Q1 (cuartil 1): El 25% de los datos estan por debajo de {q1}")
	print(f"Q2 (cuartil 2): El 50% de los datos estan por debajo de {q2}")
	print(f"Q3 (cuartil 3): El 75% de los datos estan por debajo de {q3}\n")
	print("-PERCENTILES")
	#p = int(input("Que percentil desea calcular? (1-100): "))
	print(f"P10: El 10% de los datos estan por debajo de {p10}")
	print(f"P90: El 90% de los datos estan por debajo de {p90}")
	
	#GRAFICANDO...
	plt.boxplot(data)

	# Líneas para los datos
	plt.axhline(media, color='r', linestyle='solid', label='Media')
	plt.axhline(moda, color='b', linestyle='dotted', label='Moda')

	plt.axhline(q1, color='g', linestyle='--', label='Q1 (25%)')
	plt.axhline(q2, color='g', linestyle='-.', label='Q2 (Mediana)')
	plt.axhline(q3, color='g', linestyle=':', label='Q3 (75%)')

	plt.axhline(p10, color='m', linestyle='-.', label='Percentil 10')
	plt.axhline(p90, color='y', linestyle='-.', label='Percentil 90')

	# Etiquetas
	plt.title('Diagrama de Caja con media, moda, cuartiles y percentiles\npara la columna '+columna)
	plt.ylabel('Valores')
	plt.legend()

	plt.show()



grafica_columna("NA_Sales")
grafica_columna("EU_Sales")
grafica_columna("JP_Sales")
grafica_columna("Other_Sales")
#grafica_columna("Global_Sales")
