# best time to buy and sell stock part 4

# recursive solution
def maxProfit(prices, i, buy, cap):
    if cap == 0:
        return 0
    if i == len(prices):
        return 0

    if buy:
        buying = maxProfit(prices, i+1, False, cap) - prices[i]
        notBuying = maxProfit(prices, i+1, True, cap)
        return max(buying, notBuying)
    else:
        selling = maxProfit(prices, i+1, True, cap-1) + prices[i]
        notSelling = maxProfit(prices, i+1, False, cap)
        return max(selling, notSelling)
    
# memoization solution
def maxProfitMem(prices, i, buy, cap, dp):
    if cap == 0:
        return 0
    if i == len(prices):
        return 0
    if dp[i][buy][cap] != -1:
        return dp[i][buy][cap]

    if buy:
        buying = maxProfitMem(prices, i+1, False, cap, dp) - prices[i]
        notBuying = maxProfitMem(prices, i+1, True, cap, dp)
        dp[i][buy][cap] = max(buying, notBuying)
    else:
        selling = maxProfitMem(prices, i+1, True, cap-1, dp) + prices[i]
        notSelling = maxProfitMem(prices, i+1, False, cap, dp)
        dp[i][buy][cap] = max(selling, notSelling)

    return dp[i][buy][cap]

# tabulation solution
def maxProfitTab(prices,k):
    n = len(prices)
    dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        for buy in range(0, 2):
            for cap in range(1, k+1):
                if buy:
                    buying = dp[i+1][0][cap] - prices[i]
                    notBuying = dp[i+1][1][cap]
                    dp[i][buy][cap] = max(buying, notBuying)
                else:
                    selling = dp[i+1][1][cap-1] + prices[i]
                    notSelling = dp[i+1][0][cap]
                    dp[i][buy][cap] = max(selling, notSelling)

    return dp[0][1][k]

# space optimization solution
def maxProfitSpace(prices,k):
    n = len(prices)
    after = [[0 for _ in range(k+1)] for _ in range(2)]
    curr = [[0 for _ in range(k+1)] for _ in range(2)]

    for i in range(n-1, -1, -1):
        for buy in range(0, 2):
            for cap in range(1, k+1):
                if buy:
                    buying = after[0][cap] - prices[i]
                    notBuying = after[1][cap]
                    curr[buy][cap] = max(buying, notBuying)
                else:
                    selling = after[1][cap-1] + prices[i]
                    notSelling = after[0][cap]
                    curr[buy][cap] = max(selling, notSelling)

        after = curr
    return after[1][k]


prices = [3,3,5,0,0,3,1,4]
k = 4
print(maxProfit(prices, 0, True, k))
dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(len(prices)+1)]
print(maxProfitMem(prices, 0, True, k, dp))
print(maxProfitTab(prices, k))
print(maxProfitSpace(prices, k))