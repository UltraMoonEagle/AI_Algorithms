from input import graph,heuristic
from collections import deque

def beam_search(graph, heuristic, start, goal, width=2):
    beam = [(heuristic[start], [start])]

    while beam:
        next_beam = []

        for current_cost, current_path in beam:
            current_node = current_path[-1]

            if current_node == goal:
                return current_path, current_cost

            for neighbor in graph.get(current_node, {}).keys():
                if neighbor not in current_path:
                    new_path = current_path + [neighbor]
                    new_cost = current_cost + heuristic[neighbor]
                    next_beam.append((new_cost, new_path))

        beam = sorted(next_beam, key=lambda x: x[0])[:width]

    return None, float('inf')

# Example usage
solution, cost = beam_search(graph, heuristic, 'S', 'G', width=2)
print("Solution Path:", solution)
print("Path Cost:", cost)
