package Striver.DP;

public class Q33 {
    // edit distance
    // minimum number of operations to convert word1 to word2
    // allowed operations:
    // insert a character
    // delete a character
    // replace a character

    //recursive solution - Time: O(3^n) Space: O(n)
    public static int minDistance(String word1, String word2, int i, int j) {
        if(i<0){
            return j+1;
        }
        if(j<0){
            return i+1;
        }

        if(word1.charAt(i)==word2.charAt(j)){
            return minDistance(word1, word2, i-1, j-1);
        }

        int insert = minDistance(word1, word2, i, j-1);
        int delete = minDistance(word1, word2, i-1, j);
        int replace = minDistance(word1, word2, i-1, j-1);

        return 1 + Math.min(insert, Math.min(delete, replace));
    }

    // memoization - Time: O(m*n) Space: O(m*n)
    public static int minDistance_memo(String word1, String word2, int i, int j, int[][] dp) {
        if(i<0){
            return j+1;
        }
        if(j<0){
            return i+1;
        }

        if(dp[i][j]!=0){
            return dp[i][j];
        }

        if(word1.charAt(i)==word2.charAt(j)){
            return minDistance_memo(word1, word2, i-1, j-1, dp);
        }

        int insert = minDistance_memo(word1, word2, i, j-1, dp);
        int delete = minDistance_memo(word1, word2, i-1, j, dp);
        int replace = minDistance_memo(word1, word2, i-1, j-1, dp);

        dp[i][j] = 1 + Math.min(insert, Math.min(delete, replace));
        return dp[i][j];
    }

    // tabulation - Time: O(m*n) Space: O(m*n)
    public static int minDistance_tab(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        int[][] dp = new int[n+1][m+1];

        for(int i=0; i<=n; i++){
            dp[i][0] = i;
        }

        for(int j=0; j<=m; j++){
            dp[0][j] = j;
        }

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(word1.charAt(i-1)==word2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1];
                }else{
                    int insert = dp[i][j-1];
                    int delete = dp[i-1][j];
                    int replace = dp[i-1][j-1];
                    dp[i][j] = 1 + Math.min(insert, Math.min(delete, replace));
                }
            }
        }
        return dp[n][m];
    }

    // space optimization - Time: O(m*n) Space: O(n)
    public static int minDistance_space_opt(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        int[] dp = new int[m+1];
        int[] curr = new int[m+1];

        for(int j=0; j<=m; j++){
            dp[j] = j;
        }

        for(int i = 1; i <= n; i++){
            curr[0] = i;
            for(int j = 1; j <= m; j++){
                if(word1.charAt(i-1)==word2.charAt(j-1)){
                    curr[j] = dp[j-1];
                }else{
                    int insert = curr[j-1];
                    int delete = dp[j];
                    int replace = dp[j-1];
                    curr[j] = 1 + Math.min(insert, Math.min(delete, replace));
                }
            }
        }
        return dp[m];
    }

    public static void main(String[] args) {
        String word1 = "horse";
        String word2 = "ros";
        int i = word1.length()-1;
        int j = word2.length()-1;
        int[][] dp = new int[i+1][j+1];
        System.out.println(minDistance(word1, word2, i, j));
        System.out.println(minDistance_memo(word1, word2, i, j, dp));
        System.out.println(minDistance_tab(word1, word2));
        System.out.println(minDistance_space_opt(word1, word2));
    }
    
}
