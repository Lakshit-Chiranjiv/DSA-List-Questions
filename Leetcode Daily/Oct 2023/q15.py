class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = arrLen
        @cache
        def solve(i,s):
            if i < 0 or i >= n:
                return 0
            if s < 0:
                return 0
            if i == 0 and s == 0:
                return 1
            left = solve(i-1,s-1)
            right = solve(i+1,s-1)
            stay = solve(i,s-1)
            return left+right+stay
        return solve(0,steps)