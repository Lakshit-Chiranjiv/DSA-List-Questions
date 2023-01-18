package Striver.DP;

public class Q10{
    // min cost path in grid from (0,0) to (n-1,m-1)
    // only right and down moves are allowed

    // recursive solution - Time: O(2^(n+m)) Space: O(n+m)
    public static int minCostPath(int[][] grid, int n, int m){
        if(n==0 && m==0) return grid[0][0];
        if(n<0 || m<0) return Integer.MAX_VALUE;
        return grid[n][m] + Math.min(minCostPath(grid, n-1, m), minCostPath(grid, n, m-1));
    }

    // memoization - Time: O(n*m) Space: O(n*m)
    public static int minCostPathMemo(int[][] grid, int n, int m, int[][] dp){
        if(n==0 && m==0) return grid[0][0];
        if(n<0 || m<0) return Integer.MAX_VALUE;
        if(dp[n][m] != -1) return dp[n][m];
        return dp[n][m] = grid[n][m] + Math.min(minCostPathMemo(grid, n-1, m, dp), minCostPathMemo(grid, n, m-1, dp));
    }

    // tabulation - Time: O(n*m) Space: O(n*m)
    public static int minCostPathTab(int[][] grid, int n, int m){
        int[][] dp = new int[n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(i==0 && j==0) dp[i][j] = grid[i][j];
                else if(i==0) dp[i][j] = grid[i][j] + dp[i][j-1];
                else if(j==0) dp[i][j] = grid[i][j] + dp[i-1][j];
                else dp[i][j] = grid[i][j] + Math.min(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[n-1][m-1];
    }

    // space optimization - Time: O(n*m) Space: O(m)
    public static int minCostPathSpaceOpt(int[][] grid, int m, int n){
        int[] dp = new int[n];
        for (int i = 0; i < m; i++) {
            int[] temp = new int[n];
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) temp[j] = grid[i][j];
                else temp[j] = grid[i][j] + Math.min(dp[j], temp[j - 1]);
            }
            dp = temp;
        }
        return dp[n-1];
    }

    public static void main(String[] args) {
        int[][] grid = {{1,3,5,8},{4,2,1,7},{4,3,2,3}};
        int n = grid.length;
        int m = grid[0].length;
        System.out.println(minCostPath(grid, n-1, m-1));
        int[][] dp = new int[n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                dp[i][j] = -1;
            }
        }
        System.out.println(minCostPathMemo(grid, n-1, m-1, dp));
        System.out.println(minCostPathTab(grid, n, m));
        System.out.println(minCostPathSpaceOpt(grid, m, n));
    }
}