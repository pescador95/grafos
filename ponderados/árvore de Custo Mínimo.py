# Árvore de Custo Mínimo (Kruskal)

def kruskal(graph):
    def find(parent, node):
        if parent[node] == node:
            return node
        return find(parent, parent[node])

    def union(parent, rank, node1, node2):
        root1 = find(parent, node1)
        root2 = find(parent, node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    edges = [(weight, node1, node2) for node1, adjacent in graph.items()
             for node2, weight in adjacent.items()]
    edges.sort()

    minimum_spanning_tree = {}
    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    for weight, node1, node2 in edges:
        if find(parent, node1) != find(parent, node2):
            union(parent, rank, node1, node2)
            if node1 not in minimum_spanning_tree:
                minimum_spanning_tree[node1] = {}
            minimum_spanning_tree[node1][node2] = weight
            if node2 not in minimum_spanning_tree:
                minimum_spanning_tree[node2] = {}
            minimum_spanning_tree[node2][node1] = weight

    return minimum_spanning_tree


weighted_undirected_graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'D': 2, 'E': 4},
    'C': {'A': 2, 'F': 5},
    'D': {'B': 2},
    'E': {'B': 4, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

minimum_spanning_tree = kruskal(weighted_undirected_graph)
print('Árvore de Custo Mínimo:')
for node, adjacent in minimum_spanning_tree.items():
    for neighbor, weight in adjacent.items():
        print(f'{node} - {neighbor}: {weight}')
