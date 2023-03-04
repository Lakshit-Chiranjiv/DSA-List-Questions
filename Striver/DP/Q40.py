# buy and sell stocks with transaction fee

# recursive solution
def maxProfit(prices, i, buyAllow, fee):
    if i == len(prices):
        return 0
    profit = 0
    if buyAllow:
        buy = maxProfit(prices, i+1, False, fee) - prices[i]
        notBuy = maxProfit(prices, i+1, True, fee)
        profit = max(buy, notBuy)
    else:
        sell = maxProfit(prices, i+1, True, fee) + prices[i] - fee
        notSell = maxProfit(prices, i+1, False, fee)
        profit = max(sell, notSell)

    return profit

# memoization solution
def maxProfitMem(prices, i, buyAllow, dp, fee):
    if i == len(prices):
        return 0
    if dp[i][buyAllow] != -1:
        return dp[i][buyAllow]
    profit = 0
    if buyAllow:
        buy = maxProfitMem(prices, i+1, False, dp, fee) - prices[i]
        notBuy = maxProfitMem(prices, i+1, True, dp, fee)
        profit = max(buy, notBuy)
    else:
        sell = maxProfitMem(prices, i+1, True, dp, fee) + prices[i] - fee
        notSell = maxProfitMem(prices, i+1, False, dp, fee)
        profit = max(sell, notSell)

    dp[i][buyAllow] = profit
    return profit

# tabulation solution
def maxProfitTab(prices, fee):
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
                sell = dp[i+1][1] + prices[i] - fee
                notSell = dp[i+1][0]
                dp[i][j] = max(sell, notSell)

    return dp[0][1]

# space optimization solution
def maxProfitSpace(prices, fee):
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
                sell = ahead[1] + prices[i] - fee
                notSell = ahead[0]
                curr[j] = max(sell, notSell)

        ahead[0] = curr[0]
        ahead[1] = curr[1]

    return ahead[1]

# space optimization with variables solution
def maxProfitSpaceVar(prices, fee):
    n = len(prices)
    aheadBuy = 0
    aheadNotBuy = 0

    for i in range(n-1, -1, -1):
        currBuy = max(aheadNotBuy - prices[i], aheadBuy)
        currNotBuy = max(aheadBuy + prices[i] - fee, aheadNotBuy)
        aheadBuy = currBuy
        aheadNotBuy = currNotBuy

    return aheadBuy


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(maxProfit(prices, 0, True, fee))
dp = [[-1 for _ in range(2)] for _ in range(len(prices)+1)]
print(maxProfitMem(prices, 0, True, dp, fee))
print(maxProfitTab(prices, fee))
print(maxProfitSpace(prices, fee))
print(maxProfitSpaceVar(prices, fee))