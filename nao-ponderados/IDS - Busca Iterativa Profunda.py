# Busca Iterativa Profunda (IDS - Iterative Deepening Search):
# A busca iterativa profunda é uma combinação da busca em profundidade limitada, onde o limite de profundidade aumenta gradualmente.

def dls(graph, current_node, target_node, depth_limit, visited=set()):
    if depth_limit < 0:
        return None

    if current_node == target_node:
        return [current_node]

    if current_node in visited:
        return None

    visited.add(current_node)

    for neighbor in graph[current_node]:
        path = dls(graph, neighbor, target_node, depth_limit - 1, visited)
        if path is not None:
            return [current_node] + path

    return None


def iterative_deepening(graph, start_node, target_node, max_depth):
    for depth_limit in range(max_depth + 1):
        result = dls(graph, start_node, target_node, depth_limit)
        if result is not None:
            return result

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
target_node = 'F'
max_depth = 5

result_dls = dls(graph, start_node, target_node, max_depth)
print(f'Caminho de {start_node} para {target_node} usando DLS com limite de profundidade {max_depth}: {result_dls}')

result_ids = iterative_deepening(graph, start_node, target_node, max_depth)
print(f'Caminho de {start_node} para {target_node} usando IDS com profundidade máxima {max_depth}: {result_ids}')
