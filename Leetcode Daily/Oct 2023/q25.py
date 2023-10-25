class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        l = 1
        r = 2**(n-1)
        ans = 0
        for i in range(n-1):
            m = (l+r)//2
            if k <= m:
                r = m
            else:
                l = m+1
                ans = 0 if ans else 1
        return ans