# count square submatrices with all ones

def countSquares(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = matrix[i][j]
            elif matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return sum([sum(i) for i in dp])

matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
print(countSquares(matrix))