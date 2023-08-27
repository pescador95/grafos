# Grafo de Similaridade Ponderada (Algoritmo de Prim para Encontrar Árvore Geradora Mínima)

def prim(graph):
    mst = {node: {} for node in graph}
    visited = {node: False for node in graph}
    visited[list(graph.keys())[0]] = True

    while False in visited.values():
        min_weight = float('inf')
        u, v = None, None

        for node in visited:
            if visited[node]:
                for neighbor, weight in graph[node].items():
                    if not visited[neighbor] and weight < min_weight:
                        min_weight = weight
                        u, v = node, neighbor

        visited[v] = True
        mst[u][v] = min_weight
        mst[v][u] = min_weight

    return mst


weighted_similarity_graph = {
    'A': {'B': 0.5, 'C': 0.2},
    'B': {'A': 0.5, 'C': 0.8, 'D': 0.7},
    'C': {'A': 0.2, 'B': 0.8, 'D': 0.3},
    'D': {'B': 0.7, 'C': 0.3}
}

minimum_spanning_tree_similarity = prim(weighted_similarity_graph)
print('Árvore Geradora Mínima baseada em Similaridade:')
for node, adjacent in minimum_spanning_tree_similarity.items():
    for neighbor, weight in adjacent.items():
        print(f'{node} - {neighbor}: {weight}')
