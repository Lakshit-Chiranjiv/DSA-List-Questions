package Striver.DP;

public class Q24{
    // Rod Cutting Problem
    // maximize the profit by cutting the rod into pieces and selling them at different prices

    // Recursive Solution: Time: O(2^n) Space: O(n)
    public static int maxProfit(int[] prices, int idx, int N){
        if(idx == 0){
            return (N * prices[0]);
        }

        int notTake = maxProfit(prices, idx - 1, N);
        int take = Integer.MIN_VALUE;
        int rodLength = idx + 1;
        if(N >= rodLength){
            take = maxProfit(prices, idx, N - rodLength) + prices[idx];
        }

        return Math.max(notTake, take);
    }

    // Memoization: Time: O(n^2) Space: O(n^2)
    public static int maxProfitMem(int[] prices, int idx, int N, int[][] dp){
        if(idx == 0){
            return (N * prices[0]);
        }

        if(dp[idx][N] != -1){
            return dp[idx][N];
        }

        int notTake = maxProfitMem(prices, idx - 1, N, dp);
        int take = Integer.MIN_VALUE;
        int rodLength = idx + 1;
        if(N >= rodLength){
            take = maxProfitMem(prices, idx, N - rodLength, dp) + prices[idx];
        }

        return dp[idx][N] = Math.max(notTake, take);
    }

    // Tabulation: Time: O(n^2) Space: O(n^2)
    public static int maxProfitTab(int[] prices, int N){
        int[][] dp = new int[prices.length][N + 1];
        
        for(int i = 0; i <= N; i++){
            dp[0][i] = i * prices[0];
        }

        for(int i = 1; i < prices.length; i++){
            for(int j = 0; j <= N; j++){
                int notTake = dp[i - 1][j];
                int take = Integer.MIN_VALUE;
                int rodLength = i + 1;
                if(j >= rodLength){
                    take = dp[i][j - rodLength] + prices[i];
                }

                dp[i][j] = Math.max(notTake, take);
            }
        }

        return dp[prices.length - 1][N];
    }

    // Space Optimization: Time: O(n^2) Space: O(n)
    public static int maxProfitSpOpt(int[] prices, int N){
        int[] dp = new int[N + 1];
        for(int i = 0; i <= N; i++){
            dp[i] = i * prices[0];
        }

        for(int i = 1; i < prices.length; i++){
            for(int j = N; j >= 0; j--){
                int notTake = dp[j];
                int take = Integer.MIN_VALUE;
                int rodLength = i + 1;
                if(j >= rodLength){
                    take = dp[j - rodLength] + prices[i];
                }

                dp[j] = Math.max(notTake, take);
            }
        }

        return dp[N];
    }

    public static void main(String[] args){
        int[] prices = {1, 5, 8, 9, 10, 17, 17, 20};
        int N = 8;
        System.out.println(maxProfit(prices, prices.length - 1, N));
        System.out.println(maxProfitMem(prices, prices.length - 1, N, new int[prices.length][N + 1]));
        System.out.println(maxProfitTab(prices, N));
        System.out.println(maxProfitSpOpt(prices, N));
    }
}