# coins change 2 
# given coins of different denominations and a total amount of money
# write a function to compute the number of combinations that make up that amount
# you may assume that you have infinite number of each kind of coin

# recursive solution
def coinsChange(coins, idx, amount):
    if idx == 0:
        if amount % coins[idx] == 0:
            return 1
        else:
            return 0
    
    notPick = coinsChange(coins, idx-1, amount)
    pick = 0
    if amount >= coins[idx]:
        pick = coinsChange(coins, idx, amount-coins[idx])
    
    return notPick + pick

# memoization
def coinsChangeMemo(coins, idx, amount, dp):
    if idx == 0:
        if amount % coins[idx] == 0:
            return 1
        else:
            return 0
    
    if dp[idx][amount] != -1:
        return dp[idx][amount]
    
    notPick = coinsChangeMemo(coins, idx-1, amount, dp)
    pick = 0
    if amount >= coins[idx]:
        pick = coinsChangeMemo(coins, idx, amount-coins[idx], dp)
    
    dp[idx][amount] = notPick + pick
    return dp[idx][amount]

# tabulation
def coinsChangeTab(coins, idx, amount):
    dp = [[0 for i in range(amount+1)] for j in range(idx+1)]

    for i in range(amount+1):
        if i % coins[0] == 0:
            dp[0][i] = 1
        else:
            dp[0][i] = 0

    for i in range(1, idx+1):
        for j in range(1, amount+1):
            notPick = dp[i-1][j]
            pick = 0
            if j >= coins[i]:
                pick = dp[i][j-coins[i]]
            dp[i][j] = notPick + pick
    return dp[idx][amount]

# space optimization
def coinsChangeTabSpaceOpt(coins, idx, amount):
    dp = [0 for i in range(amount+1)]
    curr = [0 for i in range(amount+1)]

    for i in range(amount+1):
        if i % coins[0] == 0:
            dp[i] = 1
        else:
            dp[i] = 0

    for i in range(1, idx+1):
        for j in range(1, amount+1):
            notPick = dp[j]
            pick = 0
            if j >= coins[i]:
                pick = curr[j-coins[i]]
            curr[j] = notPick + pick

        dp = curr
        curr = [0 for i in range(amount+1)]
    return dp[amount]


coins = [1, 2, 5]
amount = 5
print(coinsChange(coins, len(coins)-1, amount))
dp = [[-1 for i in range(amount+1)] for j in range(len(coins))]
print(coinsChangeMemo(coins, len(coins)-1, amount, dp))
print(coinsChangeTab(coins, len(coins)-1, amount))
print(coinsChangeTabSpaceOpt(coins, len(coins)-1, amount))