def flattenBoard(board):
    return [item for sublist in board for item in sublist]

def unflattenBoard(flat_board):
    board = [[0]*4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            board[i][j] = flat_board[i*4+j]

    return board

def updateSyncBoard(syncBoard, board):
    tmp = flattenBoard(board)

    for i in range(4*4):
        syncBoard[i] = tmp[i]
            
    return syncBoard