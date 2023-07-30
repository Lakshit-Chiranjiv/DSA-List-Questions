class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        @cache
        def solve(left, right):
            mn = n
            j = -1
            
            for i in range(left, right):
                if s[i] != s[right] and j == -1:
                    j = i
                if j != -1:
                    mn = min(mn, 1 + solve(j, i) + solve(i + 1, right))
                    
            if j == -1:
                mn = 0
    
            return mn

        return solve(0, n - 1) + 1