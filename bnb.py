import heapq
from input import graph

def branch_and_bound_search(graph, start, goal):
    queue = [(0, start, [start])]
    best_cost = float('inf')
    best_path = None

    while queue:
        current_cost, current_node, current_path = heapq.heappop(queue)

        if current_node == goal and current_cost < best_cost:
            best_cost = current_cost
            best_path = current_path

        for neighbor, edge_cost in graph[current_node].items():
            new_cost = current_cost + edge_cost

            if new_cost < best_cost:
                heapq.heappush(queue, (new_cost, neighbor, current_path + [neighbor]))

    return best_path, best_cost

solution_path, solution_cost = branch_and_bound_search(graph, 'S', 'G')
print("Best Path (Branch and Bound):", solution_path)
print("Total Path Cost:", solution_cost)
