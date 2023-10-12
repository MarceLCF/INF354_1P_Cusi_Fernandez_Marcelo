import random
from sklearn.datasets import load_iris

# Cargar el conjunto de datos Iris
iris = load_iris()
data = iris.data
target = iris.target

# Obtener el número total de muestras
total_samples = len(data)

# Definir el tamaño del conjunto de entrenamiento y prueba
train_size = int(0.8 * total_samples)
test_size = total_samples - train_size

# Crear una lista de índices únicos
indices = list(range(total_samples))

# Mezclar los índices para asegurar que los datos de entrenamiento y prueba sean aleatorios
random.shuffle(indices)

# Dividir los índices en conjuntos de entrenamiento y prueba
train_indices = indices[:train_size]
test_indices = indices[train_size:]

# Crear los conjuntos de entrenamiento y prueba
train_data = [data[i] for i in train_indices]
train_target = [target[i] for i in train_indices]

test_data = [data[i] for i in test_indices]
test_target = [target[i] for i in test_indices]

print("Tamaño de los datos de entrenamiento:", len(train_data))
print("Tamaño de los datos de prueba:", len(test_data))
