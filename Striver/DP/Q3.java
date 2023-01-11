package Striver.DP;

public class Q3 {
    // frog jump problem for 1 or 2 jumps

    // recursive solution
    public static int frogJump(int n, int[] cost){
        if(n == 0)
            return 0;
        int left = frogJump(n-1, cost) + Math.abs(cost[n] - cost[n-1]);
        int right = Integer.MAX_VALUE;
        if(n >= 2)
            right = frogJump(n-2, cost) + Math.abs(cost[n] - cost[n-2]);
        return Math.min(left, right);
    }

    // memoization
    public static int frogJumpMemo(int n, int[] cost, int[] dp){
        if(n == 0)
            return 0;
        if(dp[n] != -1)
            return dp[n];
        int left = frogJumpMemo(n-1, cost, dp) + Math.abs(cost[n] - cost[n-1]);
        int right = Integer.MAX_VALUE;
        if(n >= 2)
            right = frogJumpMemo(n-2, cost, dp) + Math.abs(cost[n] - cost[n-2]);
        return dp[n] = Math.min(left, right);
    }

    // tabulation
    public static int frogJumpTab(int n, int[] cost){
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = Math.abs(cost[1] - cost[0]);
        for(int i = 2;i<=n;i++){
            int left = dp[i-1] + Math.abs(cost[i] - cost[i-1]);
            int right = dp[i-2] + Math.abs(cost[i] - cost[i-2]);
            dp[i] = Math.min(left, right);
        }
        return dp[n];
    }

    // space optimization
    public static int frogJumpTabOpt(int n, int[] cost){
        int a = 0;
        int b = Math.abs(cost[1] - cost[0]);
        for(int i = 2;i<=n;i++){
            int left = b + Math.abs(cost[i] - cost[i-1]);
            int right = a + Math.abs(cost[i] - cost[i-2]);
            a = b;
            b = Math.min(left, right);
        }
        return b;
    }

    public static void main(String[] args) {
        int[] cost = {10, 30, 40, 20};
        int n = cost.length - 1;
        System.out.println(frogJump(n, cost));
        int[] dp = new int[n+1];
        for(int i = 0;i<=n;i++)
            dp[i] = -1;
        System.out.println(frogJumpMemo(n, cost, dp));
        System.out.println(frogJumpTab(n, cost));
        System.out.println(frogJumpTabOpt(n, cost));
    }

}
