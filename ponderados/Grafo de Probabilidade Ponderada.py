# Grafo de Probabilidade Ponderada (Algoritmo de Bellman-Ford com Probabilidades)

def bellman_ford_with_probabilities(graph, start_node):
    probabilities = {node: 0 for node in graph}
    probabilities[start_node] = 1

    for _ in range(len(graph) - 1):
        for node, adjacent in graph.items():
            for neighbor, probability in adjacent.items():
                probabilities[neighbor] = max(
                    probabilities[neighbor], probabilities[node] * probability)

    return probabilities


weighted_probability_graph = {
    'A': {'B': 0.5, 'C': 0.2},
    'B': {'C': 0.3, 'D': 0.7},
    'C': {'D': 0.1},
    'D': {'A': 0.4}
}

start_node = 'A'

probabilities = bellman_ford_with_probabilities(
    weighted_probability_graph, start_node)
print(
    f'Probabilidades máximas de chegar a cada nó a partir de {start_node}: {probabilities}')
