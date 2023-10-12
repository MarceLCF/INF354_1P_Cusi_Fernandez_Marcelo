import pandas as pd

datos = pd.read_csv("vgsales.csv")


print("*** Antes del etiquetado binario: ***".upper())
data = datos["Genre"]
print(data,"\n","-"*60)

#Aplicadno etiquetado binario a la columna 'Genre' (genero), 0 si el genero del juego es deporte, estrategia o accion, en otro caso: 1
c = 0
for i in data:
	if data[c] in ["Sports","Strategy","Action"]:
		data[c] = "0"
	else:
		data[c] = "1"
	c+=1

print("-"*60,"\n*** Despues del etiquetado binario: ***".upper())
print(datos["Genre"])

