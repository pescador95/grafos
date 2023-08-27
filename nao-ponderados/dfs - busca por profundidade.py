# Busca em Profundidade (DFS - Depth-First Search):
# A busca em profundidade explora o máximo possível por um ramo antes de retroceder. Pode usar recursão ou uma pilha.

def dfs(graph, current_node, target_node, visited=set()):
    if current_node == target_node:
        return [current_node]

    if current_node in visited:
        return None

    visited.add(current_node)

    for neighbor in graph[current_node]:
        path = dfs(graph, neighbor, target_node, visited)
        if path is not None:
            return [current_node] + path

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

result = dfs(graph, start_node, target_node)

if result:
    print(f'Caminho de {start_node} para {target_node}: {result}')
else:
    print(f'Não foi encontrado um caminho entre {start_node} e {target_node}.')
