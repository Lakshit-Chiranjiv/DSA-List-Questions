# distinct subsequences
# return the number of distinct subsequences of S which equals T

# recursive solution
def numDistinct(S, T, i, j):
    if j == 0:
        return 1
    if i == 0:
        return 0
    if S[i-1] == T[j-1]:
        return numDistinct(S, T, i-1, j-1) + numDistinct(S, T, i-1, j)
    else:
        return numDistinct(S, T, i-1, j)
    
# memoization
def numDistinctMem(S, T, i, j, dp):
    if j == 0:
        return 1
    if i == 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if S[i-1] == T[j-1]:
        dp[i][j] = numDistinctMem(S, T, i-1, j-1, dp) + numDistinctMem(S, T, i-1, j, dp)
    else:
        dp[i][j] = numDistinctMem(S, T, i-1, j, dp)
    return dp[i][j]

# tabulation
def numDistinctTab(S, T):
    m = len(S)
    n = len(T)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]

# space optimization
def numDistinctOpt(S, T):
    m = len(S)
    n = len(T)
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1, m+1):
        for j in range(n, 0, -1):
            if S[i-1] == T[j-1]:
                dp[j] += dp[j-1]
    return dp[n]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t, len(s), len(t)))
dp = [[-1 for i in range(len(t)+1)] for j in range(len(s)+1)]
print(numDistinctMem(s, t, len(s), len(t), dp))
print(numDistinctTab(s, t))
print(numDistinctOpt(s, t))
