class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def solve(i):
            if i >= len(cost)-1:
                return 0
            return min(cost[i]+solve(i+1), cost[i+1]+solve(i+2))

        return solve(0)