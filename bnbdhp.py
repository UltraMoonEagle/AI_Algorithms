import heapq
from input import graph, heuristic

def branch_and_bound_with_visited_check(graph, start, goal):
    queue = [(0, start, [start])]
    visited_costs = {}
    best_cost = float('inf')
    best_path = None

    while queue:
        current_cost, current_node, current_path = heapq.heappop(queue)

        if current_node == goal and current_cost < best_cost:
            best_cost = current_cost
            best_path = current_path

        if current_node in visited_costs and visited_costs[current_node] <= current_cost:
            continue

        visited_costs[current_node] = current_cost

        for neighbor, edge_cost in graph[current_node].items():
            total_cost = current_cost + edge_cost

            if total_cost < best_cost:
                heapq.heappush(queue, (total_cost, neighbor, current_path + [neighbor]))

    return best_path, best_cost

solution_path, solution_cost = branch_and_bound_with_visited_check(graph, 'S', 'G')
print("Optimal Path (Branch and Bound with Visited Check):", solution_path)
print("Total Path Cost:", solution_cost)
