class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Initialize distances from the source vertex to all other vertices as infinity
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Relax all edges |V| - 1 times, where |V| is the number of vertices
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph contains negative-weight cycle")
                return

        return dist

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, -3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -2)

source_vertex = 0
shortest_distances = g.bellman_ford(source_vertex)

print("Shortest distances from source vertex:")
for i, dist in enumerate(shortest_distances):
    print(f"Vertex {i}: {dist}")
