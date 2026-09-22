class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((weight, vertex, neighbor))
    edges.sort()
    disjoint_set = DisjointSet(graph.keys())
    mst = []
    total_cost = 0
    for weight, vertex1, vertex2 in edges:
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            disjoint_set.union(vertex1, vertex2)
            mst.append((vertex1, vertex2, weight))
            total_cost += weight
    return mst, total_cost
graph = {
    "A": {"B": 1, "C": 3},
    "B": {"A": 1, "C": 1, "D": 6},
    "C": {"A": 3, "B": 1, "D": 2},
    "D": {"B": 6, "C": 2},
}
mst, cost = kruskal(graph)
print("Kruskal's MST:", mst)
print("Total cost:", cost)
