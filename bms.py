from input import graph
from collections import deque

def bfs_search(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]
                queue.append(new_path)

    return None

path1 = bfs_search(graph, 'S', 'G')
print("Path 1:", " -> ".join(path1) if path1 else "No path found")

graph['S'] = ['B']

path2 = bfs_search(graph, 'S', 'G')
print("Path 2:", " -> ".join(path2) if path2 else "No path found")
