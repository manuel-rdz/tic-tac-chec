import unittest

from evaluator import TTCEvaluator, PlayerWrapper
from module import TTCPlayer

class TestEvaluator(unittest.TestCase):
    def test_updatePawnDirectionWhite(self):
        eval = TTCEvaluator()
        player = PlayerWrapper(TTCPlayer([1, 2, 3, 4]), 1)

        board1 = [[-1,0,1,0],
                  [0,0,-2,0],
                  [0,4,0,0],
                  [3,0,2,0]]
        
        board2 = [[0,-1,0,0],
                  [0,0,0,-4],
                  [0,0,0,0],
                  [0,3,0,1]]


        eval._TTCEvaluator__updatePawnDirection(board1, player)
        self.assertEqual(player.pawnDirection, 1)

        eval._TTCEvaluator__updatePawnDirection(board2, player)
        self.assertEqual(player.pawnDirection, -1)

    def test_updatePawnDirectionBlack(self):
        eval = TTCEvaluator()
        player = PlayerWrapper(TTCPlayer([-1, -2, -3, -4]), -1)

        board1 = [[1,0,-1,0],
                  [0,0,0,0],
                  [0,-3,-4,0],
                  [0,3,4,0]]
        
        board2 = [[0,-3,4,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,1,0,-1]]


        eval._TTCEvaluator__updatePawnDirection(board1, player)
        self.assertEqual(player.pawnDirection, 1)

        eval._TTCEvaluator__updatePawnDirection(board2, player)
        self.assertEqual(player.pawnDirection, -1)

    def test_getPawnValidMovements(self):
         eval = TTCEvaluator()

         boards = [ [[1,0,0,0],
                    [0,-3,0,0],
                    [0,0,0,0],
                    [0,0,0,0]],

                    [[0,0,0,0],
                     [0,3,-4,-1],
                     [0,1,0,0],
                     [0,0,0,0]],

                    [[0,0,0,0],
                     [0,-1,0,0],
                     [-2,1,-4,0],
                     [0,0,0,0]],
                     
                    [[0,0,-4,2],
                     [0,0,-1,0],
                     [0,0,0,0],
                     [0,0,0,0]],
                    [[0,0,0,0],
                     [0,0,0,-1],
                     [0,0,0,0],
                     [0,0,0,0]]
                   ]
         
         positions = [(0, 0), (2, 1), (1, 1), (1, 2), (1, 3)]
         pawnDirections = [1, -1, 1, -1, 1]
         validPositions = [[(1, 1), (1, 0)], 
                           [(1, 2)],
                           [],
                           [(0,3)],
                           [(2, 3)]]

         for i in range(len(positions)):
            ans = eval._TTCEvaluator__getPawnValidMovements(positions[i], boards[i], pawnDirections[i])
            self.assertEqual(set(ans), set(validPositions[i]))

    def test_getKnightValidMovements(self):
        eval = TTCEvaluator()
        boards = [ [[1, 0,-3, 0],
                    [0,-2, 0, 0],
                    [0, 3, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,2,-3,-1],
                     [0,1, 0, 0],
                     [0,0, 0, 4]],

                    [[ 0, 2, 0,0],
                     [ 0,-1, 0,0],
                     [-2, 1,-3,0],
                     [ 0, 0, 0,0]],
                     
                    [[0,0,-3,2],
                     [0,0,-1,0],
                     [0,1, 0,0],
                     [0,0, 0,0]],

                    [[0, 0,0, 0],
                     [0,-2,0,-1],
                     [0, 0,0, 0],
                     [3, 0,0, 0]]
                   ]
         
        positions = [(2, 1), (1, 2), (2, 2), (0, 2), (3, 0)]
        validPositions = [[(0, 2), (1, 3), (3, 3)], 
                           [(0, 0), (2, 0), (3, 1), (3, 3)],
                           [(1, 0), (3, 0), (0, 1), (0, 3)],
                           [(1,0), (2, 1), (2, 3)],
                           [(1, 1), (2, 2)]]

        for i in range(len(positions)):
            ans = eval._TTCEvaluator__getKnightValidMovements(positions[i], boards[i])
            self.assertEqual(set(ans), set(validPositions[i]))

    def test_getBishopValidMovements(self):
        eval = TTCEvaluator()
        boards = [ [[1, 0,-3, 0],
                    [0,-2, 0, 0],
                    [0, 3, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,2,-3,-1],
                     [0,1, 0, 0],
                     [0,0, 0, 4]],

                    [[ 0, 4, 0,0],
                     [ 0,-1, 0,-2],
                     [-4, 1,-3,0],
                     [ 0, 2, 0,0]],
                     
                    [[ 0,0,-4,3],
                     [-2,0,-1,0],
                     [ 0,1, 0,0],
                     [ 0,0, 2,0]],

                    [[0,  0, 0, 4],
                     [0, -3,-1, 0],
                     [0, -2, 0, 0],
                     [1,  0, 0, 0]]
                   ]
         
        positions = [(1, 1), (1, 1), (3, 1), (3, 2), (2, 1)]
        validPositions = [[(0, 0), (2, 2), (2, 0)], 
                           [(0, 0), (2, 0), (0, 2), (2, 2)],
                           [(2, 0), (2, 2)],
                           [(2, 3)],
                           [(1, 0), (3, 0), (3, 2)]]

        for i in range(len(positions)):
            ans = eval._TTCEvaluator__getBishopValidMovements(positions[i], boards[i])
            self.assertEqual(set(ans), set(validPositions[i]))

    def test_getRookValidMovements(self):
        eval = TTCEvaluator()
        boards = [ [[1, 0,-4, 0],
                    [0,-3, 0, 0],
                    [0, 4, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,3,-4,-1],
                     [0,1, 0, 0],
                     [0,0, 0, 4]],

                    [[ 0, 2,-4,0],
                     [ 0,-1, 0,-3],
                     [-2, 1, 4,0],
                     [ 0, 3, 0,0]],
                     
                    [[ 0,0,-4,2],
                     [-3,0,-1,0],
                     [ 0,1, 0,0],
                     [ 0,0, 3,0]],

                    [[0, 0, 0,4],
                     [0,-2,-1,0],
                     [0,-3, 0,0],
                     [1, 0, 0,0]]
                   ]
         
        positions = [(2, 1), (1, 2), (2, 2), (0, 2), (0, 3)]
        validPositions = [[(1, 1), (2, 2), (3, 1), (2, 0), (2, 3)], 
                           [(0, 2), (2, 2), (1, 1), (3, 2)],
                           [(1, 2), (2, 3), (3, 2), (0, 2)],
                           [(0, 3), (0, 1), (0, 0)],
                           [(1, 3), (0, 2), (2, 3), (0, 1), (3, 3), (0, 0)]]

        for i in range(len(positions)):
            ans = eval._TTCEvaluator__getRookValidMovements(positions[i], boards[i])
            self.assertEqual(set(ans), set(validPositions[i]))

    def test_compareWithBoardsWithNewPiece(self):
        eval = TTCEvaluator()

        oldBoards = [ 
                   [[1, 0, 0, 0],
                    [0,-3, 0, 0],
                    [0, 4, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,3,-4,-1],
                     [0,0, 0, 0],
                     [0,0, 0, 4]],

                    [[ 0, 2,-4,0],
                     [ 0,-1, 0,0],
                     [-2, 1, 4,0],
                     [ 0, 3, 0,0]],
                     
                    [[ 0,0,-4,0],
                     [-3,0,-1,0],
                     [ 0,1, 0,0],
                     [ 0,0, 3,0]],

                    [[0, 0, 0,4],
                     [0,0,-1,0],
                     [0,-3, 0,0],
                     [1, 0, 0,0]]
                   ]

        newBoards = [
                    [[1, 0,-4, 0],
                    [0,-3, 0, 0],
                    [0, 4, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,3, 0,-1],
                     [0,1,-4, 0],
                     [0,0, 0, 4]],

                    [[ 0, 2,-4,0],
                     [ 0,-1, 0,-3],
                     [-2, 1, 4,0],
                     [ 0, 3, 0,0]],
                     
                    [[ 0,0,-4,2],
                     [-3,0,-1,0],
                     [ 0,0, 0,0],
                     [ 0,0, 3,1]],

                    [[0, 0, 0,4],
                     [0,-2,-1,0],
                     [0,-3, 0,0],
                     [1, 0, 0,0]]
                   ]
        
        piecesCode = [-4, 1, -3, 2, -2]
        result = [True, False, True, False, True]

        for i in range(len(piecesCode)):
            ans = eval._TTCEvaluator__compareWithBoardsWithNewPiece(piecesCode[i], oldBoards[i], newBoards[i])
            self.assertEqual(ans, result[i])

    def test_compareWithBoardsWithMovement(self):
        eval = TTCEvaluator()

        oldBoards = [ 
                   [[1, 0, 0, 0],
                    [0,-3, 0, 0],
                    [0, 4, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,3,-4,-1],
                     [0,0, 0, 0],
                     [0,0, 0, 4]],

                    [[ 0, 2,-4,0],
                     [ 0,-1, 0,0],
                     [-2, 1, 4,0],
                     [ 0, 3, 0,0]],
                     
                    [[ 0,0,-4,0],
                     [-3,0,-1,0],
                     [ 0,1, 0,0],
                     [ 0,0, 3,0]],

                    [[0, 0, 0,0],
                     [0, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 0, 4,0]],

                    [[0, 0, 0,0],
                     [4, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 0, 4,0]],

                    [[0, 2, 0,0],
                     [0, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 3, 4,0]]
                   ]
        newBoards = [ 
                   [[0, 0, 0, 0],
                    [1,-3, 0, 0],
                    [0, 4, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,-4,0,-1],
                     [0,0, 0, 0],
                     [0,0, 0, 4]],

                    [[ 0, 2,-4,0],
                     [ 0,-1, 3,0],
                     [-2, 1, 4,0],
                     [ 0, 0, 0,0]],
                     
                    [[ 0,0,-4,0],
                     [ 1,0,-1,0],
                     [ 0,0, 0,0],
                     [ 0,0, 3,0]],

                    [[0,0, 0,0],
                     [0,0,-1,0],
                     [0,0, 0,0],
                     [1,0,-2,0]],

                    [[0, 0, 3,0],
                     [4, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 0, 4,0]],

                    [[0, 2, 0, 0],
                     [0, 0,-1, 0],
                     [0,-2, 0,-4],
                     [1, 3, 4, 0]]
                   ]
        
        piecesCodes = [1, -4, 3, 1, -2, 4, -1]
        positions = [(0,0), (1, 2), (3, 1), (2, 1), (2, 1), (1, 0), (1, 2)]
        players = [PlayerWrapper(TTCPlayer([1,2,3,4]), 1), 
                   PlayerWrapper(TTCPlayer([-1,-2,-3,-4]), -1),
                   PlayerWrapper(TTCPlayer([1,2,3,4]), 1),
                   PlayerWrapper(TTCPlayer([1,2,3,4]), 1),
                   PlayerWrapper(TTCPlayer([-1,-2,-3,-4]), -1),
                   PlayerWrapper(TTCPlayer([1,2,3,4]), 1),
                   PlayerWrapper(TTCPlayer([-1,-2,-3,-4]), -1),]
        results = [True, True, True, True, True, False, False]
        
        players[0].pawnDirection = 1

        for i in range(len(piecesCodes)):
            ans = eval._TTCEvaluator__compareWithBoardsWithMovement(piecesCodes[i], positions[i], oldBoards[i], newBoards[i], players[i])
            self.assertEqual(ans, results[i])

    def test_wasValidMove(self):
        eval = TTCEvaluator()

        oldBoards = [ 
                   [[1, 0, 0, 0],
                    [0,-3, 0, 0],
                    [0, 4, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,3,-4,-1],
                     [0,0, 0, 0],
                     [0,0, 0, 4]],

                    [[ 0, 2,-4,0],
                     [ 0,-1, 0,0],
                     [-2, 1, 4,0],
                     [ 0, 3, 0,0]],
                     
                    [[ 0,0,-4,0],
                     [-3,0,-1,0],
                     [ 0,1, 0,0],
                     [ 0,0, 3,0]],

                    [[0, 0, 0,0],
                     [0, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 0, 4,0]],

                    [[0, 0, 0,0],
                     [4, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 0, -4,0]],

                    [[0, 2, 0,0],
                     [0, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 3, 4,0]]
                   ]
        newBoards = [ 
                   [[1, 0, 2, 0],
                    [0,-3, 0, 0],
                    [0, 4, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,3,-2,-1],
                     [0,0, 0, 0],
                     [0,0, 0, 4]],

                    [[ 0, 2,-4,0],
                     [ 0,-1, 0,0],
                     [-2, 1, 3,0],
                     [ 0, 0, 0,0]],
                     
                    [[ 0,0,-4,0],
                     [-3,1,-1,0],
                     [ 0,0, 0,0],
                     [ 0,0, 3,0]],

                    [[0,-4, 0,0],
                     [0, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 0, 4,0]],

                    [[0, 0, 0,0],
                     [4, 0,-1,0],
                     [0,-2, 0,0],
                     [-4, 0,0,0]],

                    [[0, 2, 0, 0],
                     [0, 0, 0, 0],
                     [0,-2, 0,-1],
                     [1, 3, 4, 0]]
                   ]

        players = [PlayerWrapper(TTCPlayer([1,2,3,4]), 1), 
                   PlayerWrapper(TTCPlayer([-1,-2,-3,-4]), -1),
                   PlayerWrapper(TTCPlayer([1,2,3,4]), 1),
                   PlayerWrapper(TTCPlayer([1,2,3,4]), 1),
                   PlayerWrapper(TTCPlayer([-1,-2,-3,-4]), -1),
                   PlayerWrapper(TTCPlayer([-1,-2,-3,-4]), -1),
                   PlayerWrapper(TTCPlayer([-1,-2,-3,-4]), -1)]
        
        players[-1].pawnDirection = 1

        results = [True, False, False, True, True, True, False]

        for i in range(len(results)):
            ans = eval._TTCEvaluator__wasValidMove(oldBoards[i], newBoards[i], players[i])
            self.assertEqual(ans, results[i])

    def test_wasCapture(self):
        eval = TTCEvaluator()
        oldBoards = [ 
                   [[1, 0, 0, 0],
                    [0,-3, 0, 0],
                    [0, 4, 0, 0],
                    [0, 0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,3,-4,-1],
                     [0,0, 0, 0],
                     [0,0, 0, 4]],

                    [[ 0, 2,-4,0],
                     [ 0,-1, 0,0],
                     [-2, 1, 4,0],
                     [ 0, 3, 0,0]],
                     
                    [[ 0,0,-4,0],
                     [-3,0,-1,0],
                     [ 0,1, 0,0],
                     [ 0,0, 3,0]],

                    [[0, 0, 0,0],
                     [0, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 0, 4,0]],

                    [[0, 0, 0,0],
                     [4, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 0, -4,0]],

                    [[0, 2, 0,0],
                     [0, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 3, 4,0]]
                   ]
        
        newBoards = [ 
                   [[1,0, 0, 0],
                    [0,4, 0, 0],
                    [0,0, 0, 0],
                    [0,0, 0,-1]],

                    [[0,0, 0, 0],
                     [0,3,-4, 0],
                     [0,0, 0,-1],
                     [0,0, 0, 4]],

                    [[ 0, 2,-4,0],
                     [ 0,-1, 0,0],
                     [-2, 1, 4,3],
                     [ 0, 0, 0,0]],
                     
                    [[ 0,0,-4,0],
                     [-3,0, 1,0],
                     [ 0,0, 0,0],
                     [ 0,0, 3,0]],

                    [[0, 0, 0,0],
                     [0, 0,-1,0],
                     [0, 0, 0,0],
                     [-2,0, 4,0]],

                    [[0, 0, 0,0],
                     [4, 0,-1,0],
                     [0,-2, 0,0],
                     [-4, 0, 0,0]],

                    [[0, 2, 0,-3],
                     [0, 0,-1,0],
                     [0,-2, 0,0],
                     [1, 3, 4,0]]
                   ]
        
        results = [True, False, False, True, True, True, False]

        for i in range(len(results)):
            ans = eval._TTCEvaluator__wasCapture(oldBoards[i], newBoards[i])
            self.assertEqual(ans, results[i])

    def test_isWinningPosition(self):
        eval = TTCEvaluator()
        boards = [ 
                   [[1,0, 0, -2],
                    [0,2, -3, 0],
                    [0,-4, 3, 0],
                    [0, 0, -1,4]],

                    [[-4,0, 0, 0],
                     [0,-2,1,-1],
                     [0,0, -3, 0],
                     [0,2, 0, 4]],

                    [[ 1, 2, 4,0],
                     [ 0,-1, 0,0],
                     [-2, 0, 0,0],
                     [ 0, 3, 0,0]],
                     
                    [[ 0,0,-4,0],
                     [-3,0,-1,0],
                     [ 0,0, 0,0],
                     [ 2,4, 1,3]],

                    [[0, 1, 0,-2],
                     [0, 0,-3,0],
                     [0,-4, 0,0],
                     [-1, 0, 4,0]],

                    [[ 0, 0, 2,0],
                     [-4, 0, 3,0],
                     [ 0,-2, 4,0],
                     [-1, 0, 1,0]],

                    [[1, 2, 0,0],
                     [0,-2,-1,0],
                     [0, 2,-3,0],
                     [0, 3,-4,4]]
                   ]
        
        results = [True, False, False, True, True, True, False]
        piecesColor = [1, -1, 1, 1, -1, 1, 1]

        for i in range(len(results)):
            ans = eval._TTCEvaluator__isWinningPosition(boards[i], piecesColor[i])
            self.assertEqual(ans, results[i])

    def test_rotateBoard(self):
        eval = TTCEvaluator()

        boards = [ 
                   [[4, -1, 0, 0],
                   [0, 3, -4, 0],
                   [0, -3, 2, 0],
                   [-2, 0, 0, 1]],

                    [[-4,0, 0, 0],
                     [0,-2,1,-1],
                     [0,0, -3, 0],
                     [0,2, 0, 4]],

                    [[ 1, 2, 4,0],
                     [ 0,-1, 0,0],
                     [-2, 0, 0,0],
                     [ 0, 3, 0,0]],
                     
                    [[ 0,0,-4,0],
                     [-3,0,-1,0],
                     [ 0,0, 0,0],
                     [ 2,4, 1,3]],
                   ]
        
        results = [ 
                   [[1,0,0,-2],
                    [0, 2,-3,0],
                    [0, -4,3,0],
                    [0,0,-1,4]],

                    [[4,0,2,0],
                     [0,-3,0,0],
                     [-1,1,-2,0],
                     [0,0,0,-4]],

                    [[0,0,3,0],
                     [ 0,0,0,-2],
                     [0,0,-1,0],
                     [0,4,2,1]],
                     
                    [[3,1,4,2],
                     [0,0,0,0],
                     [0,-1,0,-3],
                     [0,-4,0,0]],
                   ]
        
        for i in range(len(results)):
            ans = eval._TTCEvaluator__rotateBoard(boards[i])
            self.assertEqual(ans, results[i])
        

if __name__ == '__main__':
    unittest.main()