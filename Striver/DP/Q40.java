package Striver.DP;

public class Q40 {
    // buy and sell stocks with transaction fee
    // you can buy and sell multiple times

    // recursive solution - Time: O(2^n) Space: O(n)
    public int maxProfit(int[] prices, int idx, int buy, int fee){
        if(idx == prices.length)
            return 0;
        
        if(buy == 1){
            int buying = maxProfit(prices, idx+1, 0, fee) - prices[idx];
            int notBuying = maxProfit(prices, idx+1, 1, fee);
            return Math.max(buying, notBuying);
        }
        else{
            int selling = maxProfit(prices, idx+1, 1, fee) + prices[idx] - fee;
            int notSelling = maxProfit(prices, idx+1, 0, fee);
            return Math.max(selling, notSelling);
        }
    }

    // memoization - Time: O(n^2) Space: O(n^2)
    public int maxProfitMem(int[] prices, int idx, int buy, int[][] dp, int fee){
        if(idx == prices.length)
            return 0;
        
        if(dp[idx][buy] != -1)
            return dp[idx][buy];
        
        if(buy == 1){
            int buying = maxProfitMem(prices, idx+1, 0, dp, fee) - prices[idx];
            int notBuying = maxProfitMem(prices, idx+1, 1, dp, fee);
            return dp[idx][buy] = Math.max(buying, notBuying);
        }
        else{
            int selling = maxProfitMem(prices, idx+1, 1, dp, fee) + prices[idx] - fee;
            int notSelling = maxProfitMem(prices, idx+1, 0, dp, fee);
            return dp[idx][buy] = Math.max(selling, notSelling);
        }
    }

    // tabulation - Time: O(n^2) Space: O(n^2)
    public int maxProfitTab(int[] prices, int fee){
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
                    int selling = dp[i+1][1] + prices[i] - fee;
                    int notSelling = dp[i+1][0];
                    dp[i][j] = Math.max(selling, notSelling);
                }
            }
        }

        return dp[0][1];
    }

    // space optimization - Time: O(n^2) Space: O(n)
    public int maxProfitSpaceOpt(int[] prices, int fee){
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
                    int selling = ahead[1] + prices[i] - fee;
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
    public int maxProfitSpaceOptVar(int[] prices, int fee){
        int n = prices.length;
        int aheadNotBuying = 0, aheadBuying = 0, currNotBuying, currBuying;

        for(int i = n-1; i >= 0; i--){
            currNotBuying = Math.max(aheadBuying + prices[i] - fee, aheadNotBuying);
            currBuying = Math.max(aheadNotBuying - prices[i], aheadBuying);
            aheadBuying = currBuying;
            aheadNotBuying = currNotBuying;
        }

        return aheadBuying;
    }

    public static void main(String[] args) {
        Q40 obj = new Q40();
        int[] prices = {1, 3, 2, 8, 4, 9};
        int fee = 2;
        System.out.println(obj.maxProfit(prices, 0, 1, fee));
        int[][] dp = new int[prices.length+1][2];
        for(int i = 0; i < dp.length; i++)
            for(int j = 0; j < dp[0].length; j++)
                dp[i][j] = -1;
        System.out.println(obj.maxProfitMem(prices, 0, 1, dp, fee));
        System.out.println(obj.maxProfitTab(prices, fee));
        System.out.println(obj.maxProfitSpaceOpt(prices, fee));
        System.out.println(obj.maxProfitSpaceOptVar(prices, fee));
    }
}
