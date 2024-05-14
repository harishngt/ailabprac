MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    values = []
    n = 0
    while n < 6 or n > 8:  
        n = int(input("Enter Number of Players (6-8): "))
        if n >= 6 and n <= 8:
            break
        else:
            print("Please enter a number between 6 and 8.")
    for i in range(1, n + 1):  
        x = int(input(f"Player {i}'s Turn: "))
        values.append(x)
    win_value = minimax(0, 0, True, values, MIN, MAX)
    winner_index = values.index(win_value) + 1  
    print(f"Player {winner_index} wins with choice {win_value}.")
