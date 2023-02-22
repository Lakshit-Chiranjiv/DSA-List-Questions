package Striver.DP;

import java.util.Arrays;

public class Q32{
    // Distinct Subsequences
    // return the number of distinct subsequences of S which equals T

    // Recursive solution: Time: O(2^n) Space: O(n)
    public int numDistinct(String s, String t, int n, int m){
        if(m == 0) return 1;
        if(n == 0) return 0;
        if(s.charAt(n-1) == t.charAt(m-1))
            return numDistinct(s, t, n-1, m-1) + numDistinct(s, t, n-1, m);
        else
            return numDistinct(s, t, n-1, m);
    }

    // Memoization: Time: O(n*m) Space: O(n*m)
    public int numDistinctMem(String s, String t, int n, int m, int[][] dp){
        if(m == 0) return dp[n][m] = 1;
        if(n == 0) return dp[n][m] = 0;
        if(dp[n][m] != -1) return dp[n][m];
        if(s.charAt(n-1) == t.charAt(m-1))
            return dp[n][m] = numDistinctMem(s, t, n-1, m-1, dp) + numDistinctMem(s, t, n-1, m, dp);
        else
            return dp[n][m] = numDistinctMem(s, t, n-1, m, dp);
    }

    // Tabulation: Time: O(n*m) Space: O(n*m)
    public int numDistinctTab(String s, String t, int n, int m){
        int[][] dp = new int[n+1][m+1];
        for(int i = 0; i <= n; i++)
            dp[i][0] = 1;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(s.charAt(i-1) == t.charAt(j-1))
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                else
                    dp[i][j] = dp[i-1][j];
            }
        }
        return dp[n][m];
    }

    // Space Optimization: Time: O(n*m) Space: O(m)
    public int numDistinctOpt(String s, String t, int n, int m){
        int[] dp = new int[m+1];
        dp[0] = 1;
        for(int i = 1; i <= n; i++){
            for(int j = m; j >= 1; j--){
                if(s.charAt(i-1) == t.charAt(j-1))
                    dp[j] += dp[j-1];
            }
        }
        return dp[m];
    }

    public static void main(String[] args) {
        Q32 q = new Q32();
        String s = "rabbbit";
        String t = "rabbit";
        int n = s.length();
        int m = t.length();
        System.out.println(q.numDistinct(s, t, n, m));
        int[][] dp = new int[n+1][m+1];
        for(int[] d: dp)
            Arrays.fill(d, -1);
        System.out.println(q.numDistinctMem(s, t, n, m, dp));
        System.out.println(q.numDistinctTab(s, t, n, m));
        System.out.println(q.numDistinctOpt(s, t, n, m));
    }
}