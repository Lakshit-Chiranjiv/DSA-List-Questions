package Aman_Bhaiya_DSA_List.Strings;

public class LQ53 {
    // Count Palindromic Subsequences
    public static void main(String[] args) {
        String str = "abcb";
        System.out.println(countPS(str));
    }

    public static long countPS(String str) {
        int n = str.length();
        long[][] dp = new long[n][n];
        long mod = 1000000007;

        for (int g = 0; g < n; g++) {
            for (int i = 0, j = g; j < n; i++, j++) {
                if (g == 0) {
                    dp[i][j] = 1;
                } else if (g == 1) {
                    dp[i][j] = str.charAt(i) == str.charAt(j) ? 3 : 2;
                } else {
                    if (str.charAt(i) == str.charAt(j)) {
                        dp[i][j] = (dp[i][j - 1] + dp[i + 1][j] + 1) % mod;
                    } else {
                        dp[i][j] = (dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]) % mod;
                    }
                }
            }
        }
        return dp[0][n - 1];
    }
}
