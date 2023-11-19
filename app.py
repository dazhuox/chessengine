import chess_engine as ce
import chess as ch
from flask import Flask, render_template, request

app = Flask(__name__)

class Main:

    def __init__(self):
        self.board = ch.Board()
        self.choose = ""

    def timer(self):
        print("you win or lose")

    #play human move
    def playHumanMove(self):
        try:
            print(self.board.legal_moves)
            print("""To undo your last move, type "undo".""")
            #get human move
            play = input("Your move: ")
            if (play=="undo"):
                self.board.pop()
                self.board.pop()
                self.playHumanMove()
                return
            self.board.push_san(play)
        except:
            self.playHumanMove()

    #play engine move
    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())

    def changeMaxDepth(self):
        print(self.board.legal_moves.count())
        if(self.choose == "Beginner"):
            if self.board.legal_moves.count() > 50:
                return 2
            elif len(self.board.piece_map()) < 6:
                return 2
            else:
                return 2
        elif(self.choose == "Intermediate"):
            if self.board.legal_moves.count() > 50:
                return 3
            elif len(self.board.piece_map()) < 6:
                return 6
            else:
                return 4
        elif(self.choose == "Hard"):
            if self.board.legal_moves.count() > 50:
                return 4
            elif len(self.board.piece_map()) < 6:
                return 9
            else:
                return 5
        self.board.fullmove_number
        self.board.legal_moves.count()

    #start a game
    def startGame(self):
        #get human player's color
        color=None
        while(color!="b" and color!="w"):
            color = input("""Play as (type "b" or "w"): """)
        maxDepth=None
        time=None
        while(self.choose != "Beginner" and self.choose != "Hard"
        and self.choose != "Intermediate"):
            self.choose = input("Choose a difficulty (Beginner, Intermediate, and Hard): ")
        while(isinstance(time, float)==False):
            time = float(input("Timer (in minutes per player): "))
        if color=="b":
            # realTime = th.Timer(time,self.timer)
            # botTime = th.Timer(time,self.timer)
            # botTime.start()
            while (self.board.is_checkmate()==False):
                maxDepth = self.changeMaxDepth()
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            print(self.board)
            print(self.board.outcome())
        elif color=="w":
            # realTime = th.Timer(time,self.timer)
            # botTime = th.Timer(time,self.timer)
            while (self.board.is_checkmate()==False):
                print(self.board)
                self.playHumanMove()
                print(self.board)
                maxDepth = self.changeMaxDepth()
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.BLACK)
            print(self.board)
            print(self.board.outcome())
        #reset the board
        self.board.reset
        #start another game
        self.startGame()

#create an instance and start a game
# newBoard= ch.Board()
# game = Main(newBoard,"")
# bruh = game.startGame()

game = Main()

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', board=game.board, choose=game.choose)

@app.route('/make_move', methods=['POST'])
def make_move():
    if request.method == 'POST':
        move = request.form.get('move')
        game.play_human_move(move)
        game.play_engine_move()

    return render_template('index.html', board=game.board, choose=game.choose)

if __name__ == '__main__':
    app.run(debug=True)