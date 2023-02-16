package Striver.DP;

public class Q27 {
    // longest common substring

    // tabulation: Time: O(n*m) Space: O(n*m)

    public static int lcs_tab(String s1, String s2, int n, int m){
        int[][] dp = new int[n+1][m+1];
        int ansLen = 0;
        for(int i = 0; i <= m; i++) dp[0][i] = 0;
        for(int i = 0; i <= n; i++) dp[i][0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(s1.charAt(i-1) == s2.charAt(j-1)){
                    dp[i][j] = 1 + dp[i-1][j-1];
                    ansLen = Math.max(ansLen, dp[i][j]);
                }
                else dp[i][j] = 0;
            }
        }

        return ansLen;
    }
}