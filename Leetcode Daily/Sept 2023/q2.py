class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def solve(i):
            if i >= len(s):
                return 0
            ans = 1+solve(i+1)

            for j in range(i,len(s)):
                if s[i:j+1] in dictionary:
                    ans = min(ans,solve(j+1))
            return ans
        return solve(0)