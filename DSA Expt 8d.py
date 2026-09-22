import heapq
def prim(graph, start):
    mst = []
    visited = set()
    edges = [(0, start, None)]
    total_cost = 0
    while edges:
        weight, vertex, parent = heapq.heappop(edges)
        if vertex not in visited:
            visited.add(vertex)
            if parent is not None:
                mst.append((parent, vertex, weight))
                total_cost += weight
            for next_vertex, next_weight in graph[vertex].items():
                if next_vertex not in visited:
                    heapq.heappush(edges, (next_weight, next_vertex, vertex))
    return mst, total_cost
graph = {
    "A": {"B": 1, "C": 3},
    "B": {"A": 1, "C": 1, "D": 6},
    "C": {"A": 3, "B": 1, "D": 2},
    "D": {"B": 6, "C": 2},
}
mst, cost = prim(graph, "A")
print("Prim's MST:", mst)
print("Total cost:", cost)
