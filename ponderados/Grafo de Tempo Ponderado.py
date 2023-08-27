# Grafo de Tempo Ponderado (Algoritmo de Dijkstra com Restrição de Tempo)

import heapq


def dijkstra_with_time_constraint(graph, start_node, target_node, max_time):
    priority_queue = [(0, start_node)]
    visited = set()

    while priority_queue:
        time, current_node = heapq.heappop(priority_queue)

        if current_node == target_node and time <= max_time:
            return True

        if time > max_time or current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, edge_time in graph[current_node].items():
            heapq.heappush(priority_queue, (time + edge_time, neighbor))

    return False


weighted_time_graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

start_node = 'A'
target_node = 'F'
max_time = 7

reachable = dijkstra_with_time_constraint(
    weighted_time_graph, start_node, target_node, max_time)
print(
    f'É possível chegar de {start_node} para {target_node} em no máximo {max_time} unidades de tempo? {reachable}')
