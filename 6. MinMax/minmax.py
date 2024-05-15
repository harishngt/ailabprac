import math
 
def minimax (curDepth, nodeIndex,
             maxTurn, scores, 
             targetDepth):
 
    # base case : targetDepth reached
    if (curDepth == targetDepth): 
        return scores[nodeIndex]
     
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2, 
                    False, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                    False, scores, targetDepth))
     
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, 
                     True, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                     True, scores, targetDepth))

if __name__ == "__main__":
    scores = []
    n = 0
    while n < 6 or n > 8:  
        n = int(input("Enter Number of Players (6-8): "))
        if n >= 6 and n <= 8:
            break
        else:
            print("Please enter a number between 6 and 8.")
    for i in range(1, n + 1):  
        x = int(input(f"Player {i}'s Turn: "))
        scores.append(x)
    treeDepth = math.log(len(scores), 2)
    win_value = minimax(0, 0, True, scores,treeDepth)
    winner_index = scores.index(win_value) + 1  
    print(f"Player {winner_index} wins with choice {win_value}.")
