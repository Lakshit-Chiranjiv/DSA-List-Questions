class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        dirc = [[0,1],[0,-1],[1,0],[-1,0]]
        @cache
        def solve(i,j,p):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]<=p:
                return 0
            ans = 1
            for d in dirc:
                ans += solve(i+d[0],j+d[1],grid[i][j])
            return ans
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += solve(i,j,-1)
        return ans%MOD
        