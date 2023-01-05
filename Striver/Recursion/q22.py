
# return one solved sudoku board from given board

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in range(1, 10):
                    if check(board, i, j, k):
                        board[i][j] = k
                        if solve(board):
                            return True
                        else:
                            board[i][j] = 0
                return False
    return True

def check(board, i, j, k):
    for m in range(9):
        if board[i][m] == k or board[m][j] == k:
            return False
        if board[(i//3)*3 + m//3][(j//3)*3 + m%3] == k:
            return False
    return True

board   = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

solve(board)
for i in range(9):
    print(board[i])
