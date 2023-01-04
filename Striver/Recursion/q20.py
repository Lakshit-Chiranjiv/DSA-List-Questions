# n-queen - backtracking

def nQueen(arr,col):
    if col >= len(arr):
        print(arr)
        return
    for i in range(len(arr)):
        if isSafe(arr,i,col):
            arr[i][col] = 1
            nQueen(arr,col+1)
            arr[i][col] = 0

def isSafe(arr,row,col):
    for i in range(col):
        if arr[row][i] == 1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if arr[i][j] == 1:
            return False
    for i,j in zip(range(row,len(arr),1),range(col,-1,-1)):
        if arr[i][j] == 1:
            return False
    return True


arr = [[0 for i in range(4)] for j in range(4)]
nQueen(arr,0)
