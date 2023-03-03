class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
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