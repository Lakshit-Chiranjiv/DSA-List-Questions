package Striver.DP;

public class Q19{
    // 0/1 Knapsack Problem
    // Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

    // recursive solution - Time: O(2^n) Space: O(n)
    public static int knapsack(int[] wt, int[] val, int idx, int W){
        if (idx == 0) {
            if (wt[idx] <= W) return val[idx];
            else return 0;
        }

        int notTake = knapsack(wt, val, idx-1, W);
        int take = Integer.MIN_VALUE;
        if (wt[idx] <= W) take = val[idx] + knapsack(wt, val, idx-1, W-wt[idx]);
        return Math.max(notTake, take);
    }

    // memoization - Time: O(n*W) Space: O(n*W)
    public static int knapsackMemo(int[] wt, int[] val, int idx, int W, int[][] dp){
        if (idx == 0) {
            if (wt[idx] <= W) return val[idx];
            else return 0;
        }

        if (dp[idx][W] != -1) return dp[idx][W];

        int notTake = knapsackMemo(wt, val, idx-1, W, dp);
        int take = Integer.MIN_VALUE;
        if (wt[idx] <= W) take = val[idx] + knapsackMemo(wt, val, idx-1, W-wt[idx], dp);
        return dp[idx][W] = Math.max(notTake, take);
    }

    // tabulation - Time: O(n*W) Space: O(n*W)
    public static int knapsackTab(int[] wt, int[] val, int idx, int W){
        int[][] dp = new int[idx+1][W+1];
        for (int i = wt[0]; i <= W; i++) dp[0][i] = val[0];
        for (int i = 1; i <= idx; i++) {
            for (int j = 0; j <= W; j++) {
                int notTake = dp[i-1][j];
                int take = Integer.MIN_VALUE;
                if (wt[i] <= j) take = val[i] + dp[i-1][j-wt[i]];
                dp[i][j] = Math.max(notTake, take);
            }
        }
        return dp[idx][W];
    }

    // space optimization with 2 rows - curr and dp - Time: O(n*W) Space: O(2*W)
    public static int knapsackTab2(int[] wt, int[] val, int idx, int W){
        int[] dp = new int[W+1];
        int[] curr = new int[W+1];
        for (int i = wt[0]; i <= W; i++) dp[i] = val[0];
        for (int i = 1; i <= idx; i++) {
            for (int j = 0; j <= W; j++) {
                int notTake = dp[j];
                int take = Integer.MIN_VALUE;
                if (wt[i] <= j) take = val[i] + dp[j-wt[i]];
                curr[j] = Math.max(notTake, take);
            }
            int[] temp = dp;
            dp = curr;
            curr = temp;
        }
        return dp[W];
    }

    // space optimization with 1 row - Time: O(n*W) Space: O(W)
    public static int knapsackTab3(int[] wt, int[] val, int idx, int W){
        int[] dp = new int[W+1];
        for (int i = wt[0]; i <= W; i++) dp[i] = val[0];
        for (int i = 1; i <= idx; i++) {
            for (int j = W; j >= 0; j--) {
                int notTake = dp[j];
                int take = Integer.MIN_VALUE;
                if (wt[i] <= j) take = val[i] + dp[j-wt[i]];
                dp[j] = Math.max(notTake, take);
            }
        }
        return dp[W];
    }

    public static void main(String[] args) {
        int[] wt = {1, 3, 4, 5};
        int[] val = {1, 4, 5, 7};
        int W = 7;
        int idx = wt.length-1;
        System.out.println(knapsack(wt, val, idx, W));
        int[][] dp = new int[idx+1][W+1];
        for (int[] row: dp) java.util.Arrays.fill(row, -1);
        System.out.println(knapsackMemo(wt, val, idx, W, dp));
        System.out.println(knapsackTab(wt, val, idx, W));
        System.out.println(knapsackTab2(wt, val, idx, W));
        System.out.println(knapsackTab3(wt, val, idx, W));
    }
}