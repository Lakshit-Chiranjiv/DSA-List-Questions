package Striver.DP;

public class Q36{
    // buy and sell stock part 2

    // recursive solution - Time: O(2^n) Space: O(n)
    public int maxProfit(int[] prices, int idx, int buy){
        if(idx == prices.length)
            return 0;
        
        if(buy == 1){
            int buying = maxProfit(prices, idx+1, 0) - prices[idx];
            int notBuying = maxProfit(prices, idx+1, 1);
            return Math.max(buying, notBuying);
        }
        else{
            int selling = maxProfit(prices, idx+1, 1) + prices[idx];
            int notSelling = maxProfit(prices, idx+1, 0);
            return Math.max(selling, notSelling);
        }
    }

    // memoization - Time: O(n^2) Space: O(n^2)
    public int maxProfitMem(int[] prices, int idx, int buy, int[][] dp){
        if(idx == prices.length)
            return 0;
        
        if(dp[idx][buy] != -1)
            return dp[idx][buy];
        
        if(buy == 1){
            int buying = maxProfitMem(prices, idx+1, 0, dp) - prices[idx];
            int notBuying = maxProfitMem(prices, idx+1, 1, dp);
            return dp[idx][buy] = Math.max(buying, notBuying);
        }
        else{
            int selling = maxProfitMem(prices, idx+1, 1, dp) + prices[idx];
            int notSelling = maxProfitMem(prices, idx+1, 0, dp);
            return dp[idx][buy] = Math.max(selling, notSelling);
        }
    }

    // tabulation - Time: O(n^2) Space: O(n^2)
    public int maxProfitTab(int[] prices){
        int n = prices.length;
        int[][] dp = new int[n+1][2];
        dp[n][0] = dp[n][1] = 0;

        for(int i = n-1; i >= 0; i--){
            for(int j = 0; j < 2; j++){
                if(j == 1){
                    int buying = dp[i+1][0] - prices[i];
                    int notBuying = dp[i+1][1];
                    dp[i][j] = Math.max(buying, notBuying);
                }
                else{
                    int selling = dp[i+1][1] + prices[i];
                    int notSelling = dp[i+1][0];
                    dp[i][j] = Math.max(selling, notSelling);
                }
            }
        }

        return dp[0][1];
    }

    // space optimization - Time: O(n^2) Space: O(n)
    public int maxProfitSpaceOpt(int[] prices){
        int n = prices.length;
        int[] ahead = new int[2];
        int[] curr = new int[2];
        ahead[0] = ahead[1] = 0;

        for(int i = n-1; i >= 0; i--){
            for(int j = 0; j < 2; j++){
                if(j == 1){
                    int buying = ahead[0] - prices[i];
                    int notBuying = ahead[1];
                    curr[j] = Math.max(buying, notBuying);
                }
                else{
                    int selling = ahead[1] + prices[i];
                    int notSelling = ahead[0];
                    curr[j] = Math.max(selling, notSelling);
                }
            }
            for(int j = 0; j < 2; j++)
                ahead[j] = curr[j];
        }

        return ahead[1];
    }

    //space optimization with variable - Time: O(n^2) Space: O(1)
    public int maxProfitSpaceOptVar(int[] prices){
        int n = prices.length;
        int aheadNotBuying = 0, aheadBuying = 0, currNotBuying, currBuying;

        for(int i = n-1; i >= 0; i--){
            currNotBuying = Math.max(aheadBuying + prices[i], aheadNotBuying);
            currBuying = Math.max(aheadNotBuying - prices[i], aheadBuying);
            aheadBuying = currBuying;
            aheadNotBuying = currNotBuying;
        }

        return aheadBuying;
    }

    public static void main(String[] args) {
        Q36 obj = new Q36();
        int[] prices = {7,1,5,3,6,4};
        System.out.println(obj.maxProfit(prices, 0, 1));
        int[][] dp = new int[prices.length+1][2];
        for(int i = 0; i < dp.length; i++)
            for(int j = 0; j < dp[0].length; j++)
                dp[i][j] = -1;
        System.out.println(obj.maxProfitMem(prices, 0, 1, dp));
        System.out.println(obj.maxProfitTab(prices));
        System.out.println(obj.maxProfitSpaceOpt(prices));
        System.out.println(obj.maxProfitSpaceOptVar(prices));
    }
}