package Striver.DP;

public class Q37{
    // buy and sell stocks part 3
    // can buy and sell atmost 2 times

    // recursive solution - Time: O(2^n) Space: O(n)
    public int maxProfit(int[] prices, int idx, int buy, int cap){
        if(cap == 0)
            return 0;

        if(idx == prices.length)
            return 0;
        
        if(buy == 1){
            int buying = maxProfit(prices, idx+1, 0, cap) - prices[idx];
            int notBuying = maxProfit(prices, idx+1, 1, cap);
            return Math.max(buying, notBuying);
        }
        else{
            int selling = maxProfit(prices, idx+1, 1, cap-1) + prices[idx];
            int notSelling = maxProfit(prices, idx+1, 0, cap);
            return Math.max(selling, notSelling);
        }
    }

    // memoization - Time: O(n^3) Space: O(n^3)
    public int maxProfitMem(int[] prices, int idx, int buy, int cap, int[][][] dp){
        if(cap == 0)
            return 0;

        if(idx == prices.length)
            return 0;
        
        if(dp[idx][buy][cap] != -1)
            return dp[idx][buy][cap];
        
        if(buy == 1){
            int buying = maxProfitMem(prices, idx+1, 0, cap, dp) - prices[idx];
            int notBuying = maxProfitMem(prices, idx+1, 1, cap, dp);
            return dp[idx][buy][cap] = Math.max(buying, notBuying);
        }
        else{
            int selling = maxProfitMem(prices, idx+1, 1, cap-1, dp) + prices[idx];
            int notSelling = maxProfitMem(prices, idx+1, 0, cap, dp);
            return dp[idx][buy][cap] = Math.max(selling, notSelling);
        }
    }

    // tabulation - Time: O(n^3) Space: O(n^3)
    public int maxProfitTab(int[] prices){
        int n = prices.length;
        int[][][] dp = new int[n+1][2][3];

        for(int i = n-1; i >= 0; i--){
            for(int j = 0; j < 2; j++){
                for(int k = 1; k < 3; k++){
                    if(j == 1){
                        int buying = dp[i+1][0][k] - prices[i];
                        int notBuying = dp[i+1][1][k];
                        dp[i][j][k] = Math.max(buying, notBuying);
                    }
                    else{
                        int selling = dp[i+1][1][k-1] + prices[i];
                        int notSelling = dp[i+1][0][k];
                        dp[i][j][k] = Math.max(selling, notSelling);
                    }
                }
            }
        }

        return dp[0][1][2];
    }

    // space optimization - Time: O(n^3) Space: O(n^2)
    public int maxProfitSpaceOpt(int[] prices){
        int n = prices.length;
        int[][] after = new int[2][3];
        int[][] curr = new int[2][3];

        for(int i = n-1; i >= 0; i--){
            for(int j = 0; j < 2; j++){
                for(int k = 1; k < 3; k++){
                    if(j == 1){
                        int buying = after[0][k] - prices[i];
                        int notBuying = after[1][k];
                        curr[j][k] = Math.max(buying, notBuying);
                    }
                    else{
                        int selling = after[1][k-1] + prices[i];
                        int notSelling = after[0][k];
                        curr[j][k] = Math.max(selling, notSelling);
                    }
                }
            }
            for(int buy = 0; buy < 2; buy++)
                for(int cap = 1; cap < 3; cap++)
                    after[buy][cap] = curr[buy][cap];
        }

        return after[1][2];
    }

    public static void main(String[] args) {
        Q37 obj = new Q37();
        int[] prices = {3,3,5,0,0,3,1,4};
        System.out.println(obj.maxProfit(prices, 0, 1, 2));
        int[][][] dp = new int[prices.length][2][3];
        for(int i = 0; i < prices.length; i++)
            for(int j = 0; j < 2; j++)
                for(int k = 0; k < 3; k++)
                    dp[i][j][k] = -1;
        System.out.println(obj.maxProfitMem(prices, 0, 1, 2, dp));
        System.out.println(obj.maxProfitTab(prices));
        System.out.println(obj.maxProfitSpaceOpt(prices));
    }

    
}