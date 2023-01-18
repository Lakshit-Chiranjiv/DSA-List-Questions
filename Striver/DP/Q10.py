# min cost path in grid from (0,0) to (n-1,m-1)
# only right and down moves are allowed

# recursive solution
def minCostPath(grid, i, j):
    if i == 0 and j == 0:
        return grid[i][j]
    if i < 0 or j < 0:
        return float('inf')
    return grid[i][j] + min(minCostPath(grid, i-1, j), minCostPath(grid, i, j-1))

# memoization solution
def minCostPathMem(grid, i, j, dp):
    if i == 0 and j == 0:
        return grid[i][j]
    if i < 0 or j < 0:
        return float('inf')
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = grid[i][j] + min(minCostPathMem(grid, i-1, j, dp), minCostPathMem(grid, i, j-1, dp))
    return dp[i][j]

# tabulation solution
def minCostPathTab(grid, m, n):
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = grid[i][j] + dp[i][j-1]
            elif j == 0:
                dp[i][j] = grid[i][j] + dp[i-1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]

# space optimization
def minCostPathSpaceOpt(grid, m, n):
    dp = [0 for i in range(n)]
    for i in range(m):
        temp = [0 for i in range(n)]
        for j in range(n):
            if i == 0 and j == 0:
                temp[j] = grid[i][j]
            if i == 0:
                temp[j] = grid[i][j] + temp[j-1]
            elif j == 0:
                temp[j] = grid[i][j] + dp[j]
            else:
                temp[j] = grid[i][j] + min(dp[j], temp[j-1])
        dp = temp
    return dp[n-1]

grid = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
print(minCostPath(grid, 2, 2))
dp = [[-1 for i in range(3)] for j in range(3)]
print(minCostPathMem(grid, 2, 2, dp))
print(minCostPathTab(grid, 3, 3))
print(minCostPathSpaceOpt(grid, 3, 3))