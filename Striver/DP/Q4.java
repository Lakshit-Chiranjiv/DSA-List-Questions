package Striver.DP;

public class Q4 {
    // frog jump problem - k jumps allowed

    // recursive solution - Time: O(k^n) Space: O(n)
    public static int frogJump(int n, int k, int[] cost){
        if(n == 0)
            return 0;

        int minVal = Integer.MAX_VALUE;
        for(int i = 1;i<=k;i++){
            if(n-i >= 0){
                int left = frogJump(n-i, k, cost) + Math.abs(cost[n] - cost[n-i]);
                minVal = Math.min(minVal, left);
            }
        }
        return minVal;
    }

    // memoization - Time: O(n*k) Space: O(n)
    public static int frogJumpMemo(int n, int k, int[] cost, int[] dp){
        if(n == 0)
            return 0;
        if(dp[n] != -1)
            return dp[n];

        int minVal = Integer.MAX_VALUE;
        for(int i = 1;i<=k;i++){
            if(n-i >= 0){
                int left = frogJumpMemo(n-i, k, cost, dp) + Math.abs(cost[n] - cost[n-i]);
                minVal = Math.min(minVal, left);
            }
        }
        return dp[n] = minVal;
    }

    // tabulation - Time: O(n*k) Space: O(n)
    public static int frogJumpTab(int n, int k, int[] cost){
        int[] dp = new int[n+1];
        dp[0] = 0;
        for(int i = 1;i<=n;i++){
            int minVal = Integer.MAX_VALUE;
            for(int j = 1;j<=k;j++){
                if(i-j >= 0){
                    int left = dp[i-j] + Math.abs(cost[i] - cost[i-j]);
                    minVal = Math.min(minVal, left);
                }
            }
            dp[i] = minVal;
        }
        return dp[n];
    }

    // space optimization - Time: O(n*k) Space: O(k)
    public static int frogJumpTabOpt(int n, int k, int[] cost){
        int[] dp = new int[k+1];
        dp[0] = 0;
        for(int i = 1;i<=n;i++){
            int minVal = Integer.MAX_VALUE;
            for(int j = 1;j<=k;j++){
                if(i-j >= 0){
                    int left = dp[j] + Math.abs(cost[i] - cost[i-j]);
                    minVal = Math.min(minVal, left);
                }
            }
            dp[i%k] = minVal;
        }
        return dp[n%k];
    }

    public static void main(String[] args) {
        int n = 5;
        int k = 3;
        int[] cost = {0, 10, 30, 40, 50, 60};
        int[] dp = new int[n+1];
        for(int i = 0;i<=n;i++)
            dp[i] = -1;
        System.out.println(frogJump(n, k, cost));
        System.out.println(frogJumpMemo(n, k, cost, dp));
        System.out.println(frogJumpTab(n, k, cost));
        System.out.println(frogJumpTabOpt(n, k, cost));
    }
}
