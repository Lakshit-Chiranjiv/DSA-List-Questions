class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD
        
        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % MOD


# intuition:
# 1. There are 3 changing parameters: i(the index in array), n(the number of members), p(the profit).
# 2. The dp array is 3D, dp[i][n][p] means the number of schemes with i members and p profit.
# 3. There is a skip case where we simply copy the previous value, dp[i][n][p] = dp[i - 1][n][p].
# 4. There is a take case where we add the previous value, dp[i][n][p] = dp[i - 1][n - members][max(0, p - earn)].
# 5. The final answer is the sum of dp[length][j][minProfit] for j in range(n + 1).

# solution:
# 1. Initialize the dp array of size (length + 1) * (n + 1) * (minProfit + 1) with 0.
# 2. Set dp[0][0][0] = 1.
# 3. Loop through the dp array, i from 1 to length + 1, j from 0 to n + 1, k from 0 to minProfit + 1.
# 4. If j < members, dp[i][j][k] = dp[i - 1][j][k].
# 5. Else, dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD.
# 6. Return the sum of dp[length][j][minProfit] for j in range(n + 1).

# Time complexity: O(n * length * minProfit) where n is the number of members, length is the length of group and profit, minProfit is the minimum profit as we need to loop through all possible profits.

# Space complexity: O(n * length * minProfit) where n is the number of members, length is the length of group and profit, minProfit is the minimum profit as we are using a 3D dp array.