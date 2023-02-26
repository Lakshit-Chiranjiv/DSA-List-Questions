package Striver.DP;

public class Q35 {
    // best time to buy and sell stock 

    public static int maxProfit(int[] prices) {
        int n = prices.length;
        int[] dp = new int[n];
        dp[0] = 0;
        int min = prices[0];
        for(int i=1; i<n; i++){
            min = Math.min(min, prices[i]);
            dp[i] = Math.max(dp[i-1], prices[i]-min);
        }
        return dp[n-1];
    }

    public static void main(String[] args) {
        int[] prices = {7,1,5,3,6,4};
        System.out.println(maxProfit(prices));
    }
}
