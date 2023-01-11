# frog jump problem - 1 or 2 jumps allowed

import sys
max_size = sys.maxsize

# recursive solution
def frog_jump(n,cost):
    if n == 0:
        return 0
    right = max_size
    left = frog_jump(n-1,cost) + abs(cost[n] - cost[n-1])
    if n > 1:
        right = frog_jump(n-2,cost) + abs(cost[n] - cost[n-2])
    return min(left,right)

# memoization
def frog_jump(n,cost,dp):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    right = max_size
    left = frog_jump(n-1,cost,dp) + abs(cost[n] - cost[n-1])
    if n > 1:
        right = frog_jump(n-2,cost,dp) + abs(cost[n] - cost[n-2])
    dp[n] = min(left,right)
    return dp[n]

# tabulation
def frog_jump(n,cost):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = abs(cost[1] - cost[0])
    for i in range(2,n+1):
        dp[i] = min(dp[i-1] + abs(cost[i] - cost[i-1]), dp[i-2] + abs(cost[i] - cost[i-2]))
    return dp[n]

# space optimazation
def frog_jump(n,cost):
    a = 0
    b = abs(cost[1] - cost[0])
    for i in range(2,n+1):
        c = min(b + abs(cost[i] - cost[i-1]), a + abs(cost[i] - cost[i-2]))
        a = b
        b = c
    return b