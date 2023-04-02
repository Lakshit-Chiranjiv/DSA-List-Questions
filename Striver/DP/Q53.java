package Striver.DP;

public class Q53 {
    // palindrome partitioning II

    public boolean isPalindrome(String s, int i, int j){
        while (i < j){
            if (s.charAt(i) != s.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }

    // recursive solution - Time: O(2^n) Space: O(n)
    public int minCut(String s, int i){
        if (i == s.length()) return 0;
        int min = Integer.MAX_VALUE;

        for (int j = i; j < s.length(); j++) {
            if (isPalindrome(s, i, j)){
                int cuts = 1 + minCut(s, j+1);
                min = Math.min(min, cuts);
            }
        }

        return min;
    }

    // memoization - Time: O(n^2) Space: O(n)
    public int minCutMem(String s, int i, int[] dp){
        if (i == s.length()) return 0;
        if (dp[i] != -1) return dp[i];
        int min = Integer.MAX_VALUE;

        for (int j = i; j < s.length(); j++) {
            if (isPalindrome(s, i, j)){
                int cuts = 1 + minCutMem(s, j+1, dp);
                min = Math.min(min, cuts);
            }
        }

        return dp[i] = min;
    }

    // tabulation - Time: O(n^2) Space: O(n^2)
    public int minCutTab(String s){
        int n = s.length();
        int[] dp = new int[n+1];

        dp[n] = 0;

        for(int i = n-1; i >= 0; i--){
            int min = Integer.MAX_VALUE;
            for (int j = i; j < n; j++) {
                if (isPalindrome(s, i, j)){
                    int cuts = 1 + dp[j+1];
                    min = Math.min(min, cuts);
                }
            }
            dp[i] = min;
        }

        return dp[0] - 1;
    }

    public static void main(String[] args) {
        Q53 q = new Q53();
        String s = "aab";
        System.out.println(q.minCut(s, 0) - 1);
        int[] dp = new int[s.length()];
        for (int i = 0; i < s.length(); i++) dp[i] = -1;
        System.out.println(q.minCutMem(s, 0, dp) - 1);
        System.out.println(q.minCutTab(s));
    }
}
