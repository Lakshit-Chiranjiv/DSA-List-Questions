package Striver.DP;

public class Q9 {
    // unique paths in grid with obstacles from (0,0) to (m-1,n-1)
    // you can only move right or down
    // 0 - no obstacle
    // 1 - obstacle

    // recursive solution - Time: O(2^(m+n)) Space: O(m+n)
    public static int countPaths(int m, int n, int[][] grid) {
        if (m == 0 || n == 0) return 1;
        if (m < 0 || n < 0) return 0;
        if (grid[m][n] == 1) return 0;
        return countPaths(m - 1, n, grid) + countPaths(m, n - 1, grid);
    }

    // memoization - Time: O(m*n) Space: O(m*n)
    public static int countPathsMemo(int m, int n, int[][] dp, int[][] grid) {
        if (m == 0 || n == 0) return 1;
        if (m < 0 || n < 0) return 0;
        if (grid[m][n] == 1) return 0;
        if (dp[m][n] != -1) return dp[m][n];
        return dp[m][n] = countPathsMemo(m - 1, n, dp, grid) + countPathsMemo(m, n - 1, dp, grid);
    }

    // tabulation - Time: O(m*n) Space: O(m*n)
    public static int countPathsTab(int m, int n, int[][] grid) {
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0 && j > 0 && grid[i][j] == 1){
                    dp[i][j] = 0;
                    continue;
                }
                if (i == 0 || j == 0) dp[i][j] = 1;
                else if(i > 0 && j > 0) dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m-1][n-1];
    }

    // space optimization - Time: O(m*n) Space: O(n)
    public static int countPathsSpaceOpt(int m, int n, int[][] grid) {
        int[] dp = new int[n];
        for (int i = 0; i < m; i++) {
            int[] temp = new int[n];
            for (int j = 0; j < n; j++) {
                if (i > 0 && j > 0 && grid[i][j] == 1){
                    temp[j] = 0;
                    continue;
                }
                if (i == 0 || j == 0) temp[j] = 1;
                else if(i > 0 && j > 0) temp[j] = dp[j] + temp[j - 1];
            }
            dp = temp;
        }
        return dp[n-1];
    }

    public static void main(String[] args) {
        int m = 3, n = 3;
        int[][] grid = new int[m][n];
        grid[1][1] = 1;
        System.out.println(countPaths(m - 1, n - 1, grid));
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = -1;
            }
        }
        System.out.println(countPathsMemo(m - 1, n - 1, dp, grid));
        System.out.println(countPathsTab(m, n, grid));
        System.out.println(countPathsSpaceOpt(m, n, grid));
    }
}
