# matrix chain multiplication

# recursive solution
def matrixChainMultiplication(arr, i, j):
    if i == j:
        return 0
    mn = float('inf')
    for k in range(i, j):
        count = matrixChainMultiplication(arr, i, k) + matrixChainMultiplication(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        mn = min(mn, count)

    return mn

# memoization
def matrixChainMultiplicationMem(arr, i, j, dp):
    if i == j:
        return 0
    mn = float('inf')
    if dp[i][j] != -1:
        return dp[i][j]
    
    for k in range(i, j):
        count = matrixChainMultiplicationMem(arr, i, k, dp) + matrixChainMultiplicationMem(arr, k+1, j, dp) + arr[i-1]*arr[k]*arr[j]
        mn = min(mn, count)

    dp[i][j] = mn
    return mn

arr = [40, 20, 30, 10, 30]
n = len(arr)
dp = [[-1 for i in range(n)] for j in range(n)]
print(matrixChainMultiplication(arr, 1, n-1))
print(matrixChainMultiplicationMem(arr, 1, n-1, dp))