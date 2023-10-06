class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def solve(x):
            if x <= 1:
                return x

            ans = x
            for i in range(2,x):
                val = solve(i)*solve(x-i)
                ans = max(ans,val)
            return ans
        if n <= 3: return n-1
        return solve(n)