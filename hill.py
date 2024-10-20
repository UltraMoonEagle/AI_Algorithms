from input import graph,heuristic
from collections import deque

def hill_climb(graph, heuristic, start, end):
    def compute_cost(path):
        return sum(heuristic[n] for n in path)

    def swap_neighbors(path):
        neighbors = []
        for i in range(1, len(path) - 1):
            for j in range(i + 1, len(path) - 1):
                new_path = path[:]
                new_path[i], new_path[j] = new_path[j], new_path[i]
                neighbors.append(new_path)
        return neighbors

    def find_best_neighbor(current_path):
        neighbors = swap_neighbors(current_path)
        best_path = current_path
        lowest_cost = compute_cost(current_path)
        for neighbor in neighbors:
            neighbor_cost = compute_cost(neighbor)
            if neighbor_cost < lowest_cost:
                best_path = neighbor
                lowest_cost = neighbor_cost
        return best_path, lowest_cost

    node = start
    path = [node]
    while node != end:
        neighbors = graph.get(node, {})
        if not neighbors:
            break
        next_node = min(neighbors, key=lambda n: heuristic[n])
        if next_node not in path:
            path.append(next_node)
        node = next_node

    current_path = path
    current_cost = compute_cost(current_path)

    while True:
        neighbor_path, neighbor_cost = find_best_neighbor(current_path)
        if neighbor_cost >= current_cost:
            print(f"Reached a local optimum: {current_path} with cost {current_cost}")
            break
        current_path = neighbor_path
        current_cost = neighbor_cost

    return current_path, current_cost

# Example usage
final_path, final_cost = hill_climb(graph, heuristic, 'S', 'G')
print("Optimal Path Found:", final_path)
print("Total Path Cost:", final_cost)
