package Striver.DP;

public class Q1 {
    // fibonacci number

    //recursive solution - Time complexity: O(2^n), Space complexity: O(n)
    public static int fib(int n){
        if(n==0 || n==1) return n;
        return fib(n-1) + fib(n-2);
    }

    //memoization - Time complexity: O(n), Space complexity: O(n)
    public static int fib_memo(int n, int[] dp){
        if(n==0 || n==1) return n;
        if(dp[n]!=-1) return dp[n];
        dp[n] = fib_memo(n-1, dp) + fib_memo(n-2, dp);
        return dp[n];
    }

    //tabulation - Time complexity: O(n), Space complexity: O(n)
    public static int fib_tab(int n){
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;
        for(int i=2; i<=n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }

    //space optimization - Time complexity: O(n), Space complexity: O(1)
    public static int fib_sp(int n){
        int a = 0, b = 1, c = 0;
        for(int i=2; i<=n; i++){
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    public static void main(String[] args) {
        int n = 10;
        int[] dp = new int[n+1];
        for(int i=0; i<=n; i++) dp[i] = -1;
        System.out.println(fib(n));
        System.out.println(fib_memo(n, dp));
        System.out.println(fib_tab(n));
        System.out.println(fib_sp(n));
    }
}
