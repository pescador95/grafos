# Busca Gulosa (Greedy Search):
# A busca gulosa escolhe o próximo nó que parece mais promissor com base em uma heurística. Pode não levar à solução ótima, mas é rápida e eficiente.

def greedy_search(graph, start_node, target_node, heuristic):
    priority_queue = [(heuristic[start_node], start_node)]
    visited = set()

    while priority_queue:
        cost, current_node = priority_queue.pop(0)

        if current_node == target_node:
            return visited

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                priority_queue.append((heuristic[neighbor], neighbor))
                priority_queue.sort()

    return visited


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

result = greedy_search(graph, start_node, target_node, heuristic)
print(f'Nós visitados pela busca gulosa: {result}')
