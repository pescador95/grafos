# Grafo de Fluxo de Rede (Ford-Fulkerson - Fluxo Máximo)

def ford_fulkerson(graph, source, sink):
    def dfs(node, min_capacity):
        visited.add(node)
        if node == sink:
            return min_capacity

        for neighbor, capacity in graph[node].items():
            if neighbor not in visited and capacity > 0:
                flow = dfs(neighbor, min(min_capacity, capacity))
                if flow > 0:
                    graph[node][neighbor] -= flow
                    graph[neighbor][node] += flow
                    return flow

        return 0

    max_flow = 0
    while True:
        visited = set()
        flow = dfs(source, float('inf'))
        if flow == 0:
            break
        max_flow += flow

    return max_flow


flow_network_graph = {
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

max_flow = ford_fulkerson(flow_network_graph, source_node, sink_node)
print(f'Fluxo máximo entre {source_node} e {sink_node}: {max_flow}')
