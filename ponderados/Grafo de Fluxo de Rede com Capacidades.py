# Grafo de Fluxo de Rede com Capacidades (Edmonds-Karp - Fluxo Máximo em Fluxo de Rede)

def edmonds_karp(graph, source, sink):
    def bfs():
        visited = {node: False for node in graph}
        visited[source] = True
        parent = {node: None for node in graph}
        queue = [source]

        while queue:
            node = queue.pop(0)
            for neighbor, capacity in graph[node].items():
                if not visited[neighbor] and capacity > 0:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = node

        if visited[sink]:
            path = []
            current = sink
            while current != source:
                path.append((parent[current], current))
                current = parent[current]
            return path[::-1]
        return None

    max_flow = 0
    while True:
        augmenting_path = bfs()
        if not augmenting_path:
            break
        flow = min(graph[u][v] for u, v in augmenting_path)
        max_flow += flow
        for u, v in augmenting_path:
            graph[u][v] -= flow
            graph[v][u] += flow

    return max_flow


flow_network_capacity_graph = {
    'S': {'A': 10, 'B': 5},
    'A': {'C': 15, 'D': 10},
    'B': {'D': 15, 'E': 10},
    'C': {'T': 10},
    'D': {'C': 10, 'T': 15},
    'E': {'T': 10},
    'T': {}
}

source_node = 'S'
sink_node = 'T'

max_flow_capacity = edmonds_karp(
    flow_network_capacity_graph, source_node, sink_node)
print(
    f'Fluxo máximo entre {source_node} e {sink_node} com capacidades: {max_flow_capacity}')
