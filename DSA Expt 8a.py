from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            bfs_order.append(vertex)
            queue.extend(graph[vertex] - visited)
    return bfs_order
graph = {
    "A": {"B", "C"},
    "B": {"A", "D", "E"},
    "C": {"A", "F"},
    "D": {"B"},
    "E": {"B", "F"},
    "F": {"C", "E"},
}
print("BFS:", bfs(graph, "A"))
