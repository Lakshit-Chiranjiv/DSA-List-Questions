package Aman_Bhaiya_DSA_List.Strings;

public class LQ50 {
    // longest palindromic substring using dp

    // recursive solution - Time: O(2^n) Space: O(n)
    public static String longestPalindromicSubstring(String s, int l, int r){
        if(l > r) return "";
        if(l == r) return s.charAt(l) + "";
        if(isPalindrome(s, l, r)) return s.substring(l, r+1);
        String left = longestPalindromicSubstring(s, l+1, r);
        String right = longestPalindromicSubstring(s, l, r-1);
        return left.length() > right.length() ? left : right;
    }

    private static boolean isPalindrome(String s, int l, int r) {
        while(l < r){
            if(s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }

    // memoization - Time: O(n^2) Space: O(n^2)
    public static String longestPalindromicSubstring(String s){
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        int maxLen = 0;
        String ans = "";
        for (int g = 0; g < n; g++) {
            for (int i = 0, j = g; j < n; i++, j++) {
                if(g == 0) dp[i][j] = true;
                else if(g == 1) dp[i][j] = s.charAt(i) == s.charAt(j);
                else dp[i][j] = s.charAt(i) == s.charAt(j) && dp[i+1][j-1];

                if(dp[i][j] && g+1 > maxLen){
                    maxLen = g+1;
                    ans = s.substring(i, j+1);
                }
            }
        }
        return ans;
    }
}
