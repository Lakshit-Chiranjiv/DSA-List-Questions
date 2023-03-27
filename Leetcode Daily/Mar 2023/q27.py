class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[m-1][n-1]


# intution
# 1. The minimum path from top left to bottom right will be the same as the minimum path from bottom right to top left. So we can start from the bottom right corner and move to the top left corner trying all the possible paths.
# 2. All possible paths means recursion. But recursion will be very slow. DP can be used to speed up the process. Tabulation is also feasible. We will go with Tabulation.
# 3. We will use a 2D array to store the minimum path sum from bottom right to top left. The last element of the array will be the minimum path sum from top left to bottom right.
# 4. Iterate through the array from bottom right to top left. For each element, we will add the minimum of the element below and the element to the right. This will be the minimum path sum from that element to the bottom right corner.
# 5. The last element of the array will be the minimum path sum from top left to bottom right.

# solution
# 1. Create a 2D array of size m*n. m and n are the number of rows and columns in the grid.
# 2. Iterate through the grid from first row to last row and from first column to last column.
# 3. If the current element is the first element, then dp[i][j] = grid[i][j]. This is because the first element is the starting point and it does not have any previous element.
# 4. If the current element is in the first row, then dp[i][j] = grid[i][j] + dp[i][j-1]. This is because the element to the left is the only element that can be reached from the current element.
# 5. If the current element is in the first column, then dp[i][j] = grid[i][j] + dp[i-1][j]. This is because the element below is the only element that can be reached from the current element.
# 6. If the current element is neither in the first row nor in the first column, then dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]). This is because the element below and the element to the left are the only elements that can be reached from the current element.
# 7. Return dp[m-1][n-1]. This is because the last element of the array will be the minimum path sum from top left to bottom right.

# complexity
# time: O(m*n) where m and n are the number of rows and columns in the grid. We iterate through the grid once.
# space: O(m*n) where m and n are the number of rows and columns in the grid. We create a 2D array of size m*n.