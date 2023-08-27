# Grafo de Distância Ponderada (Bellman-Ford - Menor Caminho com Pesos Negativos)

def bellman_ford(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    for _ in range(len(graph) - 1):
        for node, adjacent in graph.items():
            for neighbor, weight in adjacent.items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


weighted_distance_graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

start_node = 'A'

distances = bellman_ford(weighted_distance_graph, start_node)
print(f'Distâncias mínimas a partir de {start_node}: {distances}')
