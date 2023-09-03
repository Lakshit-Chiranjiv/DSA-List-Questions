class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def solve(i,j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            down = solve(i+1,j)
            right = solve(i,j+1)
            return down + right
        return solve(0,0)