#defining a function with the starting position, how many layers do we want to search
def minimax(position, depth, maximizingplayer,alpha,beta):
    if depth == 0:
        return position
        #stop the game because it means we have reached the final state
        #simply return the current position
    
    #if its currently the turn of white to move
    #want to find the highest possible eval from this pos
    if maximizingplayer == True:
        maxeval = -999999
        for move in 'list of next moves based off current position':
            eval = minimax(move , depth - 1, False,alpha,beta)
            maxeval = max(maxeval, eval)
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
        
        return maxeval
    
    else:
        mineval = 9999999
        for move in 'list of next moves based off current position':
            eval = minimax(move , depth - 1, True,alpha,beta)
            mineval = min(maxeval, eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        
        return mineval
    
#example with initial call:

minimax('currentPos', 3, True,-99999,999999)
#alpha is initialized as the worst possible value for white
#beta is ini as worst possible for black