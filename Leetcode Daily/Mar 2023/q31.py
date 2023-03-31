class Solution:
    def ways(self, pizza: List[str], K: int) -> int:
        m, n, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
        preSum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                preSum[r][c] = preSum[r][c + 1] + preSum[r + 1][c] - preSum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(k, r, c):
            if preSum[r][c] == 0: return 0
            if k == 0: return 1
            ans = 0

            for nr in range(r + 1, m):
                if preSum[r][c] - preSum[nr][c] > 0:
                    ans = (ans + dp(k - 1, nr, c)) % MOD                 
            for nc in range(c + 1, n):
                if preSum[r][c] - preSum[r][nc] > 0:
                    ans = (ans + dp(k - 1, r, nc)) % MOD
                    
            return ans

        return dp(K - 1, 0, 0)
    


# intution:
# 1. It is a 3D DP problem.
# 2. We can use a 3D dp array to store the result.
# 3. dp[k][r][c] stores the number of ways to cut the pizza into k pieces starting from the cell (r,c).
# 4. We can use a 2D preSum array to store the number of apples in the pizza.
# 5. preSum[r][c] stores the number of apples in the pizza starting from the cell (r,c).
# 6. Loop over rows and columns in reverse order and calculate the preSum array.
# 7. Then dp function will return the number of ways to cut the pizza into k pieces starting from the cell (r,c).

# solution:
# 1. Create a m, n and MOD variable and store the length of the pizza, the length of the pizza and 10^9 + 7 respectively.
# 2. Create a preSum array and initialize it with 0.
# 3. Loop over rows and columns in reverse order.
# 4. Calculate the preSum array by adding the current cell with the right cell, the bottom cell and the bottom right cell and subtracting the bottom right cell.
# 5. Create a dp function which takes k, r and c as parameters.
# 6. Check if the preSum[r][c] is 0, if it is return 0.
# 7. Check if k is 0, if it is return 1.
# 8. Create an ans variable and initialize it with 0.
# 9. Loop over the rows from r + 1 to m.
# 10. Check if the preSum[r][c] - preSum[nr][c] is greater than 0.
# 11. If it is, add the result of the dp function with k - 1, nr and c to the ans variable.
# 12. Loop over the columns from c + 1 to n.
# 13. Check if the preSum[r][c] - preSum[r][nc] is greater than 0.
# 14. If it is, add the result of the dp function with k - 1, r and nc to the ans variable.
# 15. Return the ans variable.
# 16. Return the result of the dp function with K - 1, 0 and 0.
