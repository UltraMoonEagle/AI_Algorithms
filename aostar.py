import math
from input import graph, heuristic

def ao_star_search(current_node, graph_structure, heuristic_values, target, explored):
    if current_node == target:
        return 0, [target]

    if current_node in explored:
        return math.inf, []

    explored.add(current_node)

    lowest_cost = math.inf
    optimal_subtree_path = []

    for next_node, edge_cost in graph_structure[current_node].items():
        cost_of_subtree, path_of_subtree = ao_star_search(next_node, graph_structure, heuristic_values, target, explored)
        total_expense = edge_cost + cost_of_subtree

        if total_expense < lowest_cost:
            lowest_cost = total_expense
            optimal_subtree_path = [current_node] + path_of_subtree

    explored.remove(current_node)

    return lowest_cost, optimal_subtree_path

def execute_ao_star(start, goal):
    explored_nodes = set()
    total_expense, resulting_path = ao_star_search(start, graph, heuristic, goal, explored_nodes)
    return resulting_path, total_expense

start_node = 'S'
goal_node = 'G'
resulting_path, total_expense = execute_ao_star(start_node, goal_node)

print("AO* Search Path:", resulting_path)
print("Total Cost to Target:", total_expense)
