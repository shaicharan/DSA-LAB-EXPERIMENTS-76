def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_order = [start]
    for next_vertex in graph[start] - visited:
        dfs_order.extend(dfs(graph, next_vertex, visited))
    return dfs_order
graph = {
    "A": {"B", "C"},
    "B": {"A", "D", "E"},
    "C": {"A", "F"},
    "D": {"B"},
    "E": {"B", "F"},
    "F": {"C", "E"},
}
print("DFS:", dfs(graph, "A"))
