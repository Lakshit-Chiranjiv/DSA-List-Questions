# count unique paths in a grid from (0,0) to (m-1,n-1)
# you can only move right or down

# recursive solution
def uniquePaths(m, n):
    if m == 0 or n == 0:
        return 1
    if m < 0 or n < 0:
        return 0
    return uniquePaths(m-1, n) + uniquePaths(m, n-1)

# memoization
def uniquePathsMem(m, n, dp):
    if m == 0 or n == 0:
        return 1
    if m < 0 or n < 0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    dp[m][n] = uniquePathsMem(m-1, n, dp) + uniquePathsMem(m, n-1, dp)
    return dp[m][n]

# tabulation
def uniquePathsTab(m, n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

# space optimization
def uniquePathsSpOpt(m, n):
    dp = [1 for i in range(n)]
    for i in range(m):
        temp = [1 for i in range(n)]
        for j in range(n):
            if i == 0 or j == 0:
                temp[j] = 1
            else:
                temp[j] = dp[j] + temp[j-1]
        dp = temp
    return dp[n-1]

m = 3
n = 7
dp = [[-1 for i in range(n+1)] for j in range(m+1)]
print(uniquePaths(m-1, n-1))
print(uniquePathsMem(m-1, n-1, dp))
print(uniquePathsTab(m, n))
print(uniquePathsSpOpt(m, n))
