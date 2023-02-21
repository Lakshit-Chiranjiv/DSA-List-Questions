package Striver.DP;

import java.util.Arrays;

public class Q31{
    // minimum common supersequence - length and print the sequence
    // length ans will be sum of length of both string - lcs

    // recursive solution: Time: O(2^n) Space: O(n)
    public static int lcs(String s1, String s2, int n, int m){
        if(n < 0 || m < 0) return 0;
        if(s1.charAt(n) == s2.charAt(m)) return 1 + lcs(s1, s2, n-1, m-1);
        else return Math.max(lcs(s1, s2, n-1, m), lcs(s1, s2, n, m-1));
    }

    public static int mcs(String s1, String s2, int n, int m){
        return s1.length() + s2.length() - lcs(s1, s2, n, m);
    }

    public static String mcs_print(String s1, String s2, int n, int m){
        if(n < 0 || m < 0) return "";
        if(s1.charAt(n) == s2.charAt(m)) return mcs_print(s1, s2, n-1, m-1) + s1.charAt(n);
        else{
            String s1_ans = mcs_print(s1, s2, n-1, m);
            String s2_ans = mcs_print(s1, s2, n, m-1);
            return s1_ans.length() > s2_ans.length() ? s1_ans : s2_ans;
        }
    }

    // memoization: Time: O(n*m) Space: O(n*m)
    public static int lcs_memo(String s1, String s2, int n, int m, int[][] dp){
        if(n < 0 || m < 0) return 0;
        if(dp[n][m] != -1) return dp[n][m];
        if(s1.charAt(n) == s2.charAt(m)) return dp[n][m] = 1 + lcs_memo(s1, s2, n-1, m-1, dp);
        else return dp[n][m] = Math.max(lcs_memo(s1, s2, n-1, m, dp), lcs_memo(s1, s2, n, m-1, dp));
    }

    public static int mcs_memo(String s1, String s2, int n, int m, int[][] dp){
        return s1.length() + s2.length() - lcs_memo(s1, s2, n, m, dp);
    }

    public static String mcs_print_memo(String s1, String s2, int n, int m, int[][] dp){
        if(n < 0 || m < 0) return "";
        if(dp[n][m] != -1) return "";
        if(s1.charAt(n) == s2.charAt(m)) return mcs_print_memo(s1, s2, n-1, m-1, dp) + s1.charAt(n);
        else{
            String s1_ans = mcs_print_memo(s1, s2, n-1, m, dp);
            String s2_ans = mcs_print_memo(s1, s2, n, m-1, dp);
            return s1_ans.length() > s2_ans.length() ? s1_ans : s2_ans;
        }
    }

    // tabulation: Time: O(n*m) Space: O(n*m)
    public static int lcs_tab(String s1, String s2, int n, int m){
        int[][] dp = new int[n+1][m+1];
        for(int i = 0; i <= m; i++) dp[0][i] = 0;
        for(int i = 0; i <= n; i++) dp[i][0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(s1.charAt(i-1) == s2.charAt(j-1)) dp[i][j] = 1 + dp[i-1][j-1];
                else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }

        return dp[n][m];
    }

    public static int mcs_tab(String s1, String s2, int n, int m){
        return s1.length() + s2.length() - lcs_tab(s1, s2, n, m);
    }

    public static void mcs_print_tab(String s1, String s2, int n, int m){
        int[][] dp = new int[n+1][m+1];
        for(int i = 0; i <= m; i++) dp[0][i] = 0;
        for(int i = 0; i <= n; i++) dp[i][0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(s1.charAt(i-1) == s2.charAt(j-1)) dp[i][j] = 1 + dp[i-1][j-1];
                else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }

        int i = n, j = m;
        String ans = "";
        while(i > 0 && j > 0){
            if(s1.charAt(i-1) == s2.charAt(j-1)){
                ans = s1.charAt(i-1) + ans;
                i--;
                j--;
            }
            else{
                if(dp[i-1][j] > dp[i][j-1]) i--;
                else j--;
            }
        }

        System.out.println(ans);
    }

    // space optimization: Time: O(n*m) Space: O(n)
    public static int lcs_tab_opt(String s1, String s2, int n, int m){
        int[] dp = new int[m+1];
        int[] curr = new int[m+1];
        for(int i = 0; i <= m; i++) dp[i] = 0;

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(s1.charAt(i-1) == s2.charAt(j-1)) curr[j] = 1 + dp[j-1];
                else curr[j] = Math.max(dp[j], curr[j-1]);
            }
            for(int j = 0; j <= m; j++) dp[j] = curr[j];
        }

        return dp[m];
    }

    public static int mcs_tab_opt(String s1, String s2, int n, int m){
        return s1.length() + s2.length() - lcs_tab_opt(s1, s2, n, m);
    }

    public static void mcs_print_tab_opt(String s1, String s2, int n, int m){
        int[] dp = new int[m+1];
        int[] curr = new int[m+1];
        for(int i = 0; i <= m; i++) dp[i] = 0;

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(s1.charAt(i-1) == s2.charAt(j-1)) curr[j] = 1 + dp[j-1];
                else curr[j] = Math.max(dp[j], curr[j-1]);
            }
            for(int j = 0; j <= m; j++) dp[j] = curr[j];
        }

        int i = n, j = m;
        String ans = "";
        while(i > 0 && j > 0){
            if(s1.charAt(i-1) == s2.charAt(j-1)){
                ans = s1.charAt(i-1) + ans;
                i--;
                j--;
            }
            else{
                if(dp[j] > curr[j-1]) i--;
                else j--;
            }
        }

        System.out.println(ans);
    }

    public static void main(String[] args) {
        String s1 = "abcdaf";
        String s2 = "acbcf";
        int n = s1.length();
        int m = s2.length();
        int[][] dp = new int[n][m];
        for(int[] d: dp) Arrays.fill(d, -1);
        System.out.println(mcs_memo(s1, s2, n-1, m-1, dp));
        System.out.println(mcs_print_memo(s1, s2, n-1, m-1, dp));
        System.out.println(mcs_tab(s1, s2, n, m));
        mcs_print_tab(s1, s2, n, m);
        System.out.println(mcs_tab_opt(s1, s2, n, m));
        mcs_print_tab_opt(s1, s2, n, m);
    }
}