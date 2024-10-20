import heapq
from input import graph, heuristic

def a_star_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    cost_tracker = {}

    while priority_queue:
        f_val, g_val, curr_node, curr_path = heapq.heappop(priority_queue)

        if curr_node == goal:
            return curr_path, g_val

        if curr_node in cost_tracker and cost_tracker[curr_node] <= g_val:
            continue

        cost_tracker[curr_node] = g_val

        for neighbor, edge_weight in graph[curr_node].items():
            new_g_val = g_val + edge_weight
            new_f_val = new_g_val + heuristic[neighbor]

            heapq.heappush(priority_queue, (new_f_val, new_g_val, neighbor, curr_path + [neighbor]))

    return None, float('inf')

start_node = 'S'
goal_node = 'G'

solution_path, solution_cost = a_star_search(graph, heuristic, start_node, goal_node)

print("A* Search Path:", solution_path)
print("Total Cost:", solution_cost)
