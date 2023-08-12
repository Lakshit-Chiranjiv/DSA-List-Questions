class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def solve(i,j):
            if i >= m or j >= n or grid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            right = 0
            if j+1 < n and grid[i][j+1] != 1:
                right = solve(i,j+1)
            down = 0
            if i+1 < m and grid[i+1][j] != 1:
                down = solve(i+1,j)

            return right + down

        return solve(0,0)
