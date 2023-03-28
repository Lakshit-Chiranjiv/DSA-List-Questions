# matrix chain multiplication

# tabulation
def matrix_chain_multiplication(arr):
    n = len(arr)
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        dp[i][i] = 0

    for i in range(n-1,0,-1):
        for j in range(i+1,n):
            dp[i][j] = float('inf')
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j])
            
    return dp[1][n-1]

arr = [40, 20, 30, 10, 30]
print(matrix_chain_multiplication(arr))