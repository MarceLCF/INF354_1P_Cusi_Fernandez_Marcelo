archivo = open("vgsales.csv")
f = archivo.readlines()

head = f[0].strip("\n").strip(";").split(",")
datos = []
for linea in f[1:]:
	dato = linea.strip("\n").strip(";").split(",")
	datos.append(dato)
#print(datos)

#********************************************************+
def grafica_columna(columna):
	print("\n********** Columna: ",columna,"***************************")
	x = head.index(columna)	
	#***media
	suma_ventas = 0
	for i in datos:
		suma_ventas += float(i[x])

	media = round(suma_ventas/len(datos),4)
	print("Media:",media, "[millones] de ventas")

	#***moda
	ventas = [float(i[x]) for i in datos]
	valores = set(ventas)
	may = 0
	moda = 0
	for i in valores:
		cont = ventas.count(i)
		#print(cont)
		if cont > may:
			may = cont
			moda = float(i)

	print("Moda:",moda,"[millones] de ventas\n")

	#PARA LAS GRAFICAS
	import matplotlib.pyplot as plt
	# Calcula cuartiles y percentiles
	data_sorted = sorted(ventas)
	n = len(data_sorted)
	q1 = data_sorted[int(n * 0.25)]
	q2 = data_sorted[int(n * 0.5)]
	q3 = data_sorted[int(n * 0.75)]
	p10 = data_sorted[int(n * 0.1)]
	p90 = data_sorted[int(n * 0.9)]
	
	print("-CUARTILES")
	print(f"Q1 (cuartil 1): El 25% de los datos estan por debajo de {q1}")
	print(f"Q2 (cuartil 2): El 50% de los datos estan por debajo de {q2}")
	print(f"Q3 (cuartil 3): El 75% de los datos estan por debajo de {q3}\n")
	print("-PERCENTILES")
	#p = int(input("Que percentil desea calcular? (1-100): "))
	print(f"P10: El 10% de los datos estan por debajo de {p10}")
	print(f"P90: El 90% de los datos estan por debajo de {p90}")

	plt.boxplot(ventas)

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


print(head)
grafica_columna("NA_Sales")
grafica_columna("EU_Sales")
grafica_columna("JP_Sales")
grafica_columna("Other_Sales")
grafica_columna("Global_Sales")

