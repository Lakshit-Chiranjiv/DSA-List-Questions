# Unbounded KnapSack

# recursive solution
def unboundedKnapSack(W, wt, val, n):
    if n == 0:
        return (W//wt[n])*val[n]
    
    notTake = unboundedKnapSack(W, wt, val, n-1)
    take = 0
    if W >= wt[n]:
        take = unboundedKnapSack(W-wt[n], wt, val, n) + val[n]
    return max(notTake, take)

# memoization
def unboundedKnapSackMemo(W, wt, val, n, dp):
    if n == 0:
        return (W//wt[n])*val[n]
    
    if dp[n][W] != -1:
        return dp[n][W]
    
    notTake = unboundedKnapSackMemo(W, wt, val, n-1, dp)
    take = 0
    if W >= wt[n]:
        take = unboundedKnapSackMemo(W-wt[n], wt, val, n, dp) + val[n]
    dp[n][W] = max(notTake, take)
    return dp[n][W]

# tabulation
def unboundedKnapSackTab(W, wt, val, n):
    dp = [[0 for i in range(W+1)] for j in range(n)]

    for i in range(W+1):
        dp[0][i] = (i//wt[0])*val[0]
    
    for i in range(1, n):
        for j in range(1, W+1):
            notTake = dp[i-1][j]
            take = 0
            if j >= wt[i]:
                take = dp[i][j-wt[i]] + val[i]
            dp[i][j] = max(notTake, take)

    return dp[n-1][W]

# space optimization
def unboundedKnapSackSpaceOpt(W, wt, val, n):
    dp = [0 for i in range(W+1)]
    curr = [0 for i in range(W+1)]

    for i in range(W+1):
        dp[i] = (i//wt[0])*val[0]

    for i in range(1, n):
        for j in range(1, W+1):
            notTake = dp[j]
            take = 0
            if j >= wt[i]:
                take = curr[j-wt[i]] + val[i]
            curr[j] = max(notTake, take)
        dp = curr
        curr = [0 for i in range(W+1)]

    return dp[W]

vals = [10, 40, 50, 70]
wts = [1, 3, 4, 5]
W = 8
n = len(vals)
dp = [[-1 for i in range(W+1)] for j in range(n)]
print(unboundedKnapSack(W, wts, vals, n-1))
print(unboundedKnapSackMemo(W, wts, vals, n-1, dp))
print(unboundedKnapSackTab(W, wts, vals, n))
print(unboundedKnapSackSpaceOpt(W, wts, vals, n))
