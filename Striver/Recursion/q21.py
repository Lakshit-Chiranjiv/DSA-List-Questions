# n-queens problem - storing the queen's position for leftrow, upperleft diagonal and lowerleft diagonal

def nQueen(arr,col,leftrow,upperleft,lowerleft):
    if col >= len(arr):
        print(arr)
        return
    for i in range(len(arr)):
        if isSafe(arr,i,col,leftrow,upperleft,lowerleft):
            arr[i][col] = 1
            leftrow[i] = 1
            upperleft[i-col] = 1
            lowerleft[i+col] = 1
            nQueen(arr,col+1,leftrow,upperleft,lowerleft)
            arr[i][col] = 0
            leftrow[i] = 0
            upperleft[i-col] = 0
            lowerleft[i+col] = 0

def isSafe(arr,row,col,leftrow,upperleft,lowerleft):
    if leftrow[row] == 1:
        return False
    if upperleft[row-col] == 1:
        return False
    if lowerleft[row+col] == 1:
        return False
    return True

arr = [[0 for i in range(4)] for j in range(4)]
leftrow = [0 for i in range(4)]
upperleft = [0 for i in range(4)]
lowerleft = [0 for i in range(4)]
nQueen(arr,0,leftrow,upperleft,lowerleft)