package Striver.DP;

public class Q34{
    // wildcard string matching
    // ? can be replaced by any single character
    // * can be replaced by any sequence of characters or empty sequence

    // recursive solution - Time: O(2^n) Space: O(n)
    public boolean isMatch(String s, String p, int i, int j){
        if(i < 0 && j < 0) return true;
        if(i < 0 && j >= 0) return false;
        if(j < 0 && i >= 0) {
            for(int k = 0; k <= i; k++){
                if(s.charAt(k) != '*') return false;
            }
            return true;
        }

        if(s.charAt(i) == p.charAt(j) || s.charAt(i) == '?') return isMatch(s, p, i-1, j-1);
        if(s.charAt(i) == '*'){
            return isMatch(s, p, i-1, j) || isMatch(s, p, i, j-1);
        }

        return false;
    }

    // memoization - Time: O(n^2) Space: O(n^2)
    public boolean isMatchMem(String s, String p, int i, int j, int[][] dp){
        if(i < 0 && j < 0) return true;
        if(i < 0 && j >= 0) return false;
        if(j < 0 && i >= 0) {
            for(int k = 0; k <= i; k++){
                if(s.charAt(k) != '*') return false;
            }
            return true;
        }

        if(dp[i][j] != -1) return dp[i][j] == 1;

        if(s.charAt(i) == p.charAt(j) || s.charAt(i) == '?'){
            
            dp[i][j] = isMatchMem(s, p, i-1, j-1, dp) ? 1 : 0;
            return dp[i][j] == 1;
        } 
        if(s.charAt(i) == '*'){
            dp[i][j] = (isMatchMem(s, p, i-1, j, dp) || isMatchMem(s, p, i, j-1, dp)) ? 1 : 0;
            return dp[i][j] == 1;
        }

        dp[i][j] = 0;
        return false;
    }

    // tabulation - Time: O(n^2) Space: O(n^2)
    public boolean isMatchTab(String s, String p){
        int n = s.length(), m = p.length();
        boolean[][] dp = new boolean[n+1][m+1];
        dp[0][0] = true;
        for(int j = 1; j <=m; j++){
            dp[0][j] = false;
        }

        for(int i = 1; i <= n; i++){
            boolean flag = true;
            for(int k = 1; k <= i; k++){
                if(s.charAt(k-1) != '*'){
                    flag = false;
                    break;
                }
            }
            dp[i][0] = flag;
        }

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(s.charAt(i-1) == p.charAt(j-1) || s.charAt(i-1) == '?') dp[i][j] = dp[i-1][j-1];
                else if(s.charAt(i-1) == '*') dp[i][j] = dp[i-1][j] || dp[i][j-1];
                else dp[i][j] = false;
            }
        }

        return dp[n][m];
    }

    // space optimization - Time: O(n^2) Space: O(n)
    public boolean isMatchOpt(String s, String p){
        int n = s.length(), m = p.length();
        boolean[] dp = new boolean[m+1];
        boolean[] curr = new boolean[m+1];
        dp[0] = true;
        for(int j = 1; j <=m; j++){
            dp[j] = false;
        }

        for(int i = 1; i <= n; i++){
            boolean flag = true;
            for(int k = 1; k <= i; k++){
                if(s.charAt(k-1) == '*'){
                    flag = false;
                    break;
                }
            }
            curr[0] = flag;
            for(int j = 1; j <= m; j++){
                if(s.charAt(i-1) == p.charAt(j-1) || s.charAt(i-1) == '?') curr[j] = dp[j-1];
                else if(s.charAt(i-1) == '*') curr[j] = dp[j] || curr[j-1];
                else curr[j] = false;
            }
            for(int j = 0; j <= m; j++){
                dp[j] = curr[j];
            }
        }

        return dp[m];
    }

    public static void main(String[] args) {
        Q34 q = new Q34();
        String s = "ba*****ab";
        String p = "baxnab";
        System.out.println(q.isMatch(s, p, s.length()-1, p.length()-1));
        int[][] dp = new int[s.length()][p.length()];
        for(int i = 0; i < s.length(); i++){
            for(int j = 0; j < p.length(); j++){
                dp[i][j] = -1;
            }
        }
        System.out.println(q.isMatchMem(s, p, s.length()-1, p.length()-1, dp));
        System.out.println(q.isMatchTab(s, p));
        System.out.println(q.isMatchOpt(s, p));
    }

}