package Striver.DP;

public class Q20 {
    // Minimum coins to reach a value
    // infinite supply of coins of given denominations
    // if not possible, return -1 else return the minimum number of coins

    // recursive solution - Time: O(n^2) Space: O(n)
    public int minCoins(int[] coins, int idx, int value) {
        if (idx == 0){
            if (value % coins[idx] == 0) return value / coins[idx];
            return 999999;
        }

        int notTake = minCoins(coins, idx - 1, value);
        int take = 999999;
        if (coins[idx] <= value) take = 1 + minCoins(coins, idx, value - coins[idx]);

        return Math.min(notTake, take);
    }

    // memoization - Time: O(n^2) Space: O(n)
    public int minCoinsMemo(int[] coins, int idx, int value, int[][] dp) {
        if (idx == 0){
            if (value % coins[idx] == 0) return value / coins[idx];
            return 999999;
        }

        if (dp[idx][value] != -1) return dp[idx][value];

        int notTake = minCoinsMemo(coins, idx - 1, value, dp);
        int take = 999999;
        if (coins[idx] <= value) take = 1 + minCoinsMemo(coins, idx, value - coins[idx], dp);

        return dp[idx][value] = Math.min(notTake, take);
    }

    // tabulation - Time: O(n^2) Space: O(n)
    public int minCoinsTab(int[] coins, int value) {
        int n = coins.length;
        int[][] dp = new int[n][value + 1];

        for (int i = 0; i <= value; i++) {
            if (i % coins[0] == 0) dp[0][i] = i / coins[0];
            else dp[0][i] = 999999;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= value; j++) {
                int notTake = dp[i - 1][j];
                int take = 999999;
                if (coins[i] <= j) take = 1 + dp[i][j - coins[i]];

                dp[i][j] = Math.min(notTake, take);
            }
        }

        return dp[n - 1][value];
    }

    // space optimization - Time: O(n^2) Space: O(n)
    public int minCoinsTabSpaceOpt(int[] coins, int value) {
        int n = coins.length;
        int[] dp = new int[value + 1];
        int[] curr = new int[value + 1];

        for (int i = 0; i <= value; i++) {
            if (i % coins[0] == 0) dp[i] = i / coins[0];
            else dp[i] = 999999;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= value; j++) {
                int notTake = dp[j];
                int take = 999999;
                if (coins[i] <= j) take = 1 + curr[j - coins[i]];

                curr[j] = Math.min(notTake, take);
            }
            dp = curr;
            curr = new int[value + 1];
        }

        return dp[value];
    }
}
