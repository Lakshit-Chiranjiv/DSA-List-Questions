# buy and sell stock with cooldown
# can't buy on the day after you sell

# recursive solution
def maxProfit(prices, i, buyAllow):
    if i >= len(prices):
        return 0
    profit = 0
    if buyAllow:
        buy = maxProfit(prices, i+1, False) - prices[i]
        notBuy = maxProfit(prices, i+1, True)
        profit = max(buy, notBuy)
    else:
        sell = maxProfit(prices, i+2, True) + prices[i]
        notSell = maxProfit(prices, i+1, False)
        profit = max(sell, notSell)

    return profit

# memoization solution
def maxProfitMem(prices, i, buyAllow, dp):
    if i >= len(prices):
        return 0
    if dp[i][buyAllow] != -1:
        return dp[i][buyAllow]
    profit = 0
    if buyAllow:
        buy = maxProfitMem(prices, i+1, False, dp) - prices[i]
        notBuy = maxProfitMem(prices, i+1, True, dp)
        profit = max(buy, notBuy)
    else:
        sell = maxProfitMem(prices, i+2, True, dp) + prices[i]
        notSell = maxProfitMem(prices, i+1, False, dp)
        profit = max(sell, notSell)

    dp[i][buyAllow] = profit
    return profit

# tabulation solution
def maxProfitTab(prices):
    n = len(prices)
    dp = [[0 for _ in range(2)] for _ in range(n+2)]
    dp[n][1] = dp[n][0] = 0

    for i in range(n-1, -1, -1):
        for j in range(2):
            if j == 1:
                buy = dp[i+1][0] - prices[i]
                notBuy = dp[i+1][1]
                dp[i][j] = max(buy, notBuy)
            else:
                sell = dp[i+2][1] + prices[i]
                notSell = dp[i+1][0]
                dp[i][j] = max(sell, notSell)

    return dp[0][1]

prices = [1,2,3,0,2]
print(maxProfit(prices, 0, True))
dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
print(maxProfitMem(prices, 0, True, dp))
print(maxProfitTab(prices))