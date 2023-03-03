class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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