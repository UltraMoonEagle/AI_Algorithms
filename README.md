# AI Algorithms implementation

## AO* Algorithm 
The AO* algorithm is designed for searching through AND-OR graphs, which are particularly useful in scenarios involving contingent decisions. This algorithm excels in solving complex decision-making problems by exploring both AND nodes (which require all children to be satisfied) and OR nodes (where only one child needs to be satisfied).

### Key Features:

Solves intricate decision-making challenges efficiently.
Effectively navigates through both AND and OR nodes, allowing for nuanced decision paths.


## A* Algorithm 
The A* algorithm is one of the most widely used pathfinding and graph traversal techniques, celebrated for its efficiency and accuracy in locating the shortest path in a graph. It combines cost (g(n)) and heuristic estimates (h(n)) to inform its decisions.

### Key Features:

Utilizes both actual cost and heuristic estimates to determine the best path (f(n) = g(n) + h(n)).
Guarantees finding the shortest path if the heuristic used is admissible, meaning it never overestimates the true cost.


## Branch and Bound with Cost and Heuristic 
This implementation of the Branch and Bound algorithm incorporates both cost and heuristic values to effectively prune the search space. It systematically explores potential solutions while discarding paths that are unlikely to lead to an optimal solution.

### Key Features:

Combines cost evaluation and heuristic guidance for efficient pruning of the search space.
Reduces computational overhead by eliminating non-promising paths early in the search process.


## Branch and Bound with Dead Horse Principle (B&BwDHP.py)
This extended version of the Branch and Bound algorithm utilizes the Dead Horse Principle to prune unpromising paths early in the exploration. By implementing this principle, the algorithm avoids wasting resources on paths that are not viable.

### Key Features:

Early detection and pruning of non-promising paths, improving overall efficiency.
Focuses computational resources on the most promising paths to optimize the search.


## Beam Search 
The Beam Search algorithm is a heuristic search technique that limits exploration to a predefined number of the most promising nodes at each level. This approach is particularly useful in managing memory usage compared to exhaustive search methods.

### Key Features:

Employs a beam width parameter to control the size of the search space.
Achieves efficient memory usage by focusing on a limited set of potential solutions.


## Best-First Search 
Best-First Search is a greedy search algorithm that prioritizes the exploration of nodes based on their heuristic values. By selecting the most promising node first, it aims to find an optimal solution efficiently.

### Key Features:

Uses a priority queue to explore the node that appears most promising according to the heuristic.
Aims for efficiency in locating a solution by focusing on the most advantageous paths.


## Breadth-First Search (BFS.py)
The Breadth-First Search algorithm is a fundamental graph traversal technique that systematically explores all nodes at the present depth before moving on to the next level. It is particularly effective for unweighted graphs.

### Key Features:

Guarantees finding the shortest path in unweighted graphs due to its level-order exploration.
Suitable for tree and graph traversal problems, ensuring complete exploration.


## Beam Search Variant 
This variant of Beam Search employs a specific beam width to focus on heuristic-driven exploration. By constraining the search space, it enhances the efficiency of the search process.

### Key Features:

Focuses on efficient search while adhering to the constraints of a limited beam width.
Balances exploration breadth and memory efficiency.


## Standard Branch and Bound 
This is a classic implementation of the Branch and Bound algorithm, which systematically investigates all possible solutions while pruning suboptimal paths. It is widely used in optimization problems.

### Key Features:

Guarantees finding the optimal solution through systematic exploration.
Prunes non-promising paths to save computational time and resources.


## Depth-First Search
The Depth-First Search algorithm is a fundamental graph traversal method that delves as deep as possible along each branch before backtracking. It is useful in various search scenarios.

### Key Features:

Explores nodes deeply, making it effective for certain types of problems.
Simplicity and ease of implementation are key advantages.


## Hill Climbing 
The Hill Climbing algorithm is a local search technique that iteratively improves a solution by selecting the neighbor with the highest value. This method is often used in optimization problems but can be prone to getting stuck in local optima.

### Key Features:

Focuses on local improvement strategies for optimization.
May require additional mechanisms to escape local optima.


## Oracle Finding 
This simple oracle-finding algorithm aims to discover the best solution within a decision problem's search space. It systematically explores the search space to identify the optimal oracle.

### Key Features:

Explores decision problem spaces to identify optimal solutions efficiently.


## Alpha-Beta Pruning 
The Alpha-Beta Pruning algorithm is an optimization technique for the Minimax algorithm used in game theory. It reduces the number of nodes evaluated in the game tree, improving efficiency.

### Key Features:

Prunes branches that do not affect the final decision, allowing for faster evaluations.
More efficient than the standard Minimax approach, particularly in adversarial settings.
