class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        aheadBuy = 0
        aheadNotBuy = 0

        for i in range(n-1, -1, -1):
            currBuy = max(aheadNotBuy - prices[i], aheadBuy)
            currNotBuy = max(aheadBuy + prices[i] - fee, aheadNotBuy)
            aheadBuy = currBuy
            aheadNotBuy = currNotBuy

        return aheadBuy