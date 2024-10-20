import heapq
from input import graph, heuristic

def best_first_search_algorithm(start, target, graph_structure, heuristic_values):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic_values[start], start, [start], 0))
    
    explored_nodes = set()
    
    while priority_queue:
        heuristic_cost, current_node, path, cumulative_cost = heapq.heappop(priority_queue)
        
        if current_node == target:
            return path, cumulative_cost
        
        explored_nodes.add(current_node)
        
        for neighbor, edge_cost in graph_structure[current_node].items():
            if neighbor not in explored_nodes:
                total_cost = cumulative_cost + edge_cost
                heapq.heappush(priority_queue, (heuristic_values[neighbor], neighbor, path + [neighbor], total_cost))
    
    return None, None

start_node = 'S'
goal_node = 'G'
result_path, total_cost = best_first_search_algorithm(start_node, goal_node, graph, heuristic)

print("Best First Search Path:", result_path)
print("Total Cost:", total_cost)
