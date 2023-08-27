class WeightedDistanceGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex1, vertex2, distance):
        if vertex1 not in self.graph:
            self.graph[vertex1] = {}
        if vertex2 not in self.graph:
            self.graph[vertex2] = {}

        self.graph[vertex1][vertex2] = distance
        self.graph[vertex2][vertex1] = distance

    def shortest_path(self, start_vertex, end_vertex):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start_vertex] = 0
        visited = set()
        current_vertex = start_vertex

        while current_vertex != end_vertex:
            visited.add(current_vertex)
            for neighbor, distance in self.graph[current_vertex].items():
                if neighbor not in visited:
                    new_distance = distances[current_vertex] + distance
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

            unvisited = {vertex: distances[vertex]
                         for vertex in distances if vertex not in visited}
            current_vertex = min(unvisited, key=unvisited.get)

        path = []
        while current_vertex != start_vertex:
            path.append(current_vertex)
            for neighbor, distance in self.graph[current_vertex].items():
                if distances[current_vertex] - distance == distances[neighbor]:
                    current_vertex = neighbor
                    break

        path.append(start_vertex)
        path.reverse()
        return path


graph = WeightedDistanceGraph()
graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'C', 5)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 4)
graph.add_edge('C', 'D', 1)

start_vertex = 'A'
end_vertex = 'D'

path = graph.shortest_path(start_vertex, end_vertex)
print(f'Caminho de {start_vertex} para {end_vertex}: {path}')
