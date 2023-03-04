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

class Errors:
    def __init__(self):
        self.UNKNOWN_PIECE = "There is an unknown piece on the board"
        self.REPEATED_PIECE = "There is a piece that appears more than once on the board"

    @staticmethod
    def UnknownPiece(self):
        return self.UNKNOWN_PIECE


class TTCEvaluator:
    def __init__(self, whitePlayer, blackPlayer):
        self.whitePlayer = whitePlayer
        self.blackPlayer = blackPlayer

        self.currentTurn = 0
        self.whiteCaptures = 0
        self.blackCaptures = 0
        
        # Hacia arriba
        self.whitePawnDirection = -1
        self.blackPawnDirection = -1

        self.maxCaptures = 0
        self.maxTurns = 0
        self.board = None
        
    def __sameSign(a, b):
        return (a < 0 and b < 0)
    
    def __isInsideBoard(row, col):
        return (row >= 0 and row < 4 and col >= 0 and col < 4)

    def __updatePawnDirection(self, board, color):
        pass

    def __getPawnValidMovements(self, position, board, color):
        validMovements = []
        yMovement = self.whitePawnDirection if color == 1 else self.blackPawnDirection
        
        row = position[0]
        col = position[1]

        # Move 1 to the front
        newRow = row + yMovement
        if self.__isInsideBoard(newRow, col) and board[newRow][col] == 0:
            validMovements.append((newRow, col))

        # Attack to the left
        newCol = col - 1
        if self.__isInsideBoard(newRow, newCol) and board[newRow][newCol] != 0 and not self.__sameSign(board[newRow][newCol], board[row][col]):
            validMovements.append((newRow, newCol))

        # Attack to the right
        newCol = col + 1
        if self.__isInsideBoard(newRow, newCol) and board[newRow][newCol] != 0 and not self.__sameSign(board[newRow][newCol], board[row][col]):
            validMovements.append((newRow, newCol))

        return validMovements
    
    def __getBishopValidMovements(self, position, board):
        validMovements = []


    def __getValidMovements(self, pieceCode, position, board, color):
        if pieceCode == 1:
            return self.__getPawnValidMovements(position, board, color)
        elif pieceCode == 2:
            return self.__getBishopValidMovements(position, board)
        elif pieceCode == 3:
            return self.__getKnightValidMovements(position, board)
        else:
            return self.__getRookValidMovements(position, board)


    def __compareWithBoardsWithNewPiece(self, pieceCode, oldBoard, newBoard):
        for i in range(4):
            for j in range(4):
                if oldBoard[i][j] == 0:
                    oldBoard[i][j] = pieceCode

                    if oldBoard == newBoard:
                        return True
                    
                    oldBoard[i][j] = 0

        return False
    
    def __compareWithBoardsWithMovement(self, pieceCode, position, oldBoard, newBoard, color):
        validMovementsSquares = self.__getValidMovements(pieceCode, position, oldBoard, color)

        oldBoard[position[0]][position[1]] = 0
        for newSquare in validMovementsSquares:
            # No se si esto haga una copia o solo sea una referencia
            prevPiece = oldBoard[newSquare[0]][newSquare[1]]
            oldBoard[newSquare[0]][newSquare[1]] = pieceCode
            if oldBoard == newBoard:
                return True
            
            oldBoard[newSquare[0]][newSquare[1]] = prevPiece

        oldBoard[position[0]][position[1]] = pieceCode
        return False




    def __wasValidMove(self, oldBoard, newBoard, color):
        pieces = [None] * 5

        # No puede haber errores porque es el tablero antiguo
        for i in range(4):
            for j in range(4):
                if self.__sameSign(oldBoard[i][j], color):
                    pieces[abs(oldBoard[i][j])] = (i, j)


        for i in range(1, len(pieces)):
            if pieces[i] is not None:
                self.__compareWithBoardsWithMovement(i, pieces[i], oldBoard, newBoard, color)
            else:
                self.__compareWithBoardsWithNewPiece(i, oldBoard, newBoard)
            


    def __isWinPosition(self, board, player):
        pass

    def __reverseBoard(self, board):
        pass

    def __playTurn(self, player, captures, color):
        newBoard = self.player.play(self.board)
        
        if self.__wasValidMove(self.board, newBoard, color):
            pass
        else:
            print(player.name, "made an illegal move. Loses automatically")
            return False

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
print([10, 11, 2, 3, 4] * -1)