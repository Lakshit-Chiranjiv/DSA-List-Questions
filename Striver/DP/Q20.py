# minimum coins required to make a given value with infinite supply of coins of given denominations

# recursive solution
def minCoins(coins, idx, value):
    if idx == 0:
        if value % coins[idx] == 0:
            return value // coins[idx]
        else:
            return float('inf')
    
    notTake = minCoins(coins, idx - 1, value)
    take = float('inf')
    if value >= coins[idx]:
        take = 1 + minCoins(coins, idx, value - coins[idx])
    
    return min(notTake, take)

# memoization
def minCoinsMem(coins, idx, value, dp):
    if idx == 0:
        if value % coins[idx] == 0:
            return value // coins[idx]
        else:
            return float('inf')
    
    if dp[idx][value] != -1:
        return dp[idx][value]
    
    notTake = minCoinsMem(coins, idx - 1, value, dp)
    take = float('inf')
    if value >= coins[idx]:
        take = 1 + minCoinsMem(coins, idx, value - coins[idx], dp)
    
    dp[idx][value] = min(notTake, take)
    return dp[idx][value]

# tabulation
def minCoinsTab(coins, value):
    dp = [[0 for _ in range(value + 1)] for _ in range(len(coins))]
    for i in range(value + 1):
        if i % coins[0] == 0:
            dp[0][i] = i // coins[0]
        else:
            dp[0][i] = float('inf')
    
    for i in range(1, len(coins)):
        for j in range(1, value + 1):
            notTake = dp[i - 1][j]
            take = float('inf')
            if j >= coins[i]:
                take = 1 + dp[i][j - coins[i]]
            dp[i][j] = min(notTake, take)
    
    return dp[len(coins) - 1][value]

# space optimization
def minCoinsSpOpt(coins, value):
    dp = [0 for _ in range(value + 1)]
    curr = [0 for _ in range(value + 1)]

    for i in range(value + 1):
        if i % coins[0] == 0:
            dp[i] = i // coins[0]
        else:
            dp[i] = float('inf')
    
    for i in range(1, len(coins)):
        for j in range(1, value + 1):
            notTake = dp[j]
            take = float('inf')
            if j >= coins[i]:
                take = 1 + curr[j - coins[i]]
            curr[j] = min(notTake, take)
        dp = curr.copy()
    
    return dp[value]

coins = [1, 2, 5]
value = 11
dp = [[-1 for _ in range(value + 1)] for _ in range(len(coins))]
print(minCoins(coins, len(coins) - 1, value))
print(minCoinsMem(coins, len(coins) - 1, value, dp))
print(minCoinsTab(coins, value))
print(minCoinsSpOpt(coins, value))
