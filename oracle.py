from input import graph,heuristic
import heapq

def least_cost_search(graph, start, goal):
    queue = [(0, start, [start])]
    min_costs = {node: float('inf') for node in graph}
    min_costs[start] = 0

    while queue:
        current_cost, current_node, current_path = heapq.heappop(queue)

        if current_node == goal:
            return current_path, current_cost

        for neighbor, travel_cost in graph[current_node].items():
            new_cost = current_cost + travel_cost

            if new_cost < min_costs[neighbor]:
                min_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor, current_path + [neighbor]))

    return None, float('inf')

final_path, total_cost = least_cost_search(graph, 'S', 'G')
print("Least Cost Path:", final_path)
print("Total Path Cost:", total_cost)
