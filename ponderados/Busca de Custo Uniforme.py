import heapq

# Busca de Custo Uniforme (Uniform Cost Search).
# Nesse caso, o grafo terá pesos associados às arestas, e o algoritmo buscará o caminho de menor custo.


def uniform_cost_search(graph, start_node, target_node):
    priority_queue = [(0, start_node, [start_node])]
    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node == target_node:
            return path

        visited.add(current_node)

        for neighbor, edge_cost in graph[current_node].items():
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (new_cost, neighbor, new_path))

    return None


weighted_graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

start_node = 'A'
target_node = 'F'

result = uniform_cost_search(weighted_graph, start_node, target_node)
print(
    f'Caminho de {start_node} para {target_node} usando Busca de Custo Uniforme: {result}')
