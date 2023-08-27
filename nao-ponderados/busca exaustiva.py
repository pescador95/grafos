# Busca Exaustiva:
# A busca exaustiva explora todas as possíveis soluções. Pode ser usada quando a solução ótima é necessária, mas pode ser lenta para problemas complexos.

def exhaustive_search(graph, current_node, target_node, path=[]):
    path = path + [current_node]

    if current_node == target_node:
        return [path]

    paths = []

    for neighbor in graph[current_node]:
        if neighbor not in path:
            new_paths = exhaustive_search(graph, neighbor, target_node, path)
            paths.extend(new_paths)

    return paths


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

result = exhaustive_search(graph, start_node, target_node)
print(f'Todos os caminhos de {start_node} para {target_node}: {result}')
