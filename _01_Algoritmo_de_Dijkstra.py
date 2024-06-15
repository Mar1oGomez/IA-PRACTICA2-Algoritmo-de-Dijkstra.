#Mario Alberto Gomez Temores     21310159     16\06\24

import heapq
# Importamos la biblioteca heapq para manejar la cola de prioridad (min-heap).

def dijkstra(graph, start):
    # Definimos la funcion Dijkstra que toma como entrada el grafo y el nodo de inicio.
    
    queue = [(0, start)]
    # Inicializamos la cola de prioridad con una tupla que contiene la distancia inicial (0) y el nodo de inicio.

    distances = {node: float('inf') for node in graph}
    # Creamos un diccionario para almacenar las distancias minimas desde el nodo de inicio a cada nodo. Inicialmente, todas las distancias son infinitas.

    distances[start] = 0
    # La distancia desde el nodo de inicio a si mismo es 0.

    previous_nodes = {node: None for node in graph}
    # Creamos un diccionario para almacenar el nodo anterior en el camino mas corto hacia cada nodo.

    while queue:
        # Mientras haya nodos en la cola de prioridad:
        
        current_distance, current_node = heapq.heappop(queue)
        # Extraemos el nodo con la menor distancia acumulada de la cola de prioridad.

        if current_distance > distances[current_node]:
            continue
        # Si la distancia extraida es mayor que la distancia almacenada, continuamos al siguiente ciclo para evitar procesar nodos redundantes.

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Calculamos la distancia total desde el nodo de inicio hasta el vecino actual pasando por el nodo actual.

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
                # Si encontramos una distancia menor, actualizamos la distancia y el nodo anterior, y anadimos el vecino a la cola de prioridad.

    return distances, previous_nodes
    # Devolvemos los diccionarios de distancias minimas y nodos anteriores.

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
# Definimos un grafo de ejemplo usando un diccionario de diccionarios.

start_node = 'A'
# Definimos el nodo de inicio.

distances, previous_nodes = dijkstra(graph, start_node)
# Llamamos a la funcion Dijkstra con el grafo y el nodo de inicio.

print("Distancias desde el nodo inicial:")
for node, distance in distances.items():
    print(f"{node}: {distance}")
# Imprimimos las distancias minimas desde el nodo de inicio a cada nodo.

print("\nNodos anteriores en el camino mas corto:")
for node, previous in previous_nodes.items():
    print(f"{node}: {previous}")
# Imprimimos los nodos anteriores en el camino mas corto hacia cada nodo.


