class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        
        ans = 1
        i = 2
        while i <= n:
            ans += (((i-2)*4)+4)
            i += 1
            
        return ans