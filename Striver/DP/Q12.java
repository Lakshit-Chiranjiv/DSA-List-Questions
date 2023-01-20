package Striver.DP;

public class Q12 {
    // Maximum Falling Path Sum | Variable Starting and Ending Points

    // Given a grid of M x N integers, find the maximum sum of a falling path from any cell in the first row to any cell in the last row.

    // recursive solution - Time: O(3^N), Space: O(N)
    public static int maxFallingPathSum(int i, int j, int[][] grid) {
        
        if (j < 0 || j >= grid[0].length) {
            return Integer.MIN_VALUE;
        }
        
        if (i == 0) {
            return grid[i][j];
        }

        int up = maxFallingPathSum(i - 1, j, grid);
        int leftUpperDiag = maxFallingPathSum(i - 1, j - 1, grid);
        int rightUpperDiag = maxFallingPathSum(i - 1, j + 1, grid);

        return grid[i][j] + Math.max(up, Math.max(leftUpperDiag, rightUpperDiag));
    }

    public static int findMaxFallingPathSum(int[][] grid) {
        int maxSum = Integer.MIN_VALUE;

        for (int j = 0; j < grid[0].length; j++) {
            maxSum = Math.max(maxSum, maxFallingPathSum(grid.length - 1, j, grid));
        }

        return maxSum;
    }

    // memoization - Time: O(M*N), Space: O(M*N)
    public static int maxFallingPathSumMem(int i, int j, int[][] grid, int[][] dp) {
        
        if (j < 0 || j >= grid[0].length) {
            return Integer.MIN_VALUE;
        }
        
        if (i == 0) {
            return grid[i][j];
        }

        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        int up = maxFallingPathSumMem(i - 1, j, grid, dp);
        int leftUpperDiag = maxFallingPathSumMem(i - 1, j - 1, grid, dp);
        int rightUpperDiag = maxFallingPathSumMem(i - 1, j + 1, grid, dp);

        return dp[i][j] = grid[i][j] + Math.max(up, Math.max(leftUpperDiag, rightUpperDiag));
    }

    public static int findMaxFallingPathSum2(int[][] grid) {
        int maxSum = Integer.MIN_VALUE;
        int[][] dp = new int[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                dp[i][j] = -1;
            }
        }

        for (int j = 0; j < grid[0].length; j++) {
            maxSum = Math.max(maxSum, maxFallingPathSumMem(grid.length - 1, j, grid, dp));
        }

        return maxSum;
    }

    // tabulation - Time: O(M*N), Space: O(M*N)
    public static int maxFallingPathSumTab(int[][] grid){
        int n = grid.length;
        int m = grid[0].length;
        int[][] dp = new int[n][m];
        for(int j = 0; j < m; j++){
            dp[0][j] = grid[0][j];
        }

        for(int i = 1; i < n; i++){
            for(int j = 0; j < m; j++){
                int up = dp[i - 1][j];
                int leftUpperDiag = j - 1 >= 0 ? dp[i - 1][j - 1] : Integer.MIN_VALUE;
                int rightUpperDiag = j + 1 < m ? dp[i - 1][j + 1] : Integer.MIN_VALUE;
                dp[i][j] = grid[i][j] + Math.max(up, Math.max(leftUpperDiag, rightUpperDiag));
            }
        }

        int maxSum = Integer.MIN_VALUE;
        for(int j = 0; j < m; j++){
            maxSum = Math.max(maxSum, dp[n - 1][j]);
        }

        return maxSum;
    }

    // space optimization - Time: O(M*N), Space: O(N)
    public static int maxFallingPathSumSpaceOpt(int[][] grid){
        int n = grid.length;
        int m = grid[0].length;
        int[] dp = new int[m];
        for(int j = 0; j < m; j++){
            dp[j] = grid[0][j];
        }

        for(int i = 1; i < n; i++){
            int[] temp = new int[m];
            for(int j = 0; j < m; j++){
                int up = dp[j];
                int leftUpperDiag = j - 1 >= 0 ? dp[j - 1] : Integer.MIN_VALUE;
                int rightUpperDiag = j + 1 < m ? dp[j + 1] : Integer.MIN_VALUE;
                temp[j] = grid[i][j] + Math.max(up, Math.max(leftUpperDiag, rightUpperDiag));
            }
            dp = temp;
        }

        int maxSum = Integer.MIN_VALUE;
        for(int j = 0; j < m; j++){
            maxSum = Math.max(maxSum, dp[j]);
        }

        return maxSum;
    }

}
