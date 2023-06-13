class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        c = 0
        for i in grid:
            for j in res:
                if i == j:
                    c += 1
        return c
    
# intuition:
# 1. We will create a transpose of the grid and check each row of grid against each row of the transpose. If they are equal, then we have found a pair of equal rows.

# solution:
# 1. Create the transpose of the grid and store it in a variable res.
# 2. Initialize a variable c to store the count of equal pairs. Set it to 0.
# 3. Iterate over the rows of grid. For each row, iterate over the rows of res. If the row of grid is equal to the row of res, then increment c by 1.
# 4. Return c.

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)