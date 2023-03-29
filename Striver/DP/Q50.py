# minimum cost to cut the stick

# recursive solution
def minCost(cuts, i, j):
    if i > j:
        return 0
    mn = float('inf')
    for k in range(i, j+1):
        mn = min(mn, minCost(cuts, i, k-1) + minCost(cuts, k+1, j) + cuts[j+1] - cuts[i-1])
    return mn

# memoization
def minCostMemo(cuts, i, j, dp):
    if i > j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mn = float('inf')
    for k in range(i, j+1):
        mn = min(mn, minCostMemo(cuts, i, k-1, dp) + minCostMemo(cuts, k+1, j, dp) + cuts[j+1] - cuts[i-1])
    dp[i][j] = mn
    return mn

# tabulation
def minCostTab(cuts, n):
    c = len(cuts)-2

    dp = [[0 for i in range(c+2)] for j in range(c+2)]
    for i in range(c, 0, -1):
        for j in range(1, c+1):
            if i > j:
                continue
            mn = float('inf')
            for k in range(i, j+1):
                mn = min(mn, dp[i][k-1] + dp[k+1][j] + cuts[j+1] - cuts[i-1])
            dp[i][j] = mn

    return dp[1][c]

arr = [1, 3, 4, 5, 8]
c = len(arr)
n = 12
cuts = [0] + arr + [n]
dp = [[-1 for i in range(c+2)] for j in range(c+2)]
cuts.sort()
print(minCost(cuts, 1, c))
print(minCostMemo(cuts, 1, c, dp))
print(minCostTab(cuts, n))