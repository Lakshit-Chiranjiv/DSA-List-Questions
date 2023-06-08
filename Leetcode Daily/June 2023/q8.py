class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for i in grid:
            for j in i:
                if j < 0:
                    c += 1
        return c
    
    
# intuition:
# 1. Simply iterate over the grid and count the number of negative numbers.

# solution:
# 1. Initialize a variable c to 0.
# 2. Iterate over the grid and check if the current element is negative. If yes, then increment c by 1.
# 3. Return c.

# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the grid. We are iterating over the entire grid.

# Space Complexity: O(1) as we are not using any extra space. We are just using a variable c to store the count of negative numbers.