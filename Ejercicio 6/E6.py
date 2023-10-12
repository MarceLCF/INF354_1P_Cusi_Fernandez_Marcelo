import pandas as pd

datos = pd.read_csv("vgsales1.csv")

#1ra tecnica de preprocesamiento
print("· 1. Manejo de datos faltantes en la columna Global_Sales:")
data = datos['Global_Sales']
print(data)

print("Se reemplaza los datos faltantes por la media, para evitar campos vacios en la columna")
datos['Global_Sales'].fillna(datos['Global_Sales'].mean(), inplace=True)
print(data)

#2da tecnica
print("\n\n· 2. Eliminacion de columnas:")

print(datos)

datos = datos.drop("Rank", axis=1)
datos = datos.drop("NA_Sales", axis=1)
datos = datos.drop("EU_Sales", axis=1)
datos = datos.drop("JP_Sales", axis=1)
datos = datos.drop("Other_Sales", axis=1)
print("Se eliminan algunas columnas innecesarias o que aportan poco en el analisis de datos")
print(datos)

#3ra tecnica
print("\n\n· 3. NORMALIZACION. en la columna Global Sales:")

from sklearn.preprocessing import MinMaxScaler
# Crea el objeto MinMaxScaler
scaler = MinMaxScaler()

print("Normalizando los datos para tenerlo en una escala de 0 a 1")
datos['Global_Sales'] = scaler.fit_transform(datos['Global_Sales'].values.reshape(-1, 1))
print(datos)
