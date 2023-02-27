# buy and sell stocks part 2

# recursive solution
def maxProfit(prices, i, buyAllow):
    if i == len(prices):
        return 0
    profit = 0
    if buyAllow:
        buy = maxProfit(prices, i+1, False) - prices[i]
        notBuy = maxProfit(prices, i+1, True)
        profit = max(buy, notBuy)
    else:
        sell = maxProfit(prices, i+1, True) + prices[i]
        notSell = maxProfit(prices, i+1, False)
        profit = max(sell, notSell)

    return profit

# memoization solution
def maxProfitMem(prices, i, buyAllow, dp):
    if i == len(prices):
        return 0
    if dp[i][buyAllow] != -1:
        return dp[i][buyAllow]
    profit = 0
    if buyAllow:
        buy = maxProfitMem(prices, i+1, False, dp) - prices[i]
        notBuy = maxProfitMem(prices, i+1, True, dp)
        profit = max(buy, notBuy)
    else:
        sell = maxProfitMem(prices, i+1, True, dp) + prices[i]
        notSell = maxProfitMem(prices, i+1, False, dp)
        profit = max(sell, notSell)

    dp[i][buyAllow] = profit
    return profit

# tabulation solution
def maxProfitTab(prices):
    n = len(prices)
    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    dp[n][1] = dp[n][0] = 0

    for i in range(n-1, -1, -1):
        for j in range(2):
            if j == 1:
                buy = dp[i+1][0] - prices[i]
                notBuy = dp[i+1][1]
                dp[i][j] = max(buy, notBuy)
            else:
                sell = dp[i+1][1] + prices[i]
                notSell = dp[i+1][0]
                dp[i][j] = max(sell, notSell)

    return dp[0][1]

# space optimization solution
def maxProfitSpace(prices):
    n = len(prices)
    ahead = [0 for _ in range(2)]
    curr = [0 for _ in range(2)]
    ahead[1] = 0
    ahead[0] = 0

    for i in range(n-1, -1, -1):
        for j in range(2):
            if j == 1:
                buy = ahead[0] - prices[i]
                notBuy = ahead[1]
                curr[j] = max(buy, notBuy)
            else:
                sell = ahead[1] + prices[i]
                notSell = ahead[0]
                curr[j] = max(sell, notSell)

        ahead[0] = curr[0]
        ahead[1] = curr[1]

    return ahead[1]

# space optimization with variables solution
def maxProfitSpaceVar(prices):
    n = len(prices)
    aheadBuy = 0
    aheadNotBuy = 0

    for i in range(n-1, -1, -1):
        currBuy = max(aheadNotBuy - prices[i], aheadBuy)
        currNotBuy = max(aheadBuy + prices[i], aheadNotBuy)
        aheadBuy = currBuy
        aheadNotBuy = currNotBuy

    return aheadBuy

prices = [7,1,5,3,6,4]
print(maxProfit(prices, 0, True))
dp = [[-1 for _ in range(2)] for _ in range(len(prices)+1)]
print(maxProfitMem(prices, 0, True, dp))
print(maxProfitTab(prices))
print(maxProfitSpace(prices))
print(maxProfitSpaceVar(prices))