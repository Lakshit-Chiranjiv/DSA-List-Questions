# right angled triangle with n rows and each row has i+1 elements
# find the minimum sum path from top (0,0) to any element in last row
# you can move only to down or diagonally right down


# recursive solution
def minPathSum(arr, n, i, j):
    if i == n-1:
        return arr[i][j]
    down = minPathSum(arr, n, i+1, j)
    diag = minPathSum(arr, n, i+1, j+1)
    return arr[i][j] + min(down, diag)

# memoization
def minPathSumMemo(arr, n, i, j, dp):
    if i == n-1:
        return arr[i][j]
    if dp[i][j] != -1:
        return dp[i][j]
    down = minPathSumMemo(arr, n, i+1, j, dp)
    diag = minPathSumMemo(arr, n, i+1, j+1, dp)
    dp[i][j] = arr[i][j] + min(down, diag)
    return dp[i][j]

# tabulation
def minPathSumTab(arr, n):
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n-1, -1, -1):
        dp[n-1][i] = arr[n-1][i]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = arr[i][j] + min(dp[i+1][j], dp[i+1][j+1])
    return dp[0][0]

# space optimization
def minPathSumSpaceOpt(arr, n):
    dp = [0 for i in range(n)]
    temp = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        dp[i] = arr[n-1][i]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            temp[j] = arr[i][j] + min(dp[j], dp[j+1])
        dp, temp = temp, dp
    return dp[0]

arr = [[2, 0, 0, 0],
         [3, 7, 0, 0],
            [9, 4, 1, 0],
                [2, 7, 5, 9]]
n = len(arr)
print(minPathSum(arr, n, 0, 0))
dp = [[-1 for j in range(n)] for i in range(n)]
print(minPathSumMemo(arr, n, 0, 0, dp))
print(minPathSumTab(arr, n))
print(minPathSumSpaceOpt(arr, n))