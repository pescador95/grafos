# Busca A:*
# A busca A* combina a busca em largura com uma função heurística para avaliar a promessa de um nó. É eficiente e garante uma solução ótima se a heurística for admissível.

def a_star_search(graph, start_node, target_node, heuristic):
    priority_queue = [(heuristic[start_node], start_node, [start_node])]
    visited = set()

    while priority_queue:
        cost, current_node, path = priority_queue.pop(0)

        if current_node == target_node:
            return path

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                priority_queue.append(
                    (cost + heuristic[neighbor], neighbor, new_path))
                priority_queue.sort()

    return None


heuristic = {
    'A': 2,
    'B': 3,
    'C': 1,
    'D': 4,
    'E': 5,
    'F': 0
}

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

result = a_star_search(graph, start_node, target_node, heuristic)
print(f'Caminho de {start_node} para {target_node} usando A*: {result}')
