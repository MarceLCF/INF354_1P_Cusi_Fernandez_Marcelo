from sklearn.datasets import load_iris

datos= load_iris()
x = datos.data
y = datos.target

# cantidad  total de muestras
cant = len(x)

# Definir el tamaño del train y test
train_size = int(0.8 * cant)
test_size = cant - train_size

# lista de índices
indices = list(range(cant))

import random
#mezclando los indices para que los dstos de train y test sean aleatorios
random.shuffle(indices)

# Dividir los índices entrenamiento y prueba
train_ind = indices[:train_size]
test_ind = indices[train_size:]

# se crean los conjuntos de train y test
train_data = [x[i] for i in train_ind]
train_target = [y[i] for i in train_ind]

test_data = [x[i] for i in test_ind]
test_target = [y[i] for i in test_ind]

print("Tamaño del train:", len(train_data))
print("Tamaño del test:", len(test_data))
