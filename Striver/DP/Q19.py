# 0/1 knapsack problem

# recursive solution
def knapsack(wt,val,idx,W):
    if idx == 0:
        if wt[idx] <= W:
            return val[idx]
        else:
            return 0
    notTake = knapsack(wt,val,idx-1,W)
    take = float('-inf')
    if wt[idx] <= W:
        take = val[idx] + knapsack(wt,val,idx-1,W-wt[idx])
    return max(notTake,take)

# memoization
def knapsackMemo(wt,val,idx,W,dp):
    if idx == 0:
        if wt[idx] <= W:
            return val[idx]
        else:
            return 0
    if dp[idx][W] != -1:
        return dp[idx][W]
    notTake = knapsackMemo(wt,val,idx-1,W,dp)
    take = float('-inf')
    if wt[idx] <= W:
        take = val[idx] + knapsackMemo(wt,val,idx-1,W-wt[idx],dp)
    dp[idx][W] = max(notTake,take)
    return dp[idx][W]

# tabulation
def knapsackTab(wt,val,W):
    n = len(wt)
    dp = [[0 for i in range(W+1)] for j in range(n)]
    for i in range(wt[0],W+1):
        dp[0][i] = val[0]
    
    for i in range(1,n):
        for j in range(1,W+1):
            notTake = dp[i-1][j]
            take = float('-inf')
            if wt[i] <= j:
                take = val[i] + dp[i-1][j-wt[i]]
            dp[i][j] = max(notTake,take)
    return dp[n-1][W]

# space optimization with 2 1D arrays
def knapsackSpaceOpt(wt,val,W):
    n = len(wt)
    dp = [0 for i in range(W+1)]
    curr = [0 for i in range(W+1)]
    for i in range(wt[0],W+1):
        dp[i] = val[0]
    
    for i in range(1,n):
        for j in range(1,W+1):
            notTake = dp[j]
            take = float('-inf')
            if wt[i] <= j:
                take = val[i] + dp[j-wt[i]]
            curr[j] = max(notTake,take)
        dp = curr
        curr = [0 for i in range(W+1)]
    return dp[W]

# space optimization with 1 1D array
def knapsackSpaceOpt2(wt,val,W):
    n = len(wt)
    dp = [0 for i in range(W+1)]
    for i in range(wt[0],W+1):
        dp[i] = val[0]
    
    for i in range(1,n):
        for j in range(W,wt[i]-1,-1):
            notTake = dp[j]
            take = float('-inf')
            if wt[i] <= j:
                take = val[i] + dp[j-wt[i]]
            dp[j] = max(notTake,take)
    return dp[W]

wt = [1,3,4,5]
val = [1,4,5,7]
W = 7
print(knapsack(wt,val,len(wt)-1,W))
dp = [[-1 for i in range(W+1)] for j in range(len(wt))]
print(knapsackMemo(wt,val,len(wt)-1,W,dp))
print(knapsackTab(wt,val,W))
print(knapsackSpaceOpt(wt,val,W))
print(knapsackSpaceOpt2(wt,val,W))