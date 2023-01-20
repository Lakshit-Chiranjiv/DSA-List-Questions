# Maximum Falling Path Sum | Variable Starting and Ending Points

# Given a grid of M x N integers, find the maximum sum of a falling path from any cell in the first row to any cell in the last row.

# recursive solution
def maxFallingPathSum(i,j,grid):
    if j < 0 or j >= len(grid[0]):
        return float('-inf')
    if i == 0:
        return grid[i][j]
    up = maxFallingPathSum(i-1,j,grid)
    leftUpDiag = maxFallingPathSum(i-1,j-1,grid)
    rightUpDiag = maxFallingPathSum(i-1,j+1,grid)

    return grid[i][j] + max(up,leftUpDiag,rightUpDiag)

def findMaxFallingPathSum(grid):
    maxSum = float('-inf')
    for j in range(len(grid[0])):
        maxSum = max(maxSum,maxFallingPathSum(len(grid)-1,j,grid))
    return maxSum

# memoization solution
def maxFallingPathSumMem(i,j,grid,dp):
    if j < 0 or j >= len(grid[0]):
        return float('-inf')
    if i == 0:
        return grid[i][j]
    if dp[i][j] != -1:
        return dp[i][j]
    up = maxFallingPathSumMem(i-1,j,grid,dp)
    leftUpDiag = maxFallingPathSumMem(i-1,j-1,grid,dp)
    rightUpDiag = maxFallingPathSumMem(i-1,j+1,grid,dp)

    dp[i][j] = grid[i][j] + max(up,leftUpDiag,rightUpDiag)
    return dp[i][j]

def findMaxFallingPathSumMem(grid):
    maxSum = float('-inf')
    dp = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
    for j in range(len(grid[0])):
        maxSum = max(maxSum,maxFallingPathSumMem(len(grid)-1,j,grid,dp))
    return maxSum

# tabulation solution
def findMaxFallingPathSumTab(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[0 for j in range(m)] for i in range(n)]
    for j in range(m):
        dp[0][j] = grid[0][j]
    for i in range(1,n):
        for j in range(m):
            up = dp[i-1][j]
            leftUpDiag = dp[i-1][j-1] if j-1 >= 0 else float('-inf')
            rightUpDiag = dp[i-1][j+1] if j+1 < m else float('-inf')
            dp[i][j] = grid[i][j] + max(up,leftUpDiag,rightUpDiag)

    maxSum = float('-inf')
    for j in range(m):
        maxSum = max(maxSum,dp[n-1][j])

    return maxSum

# space optimization
def findMaxFallingPathSumSpOpt(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [0 for j in range(m)]
    for j in range(m):
        dp[j] = grid[0][j]
    for i in range(1,n):
        newDp = [0 for j in range(m)]
        for j in range(m):
            up = dp[j]
            leftUpDiag = dp[j-1] if j-1 >= 0 else float('-inf')
            rightUpDiag = dp[j+1] if j+1 < m else float('-inf')
            newDp[j] = grid[i][j] + max(up,leftUpDiag,rightUpDiag)
        dp = newDp

    maxSum = float('-inf')
    for j in range(m):
        maxSum = max(maxSum,dp[j])

    return maxSum

grid = [[1,2,3],[4,5,6],[7,8,9]]
print(findMaxFallingPathSum(grid))
print(findMaxFallingPathSumMem(grid))
print(findMaxFallingPathSumTab(grid))
print(findMaxFallingPathSumSpOpt(grid))



    