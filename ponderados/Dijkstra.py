import heapq

# Grafo Direcionado Ponderado com Dijkstra (Busca de Menor Caminho)


def dijkstra(graph, start_node, target_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        dist, current_node = heapq.heappop(priority_queue)

        if current_node == target_node:
            return dist

        if dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return None


weighted_directed_graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

start_node = 'A'
target_node = 'F'

result_dijkstra = dijkstra(weighted_directed_graph, start_node, target_node)
print(
    f'Distância mínima de {start_node} para {target_node} usando Dijkstra: {result_dijkstra}')
