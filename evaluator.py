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
        return ((a < 0 and b < 0) or (a > 0  and b > 0))
    
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

        row = position[0]
        col = position[1]

        # To check whether I already encountered a piece in this diagonal or not
        # 0 -> Up-Left Diagonal
        # 1 -> Up-Right Diagonal
        # 2 -> Down-Left Diagonal
        # 3 -> Down-Right Diagonal
        diagEncounteredPiece = [False] * 4

        # Describe the direction of the movement for the bishop in the same
        # order as described above
        movDirection = [[-1, -1],
                     [-1, 1],
                     [1, -1],
                     [1, 1]]

        # A bishop can move at most 3 squares
        for i in range(1,4):
            # Check 4 directions of movement
            for j in range(4):
                newCol = col + i * movDirection[j][0]
                newRow = row + i * movDirection[j][1]

                # If I haven't found a piece yet in this direction and its inside the board
                if not diagEncounteredPiece[j] and self.__isInsideBoard(newRow, newCol):
                    # If the proposed square its occupied
                    if board[newRow][newCol] != 0:
                        # If the piece that occupies the square its from the opponent, then its a valid movement
                        if not self.__sameSign(board[row][col], board[newRow][newCol]):
                            validMovements.append((newRow, newCol))
                        diagEncounteredPiece[j] = True
                    else: # If not, just append the movement
                        validMovements.append((newRow, newCol))

        return validMovements

    def __getKnightValidMovements(self, position, board):
        validMovements = []

        row = position[0]
        col = position[1]


        # Describe the movements of the knight
        movements = [[-2, 1],
                     [-1, 2],
                     [1, 2],
                     [2, 1],
                     [2, -1],
                     [1, -2],
                     [-1, -2],
                     [-2, -1]]
        
        # Loop through all possible movements
        for move in movements:
            newRow = row + move[0]
            newCol = col + move[1]

            # For the knight we just need to check if the new square is valid and it is not occupied by a piece of the same color
            if self.__isInsideBoard(newRow, newCol) and not self.__sameSign(board[row][col], board[newRow][newCol]):
                validMovements.append((newRow, newCol))

        return validMovements

    def __getRookValidMovements(self, position, board):
        validMovements = []

        row = position[0]
        col = position[1]

        # Checks whether or not I have found a piece in this direction
        # 0 - Up
        # 1 - Right
        # 2 - Down
        # 3 - Left
        dirPieceEncountered = [False] * 4

        # Describe the direction of movement for the rook
        # The order is the same as described above
        movDirection = [[-1, 0],
                        [0, 1],
                        [1, 0],
                        [0, -1]]
        
        # The rook can move maximum 3 squares
        for i in range(1, 4):
            # Loop through all possible movements
            for j in range(4):
                newRow = row + i * movDirection[j][0]
                newCol = col + i * movDirection[j][1]

                if not dirPieceEncountered[j] and self.__isInsideBoard(newRow, newCol):
                    if board[newRow][newCol] != 0:
                        if not self.__sameSign(board[newRow][newCol], board[row][col]):
                            validMovements.append((newRow, newCol))
                        dirPieceEncountered[j] = True
                    else:
                        validMovements.append((newRow, newCol))

        return validMovements        

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

        row = position[0]
        col = position[1]

        oldBoard[row][col] = 0
        for newSquare in validMovementsSquares:
            # No se si esto haga una copia o solo sea una referencia
            prevPiece = oldBoard[newSquare[0]][newSquare[1]]
            oldBoard[newSquare[0]][newSquare[1]] = pieceCode
            if oldBoard == newBoard:
                return True
            
            oldBoard[newSquare[0]][newSquare[1]] = prevPiece

        oldBoard[row][col] = pieceCode
        return False

    def __wasValidMove(self, oldBoard, newBoard, color):
        pieces = [None] * 5

        # No puede haber errores porque es el tablero antiguo
        for i in range(4):
            for j in range(4):
                if self.__sameSign(oldBoard[i][j], color):
                    pieces[abs(oldBoard[i][j])] = (i, j)

        wasBoardFound = False
        for i in range(1, len(pieces)):
            if pieces[i] is not None:
                wasBoardFound = self.__compareWithBoardsWithMovement(i, pieces[i], oldBoard, newBoard, color)
            else:
                wasBoardFound = self.__compareWithBoardsWithNewPiece(i, oldBoard, newBoard)

            if wasBoardFound:
                return True
            
        return False

    # Function to check whether a movement was a capture or not
    # For a movement to be classified as a capture, 2 conditions have to occur
    # 1. Only 2 squares changed value
    # 2. One square has to change from used to empty and the other from used to used with different color    
    def __wasCapture(self, oldBoard, newBoard, color):
        changedSquares = []

        for i in range(4):
            for j in range(4):
                if oldBoard[i][j] != newBoard[i][j]:
                    changedSquares.append((i, j))

        if len(changedSquares) != 2:
            return False
        
        def areChangesFromCapture(row1, col1, row2, col2):
            return (newBoard[row1][col1] == 0 and newBoard[row2][col2] == oldBoard[row1][col1])
        
        return (areChangesFromCapture(changedSquares[0][0], changedSquares[0][1], changedSquares[1][0], changedSquares[1][1]) 
                or areChangesFromCapture(changedSquares[1][0], changedSquares[1][1], changedSquares[0][0], changedSquares[0][1]))


    def __isWinningPosition(self, board, player):
        pass

    def __reverseBoard(self, board):
        pass

    def __playTurn(self, player, captures, color):
        newBoard = self.player.play(self.board)
        
        if self.__wasValidMove(self.board, newBoard, color):
            if self.__wasCapture(self.board, newBoard, color):
                pass
        else:
            print(player.name, "made an illegal move. Loses automatically")
            print(self.board)
            print(newBoard)

            return False

    def __startGame(self):
        while self.currentTurn < self.maxTurns:
            self.__playTurn(self.whitePlayer)

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