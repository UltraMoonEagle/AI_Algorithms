import math

def alpha_beta_pruning(depth, node_index, is_max_player, values, max_depth, alpha=-math.inf, beta=math.inf):
    
    if depth == max_depth:
        print(f"Reached leaf node at depth {depth}, returning value: {values[node_index]}")
        return values[node_index]

    if is_max_player:
        max_eval = -math.inf
        print(f"Maximizing player at depth {depth}")

        for i in range(2): 
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, max_depth, alpha, beta)
            print(f"Maximizing player at depth {depth}, comparing value: {eval} with current max: {max_eval}")
            max_eval = max(max_eval, eval)
            alpha = max(alpha, max_eval)

            if beta <= alpha:
                print(f"Pruning at depth {depth} with alpha: {alpha} and beta: {beta}")
                break

        print(f"Maximizing player at depth {depth}, best value: {max_eval}")
        return max_eval
    else:
        min_eval = math.inf
        print(f"Minimizing player at depth {depth}")

        for i in range(2):  
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, max_depth, alpha, beta)
            print(f"Minimizing player at depth {depth}, comparing value: {eval} with current min: {min_eval}")
            min_eval = min(min_eval, eval)
            beta = min(beta, min_eval)

            if beta <= alpha:
                print(f"Pruning at depth {depth} with alpha: {alpha} and beta: {beta}")
                break

        print(f"Minimizing player at depth {depth}, best value: {min_eval}")
        return min_eval


if __name__ == "__main__":
    
    terminal_values = [3, 5, 6, 9, 1, 2, 0, -1]
    depth_limit = 3  

    result = alpha_beta_pruning(0, 0, True, terminal_values, depth_limit)
    print(f"Optimal value: {result}")
