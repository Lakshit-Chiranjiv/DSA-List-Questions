class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        dir = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
        @cache
        def solve(i,j,k):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0

            if k == 0:
                return 1

            ans = 0
            for d in dir:
                r = i + d[0] 
                c = j + d[1] 
                ans += solve(r,c,k-1)

            return ans/8
        return solve(row,column,k)