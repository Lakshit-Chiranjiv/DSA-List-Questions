class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        maxProfit = 0
        for i in prices[1:]:
            minSoFar = min(minSoFar,i)
            maxProfit = max(maxProfit,i - minSoFar)
        
        return maxProfit