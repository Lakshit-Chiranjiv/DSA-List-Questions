package Striver.DP;

public class Q22{
    // coins change 2 
    // given coins of different denominations and a total amount of money
    // write a function to compute the number of combinations that make up that amount
    // you may assume that you have infinite number of each kind of coin

    // recursive solution - Time: O(2^n) Space: O(n)
    public int coinsChange(int[] coins, int idx, int amount){
        if (idx == 0){
            if (amount % coins[idx] == 0) return 1;
            else return 0;
        }

        int notTake = coinsChange(coins, idx-1, amount);
        int take = 0;
        if (amount >= coins[idx]) take = coinsChange(coins, idx, amount-coins[idx]);
        return notTake + take;
    }

    // memoization - Time: O(n*amount) Space: O(n*amount)
    public int coinsChangeMem(int[] coins, int idx, int amount, int[][] dp){
        if (idx == 0){
            if (amount % coins[idx] == 0) return dp[idx][amount] = 1;
            else return dp[idx][amount] = 0;
        }

        if (dp[idx][amount] != -1) return dp[idx][amount];

        int notTake = coinsChangeMem(coins, idx-1, amount, dp);
        int take = 0;
        if (amount >= coins[idx]) take = coinsChangeMem(coins, idx, amount-coins[idx], dp);
        return dp[idx][amount] = notTake + take;
    }

    // tabulation - Time: O(n*amount) Space: O(n*amount)
    public int coinsChangeTab(int[] coins, int amount){
        int n = coins.length;
        int[][] dp = new int[n][amount+1];

        for (int i=0; i<=amount; i++){
            if (i % coins[0] == 0) dp[0][i] = 1;
            else dp[0][i] = 0;
        }

        for (int i=1; i<n; i++){
            for (int j=0; j<=amount; j++){
                int notTake = dp[i-1][j];
                int take = 0;
                if (j >= coins[i]) take = dp[i][j-coins[i]];
                dp[i][j] = notTake + take;
            }
        }

        return dp[n-1][amount];
    }

    // space optimization - Time: O(n*amount) Space: O(amount)
    public int coinsChangeTabOpt(int[] coins, int amount){
        int n = coins.length;
        int[] dp = new int[amount+1];
        int[] curr = new int[amount+1];

        for (int i=0; i<=amount; i++){
            if (i % coins[0] == 0) dp[i] = 1;
            else dp[i] = 0;
        }

        for (int i=1; i<n; i++){
            for (int j=0; j<=amount; j++){
                int notTake = dp[j];
                int take = 0;
                if (j >= coins[i]) take = curr[j-coins[i]];
                curr[j] = notTake + take;
            }
            dp = curr;
            curr = new int[amount+1];
        }

        return dp[amount];
    }

    public static void main(String[] args) {
        Q22 q = new Q22();
        int[] coins = {1,2,5};
        int amount = 5;
        System.out.println(q.coinsChange(coins, coins.length-1, amount));
        int[][] dp = new int[coins.length][amount+1];
        for (int i=0; i<coins.length; i++){
            for (int j=0; j<=amount; j++){
                dp[i][j] = -1;
            }
        }
        System.out.println(q.coinsChangeMem(coins, coins.length-1, amount, dp));
        System.out.println(q.coinsChangeTab(coins, amount));
        System.out.println(q.coinsChangeTabOpt(coins, amount));
    }

}