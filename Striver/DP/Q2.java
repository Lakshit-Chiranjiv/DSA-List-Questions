package Striver.DP;

class Q2{
    // climbing stairs problem

    //recursive solution
    public static int climbStairs(int n) {
        if(n==0 || n==1){
            return 1;
        }
        return climbStairs(n-1) + climbStairs(n-2);
    }

    //memoization
    public static int climbStairs_memo(int n, int[] dp) {
        if(n==0 || n==1){
            return 1;
        }
        if(dp[n]!=0){
            return dp[n];
        }
        dp[n] = climbStairs_memo(n-1, dp) + climbStairs_memo(n-2, dp);
        return dp[n];
    }

    //tabulation
    public static int climbStairs_tab(int n) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for(int i=2; i<=n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }

    //space optimization
    public static int climbStairs_opt(int n) {
        if(n==0 || n==1){
            return 1;
        }
        int a = 1;
        int b = 1;
        int c = 0;
        for(int i=2; i<=n; i++){
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    public static void main(String[] args) {
        int n = 4;
        System.out.println(climbStairs(n));
        int[] dp = new int[n+1];
        System.out.println(climbStairs_memo(n, dp));
        System.out.println(climbStairs_tab(n));
        System.out.println(climbStairs_opt(n));
    }
}