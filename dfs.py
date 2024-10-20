from input import graph
from collections import deque


def depth_first_search(graph, current, target, explored=None, route=None):
    if explored is None:
        explored = set()
    if route is None:
        route = []

    explored.add(current)
    route.append(current)
    print(f"Currently at: {current}")

    if current == target:
        print(f"Success! Reached {target}.")
        print("Discovered Path:", " -> ".join(route))
        return True

    for adjacent in graph.get(current, []):
        if adjacent not in explored:
            if depth_first_search(graph, adjacent, target, explored, route):
                return True

    route.pop()
    return False


depth_first_search(graph, 'S', 'G')