#defining a function with the starting position, how many layers do we want to search
def minimax(position, depth, maximizingplayer):
    if depth == 0:
        return position
        #stop the game because it means we have reached the final state
        #simply return the current position
    
    #if its currently the turn of white to move
    #want to find the highest possible eval from this pos
    if maximizingplayer == True:
        maxeval = -999999
        for move in 'list of next moves based off current position':
            eval = minimax(move , depth - 1, False)
            maxeval = max(maxeval, eval)
        
        return maxeval
    
    else:
        mineval = 9999999
        for move in 'list of next moves based off current position':
            eval = minimax(move , depth - 1, True)
            mineval = min(maxeval, eval)
        
        return mineval
    
#example with initial call:

minimax('currentPos', 3, True)


    