# frog jump problem - k jumps allowed
import sys
max_size = sys.maxsize

# recursive solution
def frogJump(n, k, cost):
    if n == 0:
        return 0
    minVal = max_size
    for i in range(1, k+1):
        if n-i >= 0:
            minVal = min(minVal, frogJump(n-i, k, cost) + abs(cost[n] - cost[n-i]))
    return minVal

# memoization
def frogJump(n, k, cost, dp):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    minVal = max_size
    for i in range(1, k+1):
        minVal = min(minVal, frogJump(n-i, k, cost, dp) + abs(cost[n] - cost[n-i]))
    dp[n] = minVal
    return dp[n]

# tabulation
def frogJump(n,k,cost):
    dp = [-1] * (n+1)
    dp[0] = 0
    for i in range(1,n+1):
        minVal = max_size
        for j in range(1,k+1):
            if i-j >= 0:
                minVal = min(minVal, dp[i-j] + abs(cost[i] - cost[i-j]))
        dp[i] = minVal
    return dp[n]

# space optimazation
def frogJump(n,k,cost):
    dp = [-1] * (k+1)
    dp[0] = 0
    for i in range(1,n+1):
        minVal = max_size
        for j in range(1,k+1):
            if i-j >= 0:
                minVal = min(minVal, dp[j] + abs(cost[i] - cost[i-j]))
        dp[i%k] = minVal
    return dp[n%k]

k = 3
cost = [10, 30, 40, 20]
print(frogJump(len(cost)-1, k, cost))
dp = [-1] * (len(cost))
print(frogJump(len(cost)-1, k, cost, dp))
print(frogJump(len(cost)-1, k, cost))
