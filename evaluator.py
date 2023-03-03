"""
Tic-Tac-Chec Evaluator
Program to run and evaluate Tic-Tac-Chess analysis modules. 

This program makes two modules compete against each other several times and
gather statics about the number of wins, losses and draws for each program.
It also checks for legal and illegal moves as well as for winning and losing positions. 

The set of rules that this evaluator checks are as follows:
    1. Tic-Tac-Chess is played by 2 players on a 4x4 chess board. The game starts with an empty board, each player taking a contrary side, facing each other.
    
    2. Each player has a set of pieces, white and black respectively, that contains: 1 rook, 1 knight, 1 bishop and 1 pawn. 
    Each piece moves the same as in regular chess. The only exception is when the pawn reaches the opponent's side of the board, in which case it reverses direction.

    3. A new piece can only be positioned on an empty square, it cannot capture pieces while entering the board.

    4. For the first 3 turns, each player can only place new pieces on the board. In this initial stage, tha players cannot move or capture any piece that is already on the board.

    5. Starting on the 4th turn, the player can move or capture pieces from his/her opponent. When a piece is captured, it is returned to the owner, who can
    place it inmediately on his/her next turn.

    6. There is a limit on the number of times a player can capture an opponent's piece. After that limit is reached by the player, he/she can no longer capture pieces.

    7. The game is finished when a player is able to align his/her four pieces horizontally, vertically or diagonally.

    8. There is a limit of turns that can be played. If that limit is reached and no player has won, the game would be considered a draw.

"""
from module import TTCPlayer


class TTCEvaluator:
    def __init__(self, whitePlayer, blackPlayer):
        self.whitePlayer = whitePlayer
        self.blackPlayer = blackPlayer

        self.currentTurn = 0
        self.whiteCaptures = 0
        self.blackCaptures = 0

        self.maxCaptures = 0
        self.maxTurns = 0
        

    def __wasValidMove(self, oldBoard, newBoard):
        pass

    def __isWinPosition(self, board, player):
        pass

    def __reverseBoard(self, board):
        pass

    def __playTurn(self):
        pass

    def __startGame(self):
        while self.currentTurn < self.maxTurns:
            self.__playTurn()

    def runAnalysis(self, noGames, maxCaptures, maxTurns):
        self.maxCaptures = maxCaptures
        self.maxTurns = maxTurns

        self.board = [[0] * 4 for _ in range(4)]

        for i in range(noGames):
            self.__startGame()



whitePlayer = TTCPlayer([10, 2, 3, 4])
blackPlayer = TTCPlayer([-10, -2, -3, -4])

evaluator = TTCEvaluator(whitePlayer, blackPlayer)

#evaluator.runAnalysis(100, 8, 150)


print([[0] * 4 for _ in range(4)])