from collections import deque

# Busca em Largura (BFS - Breadth-First Search):
# A busca em largura explora os nós vizinhos antes de explorar os nós mais distantes. Ela usa uma fila para manter os nós a serem visitados.


def bfs(graph, start_node, target_node):
    queue = deque([(start_node, [start_node])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == target_node:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

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

result = bfs(graph, start_node, target_node)

if result:
    print(f'Caminho de {start_node} para {target_node}: {result}')
else:
    print(f'Não foi encontrado um caminho entre {start_node} e {target_node}.')
