import heapq
from input import graph, heuristic
def heuristic_branch_and_bound(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited_costs = {}
    best_cost = float('inf')
    best_path = None

    while queue:
        f_cost, current_g_cost, current_node, current_path = heapq.heappop(queue)

        if current_node == goal and current_g_cost < best_cost:
            best_cost = current_g_cost
            best_path = current_path
            continue

        if current_node in visited_costs and visited_costs[current_node] <= current_g_cost:
            continue

        visited_costs[current_node] = current_g_cost

        for neighbor, edge_cost in graph[current_node].items():
            new_g_cost = current_g_cost + edge_cost
            f_neighbor = new_g_cost + heuristic[neighbor]

            if new_g_cost < best_cost:
                heapq.heappush(queue, (f_neighbor, new_g_cost, neighbor, current_path + [neighbor]))

    return best_path, best_cost


solution_path, solution_cost = heuristic_branch_and_bound(graph, heuristic, 'S', 'G')
print("Best Path (Heuristic Branch and Bound):", solution_path)
print("Total Path Cost:", solution_cost)
