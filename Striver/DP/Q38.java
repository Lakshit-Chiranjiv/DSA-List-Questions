package Striver.DP;

public class Q38{
    // buy and sell stock part 4
    // atmost k transactions allowed

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
    public int maxProfitTab(int[] prices, int k){
        int n = prices.length;
        int[][][] dp = new int[n+1][2][k+1];

        for(int i = n-1; i >= 0; i--){
            for(int j = 0; j < 2; j++){
                for(int z = 1; z <= k; z++){
                    if(j == 1){
                        int buying = dp[i+1][0][z] - prices[i];
                        int notBuying = dp[i+1][1][z];
                        dp[i][j][z] = Math.max(buying, notBuying);
                    }
                    else{
                        int selling = dp[i+1][1][z-1] + prices[i];
                        int notSelling = dp[i+1][0][z];
                        dp[i][j][z] = Math.max(selling, notSelling);
                    }
                }
            }
        }

        return dp[0][1][k];
    }

    // space optimization - Time: O(n^3) Space: O(n^2)
    public int maxProfitSpaceOpt(int[] prices, int k){
        int n = prices.length;
        int[][] after = new int[2][k+1];
        int[][] curr = new int[2][k+1];

        for(int i = n-1; i >= 0; i--){
            for(int j = 0; j < 2; j++){
                for(int z = 1; z <= k; z++){
                    if(j == 1){
                        int buying = after[0][z] - prices[i];
                        int notBuying = after[1][z];
                        curr[j][z] = Math.max(buying, notBuying);
                    }
                    else{
                        int selling = after[1][z-1] + prices[i];
                        int notSelling = after[0][z];
                        curr[j][z] = Math.max(selling, notSelling);
                    }
                }
            }
            for(int buy = 0; buy < 2; buy++)
                for(int cap = 1; cap <= k; cap++)
                    after[buy][cap] = curr[buy][cap];
        }

        return after[1][k];
    }

    public static void main(String[] args) {
        Q38 obj = new Q38();
        int[] prices = {3,3,5,0,0,3,1,4};
        int k = 4;
        System.out.println(obj.maxProfit(prices, 0, 1, k));
        int[][][] dp = new int[prices.length][2][k+1];
        for(int i = 0; i < prices.length; i++)
            for(int j = 0; j < 2; j++)
                for(int z = 0; z <= k; z++)
                    dp[i][j][z] = -1;
        System.out.println(obj.maxProfitMem(prices, 0, 1, k, dp));
        System.out.println(obj.maxProfitTab(prices, k));
        System.out.println(obj.maxProfitSpaceOpt(prices, k));
    }

}