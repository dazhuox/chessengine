import chess as ch
import random


class Engine:

    def __init__(self,board,depth,color):
        self.board = board
        self.depth = depth
        self.color = color

    def get_best_move(self):
        return self.engine(None, 1)

    def evalfunct(self):
        compt = 0
        for i in range(64):
            compt += self.square_res_pts(ch.SQUARES[i])
        compt += self.mate_opportunity() + self.opening() + 0.001 * random.random() #alpha pruning reasons


    def mate_opportunity(self):
        #if someone is getting checkmated, then there are no legal moves allowed
        if self.board.legal_moves.count() == 0:
            if (self.board.turn == self.color):
                return -999
            else:
                return 999
        else:
            return 0
        
    #Takes a square as input and returns the corresponding han's berliner's system value of it's resident

    #pawn is 1
    #knight is 3.2
    #bishop is 3.33
    #rook is 5.1
    #queen is 8.8

    def square_res_pts(self, square):
        piece_value = 0
        if(self.board.piece_type_at(square) == ch.PAWN):
            piece_value = 1
        if(self.board.piece_type_at(square) == ch.KNIGHT):
            piece_value = 3.2
        if(self.board.piece_type_at(square) == ch.BISHOP):
            piece_value = 3.33
        if(self.board.piece_type_at(square) == ch.QUEEN):
            piece_value = 8.8
        if(self.board.piece_type_at(square) == ch.ROOK):
            piece_value = 5.1

    def opening(self):
        if (self.board.fullmove_Number < 10):
            if self.board.turn == self.color:
                return 1/30 * self.board.legal_moves.count()
            else:
                return -1/30 * self.board.legal_moves.count()
            
        else:
            return 0

    def engine(self, candidate, depth):
        if (depth == self.depth or self.board.legal_moves.count() == 0):
            return self.evalfunct()
        
        else:
            #get list of legal movese of the current position
            move_list = list(self.board.legal_moves)

            #initialize new_candidate
            new_candidate = None

            if depth % 2 != 0:
                new_candidate = float("-inf")
            else:
                new_candidate = float("inf")

            for i in move_list:
                #play the move i
                self.board.push(i)

                #get the value of move i
                value = self.engine(new_candidate, depth + 1)

                #basic minmax algorithm:

                #if maximizing (ai's turn)
                if(value > new_candidate and depth % 2 != 0):
                    new_candidate = value

                    if(depth == 1):
                        move = i

                #if minimizing (human's turn)
                elif(value < new_candidate and depth % 2 == 0):
                    new_candidate = value

                # alpha-beta pruning cuts

                # (if previous move was made by the ai)
                if (candidate != None and value < candidate and depth % 2 == 0):
                    self.board.pop()
                    break

                # (if previous move was made by the human)
                if (candidate != None and value > candidate and depth % 2 != 0):
                    self.board.pop()
                    break

                #undo last move 
                self.board.pop()

        if (depth > 1):
            #return the value of the node in the tree
            return new_candidate
        else:
            return move

