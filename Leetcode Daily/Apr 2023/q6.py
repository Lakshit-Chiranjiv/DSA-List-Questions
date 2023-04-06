class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if visited[i][j]:
                return True
            visited[i][j] = True
            if grid[i][j] == 1:
                return True
            isClosed = True
            isClosed &= dfs(i - 1, j)
            isClosed &= dfs(i + 1, j)
            isClosed &= dfs(i, j - 1)
            isClosed &= dfs(i, j + 1)
            return isClosed
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and not visited[i][j]:
                    isClosed = dfs(i, j)
                    if isClosed:
                        count += 1
        return count
    
# intution:
# 1. For each cell in the grid, if it is 0 and not visited, then we check if it is closed using dfs.
# 2. Call dfs on the cell and if it returns True, then we increment count by 1.
# 3. In dfs, if the cell is out of bounds or visited, then we return True.
# 4. If the cell is 1, then we return True.
# 5. Else, we set isClosed to True and call dfs on the 4 adjacent cells.

# solution:
# 1. Initialize m to the number of rows in the grid and n to the number of columns in the grid.
# 2. Initialize count to 0 and visited to a 2D array of size m * n with all elements set to False.
# 3. Define dfs as follows:
# 4. If the cell is out of bounds or visited, then we return True.
# 5. If the cell is 1, then we return True.
# 6. Else, we set isClosed to True and call dfs on the 4 adjacent cells.
# 7. Return isClosed at the end.
# 8. For each cell in the grid, if it is 0 and not visited, then we check if it is closed using dfs.
# 9. Call dfs on the cell and if it returns True, then we increment count by 1.
# 10. Return count at the end.

# Time complexity: O(m * n) where m is the number of rows in the grid and n is the number of columns in the grid. We visit each cell once. 
# Space complexity: O(m * n) where m is the number of rows in the grid and n is the number of columns in the grid. We use a 2D array of size m * n to store visited.

