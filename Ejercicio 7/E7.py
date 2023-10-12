import networkx as nx
# Crear un grafo dirigido
familia = nx.DiGraph()

familia.add_node("Abuelo")
familia.add_node("Abuela")
familia.add_node("Padre")
familia.add_node("Madre")
familia.add_node("Hijo")
familia.add_node("Tio")
familia.add_node("Primo")

familia.add_edge("Abuelo", "Padre")
familia.add_edge("Abuela", "Padre")
familia.add_edge("Abuelo", "Tio")
familia.add_edge("Abuela", "Tio")
familia.add_edge("Padre", "Hijo")
familia.add_edge("Madre", "Hijo")
familia.add_edge("Padre", "Primo")
familia.add_edge("Madre", "Primo")

import matplotlib.pyplot as plt
pos = nx.spring_layout(familia, seed=42)
nx.draw(familia, pos, with_labels=True, node_size=800, node_color='lightblue')
plt.title("Árbol Familiar")
plt.show()
