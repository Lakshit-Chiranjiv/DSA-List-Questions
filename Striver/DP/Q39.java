package Striver.DP;

public class Q39{
    // buy and sell stock with cooldown
    // can't buy on the next day after selling

    // recursive solution - Time: O(2^n) Space: O(n)
    public int maxProfit(int[] prices, int idx, int buy){
        if(idx >= prices.length)
            return 0;
        
        if(buy == 1){
            int buying = maxProfit(prices, idx+1, 0) - prices[idx];
            int notBuying = maxProfit(prices, idx+1, 1);
            return Math.max(buying, notBuying);
        }
        else{
            int selling = maxProfit(prices, idx+2, 1) + prices[idx];
            int notSelling = maxProfit(prices, idx+1, 0);
            return Math.max(selling, notSelling);
        }
    }

    // memoization - Time: O(n^2) Space: O(n^2)
    public int maxProfitMem(int[] prices, int idx, int buy, int[][] dp){
        if(idx >= prices.length)
            return 0;
        
        if(dp[idx][buy] != -1)
            return dp[idx][buy];
        
        if(buy == 1){
            int buying = maxProfitMem(prices, idx+1, 0, dp) - prices[idx];
            int notBuying = maxProfitMem(prices, idx+1, 1, dp);
            return dp[idx][buy] = Math.max(buying, notBuying);
        }
        else{
            int selling = maxProfitMem(prices, idx+2, 1, dp) + prices[idx];
            int notSelling = maxProfitMem(prices, idx+1, 0, dp);
            return dp[idx][buy] = Math.max(selling, notSelling);
        }
    }

    // tabulation - Time: O(n^2) Space: O(n^2)
    public int maxProfitTab(int[] prices){
        int n = prices.length;
        int[][] dp = new int[n+2][2];
        dp[n][0] = dp[n][1] = 0;

        for(int i = n-1; i >= 0; i--){
            for(int j = 0; j < 2; j++){
                if(j == 1){
                    int buying = dp[i+1][0] - prices[i];
                    int notBuying = dp[i+1][1];
                    dp[i][j] = Math.max(buying, notBuying);
                }
                else{
                    int selling = dp[i+2][1] + prices[i];
                    int notSelling = dp[i+1][0];
                    dp[i][j] = Math.max(selling, notSelling);
                }
            }
        }

        return dp[0][1];
    }

}