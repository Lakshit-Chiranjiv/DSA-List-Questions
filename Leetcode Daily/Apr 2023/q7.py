class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            
            grid[i][j] = -1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)

        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        return count
    
# intuition:
# 1. We start from the boundaries of the grid and call dfs on all the 1s. We mark all the 1s that are connected to the boundaries as -1.
# 2. We then count the number of 1s that are not marked as -1 and return it as those 1s are not reachable from the boundaries.

# solution:
# 1. Initialize m to the number of rows in the grid and n to the number of columns in the grid.
# 2. Initialize count to 0.
# 3. Define dfs as follows:
# 4. If the cell is out of bounds or the cell is not 1, then we return.
# 5. Else, we mark the cell as -1 and call dfs on the 4 adjacent cells.
# 6. For each boundary row, we call dfs on the first and last column.
# 7. For each boundary column, we call dfs on the first and last row.
# 8. For each cell in the grid, if the cell is 1, then we increment count by 1.
# 9. Return count at the end.