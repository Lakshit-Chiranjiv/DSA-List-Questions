package Striver.DP;

public class Q26{
    // print the longest common subsequence using tabulation method
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

        return dp[n][m];
    }

    public static void main(String[] args){
        String s1 = "abcdgh";
        String s2 = "abedfhr";
        int n = s1.length();
        int m = s2.length();
        System.out.println(lcs_tab(s1, s2, n, m));
    }
}