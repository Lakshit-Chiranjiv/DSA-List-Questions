package Striver.DP;

public class Q28{
    // longest palindromic subsequence length

    // recursive solution: Time: O(2^n) Space: O(n)
    public static int lcs(String s1, String s2, int n, int m){
        if(n < 0 || m < 0) return 0;
        if(s1.charAt(n) == s2.charAt(m)) return 1 + lcs(s1, s2, n-1, m-1);
        else return Math.max(lcs(s1, s2, n-1, m), lcs(s1, s2, n, m-1));
    }

    public static int longest_palindromic_subsequence(String s){
        String s2 = new StringBuilder(s).reverse().toString();
        return lcs(s, s2, s.length()-1, s2.length()-1);
    }

    // memoization: Time: O(n*m) Space: O(n*m)
    public static int lcs_memo(String s1, String s2, int n, int m, int[][] dp){
        if(n < 0 || m < 0) return 0;
        if(dp[n][m] != -1) return dp[n][m];
        if(s1.charAt(n) == s2.charAt(m)) return dp[n][m] = 1 + lcs_memo(s1, s2, n-1, m-1, dp);
        else return dp[n][m] = Math.max(lcs_memo(s1, s2, n-1, m, dp), lcs_memo(s1, s2, n, m-1, dp));
    }

    public static int longest_palindromic_subsequence_memo(String s){
        String s2 = new StringBuilder(s).reverse().toString();
        int n = s.length();
        int m = s2.length();
        int[][] dp = new int[n][m];
        for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) dp[i][j] = -1;
        return lcs_memo(s, s2, n-1, m-1, dp);
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

    public static int longest_palindromic_subsequence_tab(String s){
        String s2 = new StringBuilder(s).reverse().toString();
        int n = s.length();
        int m = s2.length();
        return lcs_tab(s, s2, n, m);
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

    public static int longest_palindromic_subsequence_tab_opt(String s){
        String s2 = new StringBuilder(s).reverse().toString();
        int n = s.length();
        int m = s2.length();
        return lcs_tab_opt(s, s2, n, m);
    }

    public static void main(String[] args){
        String s = "agbcba";
        System.out.println(longest_palindromic_subsequence(s));
        System.out.println(longest_palindromic_subsequence_memo(s));
        System.out.println(longest_palindromic_subsequence_tab(s));
        System.out.println(longest_palindromic_subsequence_tab_opt(s));
    }
}