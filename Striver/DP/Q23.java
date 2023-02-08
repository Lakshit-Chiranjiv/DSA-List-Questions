package Striver.DP;

public class Q23 {
    // Unbounded Knapsack Problem

    // recursive solution - Time: O(2^n) Space: O(n)
    public static int unboundedKnapsack(int[] wt, int[] val, int W, int n) {
        if(n == 0){
            return (int)((W/wt[n])*val[n]);
        }
        int notTake = unboundedKnapsack(wt, val, W, n-1);
        int take = 0;
        if(W >= wt[n]){
            take = unboundedKnapsack(wt, val, W-wt[n], n) + val[n];
        }
        return Math.max(notTake, take);
    }

    // memoization - Time: O(n*W) Space: O(n*W)
    public static int unboundedKnapsackMemo(int[] wt, int[] val, int W, int n, int[][] dp) {
        if(n == 0){
            return (int)((W/wt[n])*val[n]);
        }
        if(dp[n][W] != -1){
            return dp[n][W];
        }
        int notTake = unboundedKnapsackMemo(wt, val, W, n-1, dp);
        int take = 0;
        if(W >= wt[n]){
            take = unboundedKnapsackMemo(wt, val, W-wt[n], n, dp) + val[n];
        }
        return dp[n][W] = Math.max(notTake, take);
    }

    // tabulation - Time: O(n*W) Space: O(n*W)
    public static int unboundedKnapsackTab(int[] wt, int[] val, int W, int n) {
        int[][] dp = new int[n][W+1];

        for(int i = 0; i <= W; i++){
            dp[0][i] = (int)((i/wt[0])*val[0]);
        }

        for(int i = 1; i < n; i++){
            for(int j = 0; j <= W; j++){
                int notTake = dp[i-1][j];
                int take = 0;
                if(j >= wt[i]){
                    take = dp[i][j-wt[i]] + val[i];
                }
                dp[i][j] = Math.max(notTake, take);
            }
        }

        return dp[n-1][W];
    }

    // space optimization - Time: O(n*W) Space: O(W)
    public static int unboundedKnapsackSpaceOpt(int[] wt, int[] val, int W, int n) {
        int[] dp = new int[W+1];
        int[] curr = new int[W+1];

        for(int i = 0; i <= W; i++){
            dp[i] = (int)((i/wt[0])*val[0]);
        }

        for(int i = 1; i < n; i++){
            for(int j = 0; j <= W; j++){
                int notTake = dp[j];
                int take = 0;
                if(j >= wt[i]){
                    take = curr[j-wt[i]] + val[i];
                }
                curr[j] = Math.max(notTake, take);
            }
            dp = curr;
            curr = new int[W+1];
        }

        return dp[W];
    }

    public static void main(String[] args) {
        int[] wt = {1, 3, 4, 5};
        int[] val = {10, 40, 50, 70};
        int W = 8;
        int n = wt.length-1;

        System.out.println(unboundedKnapsack(wt, val, W, n));
        System.out.println(unboundedKnapsackMemo(wt, val, W, n, new int[n+1][W+1]));
        System.out.println(unboundedKnapsackTab(wt, val, W, n));
        System.out.println(unboundedKnapsackSpaceOpt(wt, val, W, n));
    }
}