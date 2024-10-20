from input import graph
from collections import deque

def breadth_first_search(graph, source, target):
    visited = set()
    queue = deque([(source, [source])])

    while queue:
        current_node, current_path = queue.popleft()
        print(f"Exploring: {current_node}")

        if current_node == target:
            print(f"Success! Reached {target}.")
            print("Found Path:", " -> ".join(current_path))
            return True

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, current_path + [neighbor]))

    print(f"{target} could not be reached.")
    return False

breadth_first_search(graph, 'S', 'G')