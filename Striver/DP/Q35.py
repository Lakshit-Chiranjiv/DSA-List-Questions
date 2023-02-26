# best time to buy and sell stock

def maxProfit(prices):
    n = len(prices)
    dp = [0] * n
    minPrice = prices[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1], prices[i]-minPrice)
        minPrice = min(minPrice, prices[i])

    return dp[n-1]

prices = [7,1,5,3,6,4]
print(maxProfit(prices))