package Striver.DP;

public class Q11 {
    // right angled triangle with n rows and each row has i+1 elements
    // find the minimum sum path from top (0,0) to any element in last row
    // you can move only to down or diagonally right down

    // recursive solution - Time: O(2^n) Space: O(n)
    public static int minPathSum(int[][] arr, int n, int i, int j) {
        if (i == n - 1) return arr[i][j];
        int down = minPathSum(arr, n, i + 1, j);
        int diagRight = minPathSum(arr, n, i + 1, j + 1);
        return arr[i][j] + Math.min(down, diagRight);
    }

    // memoization - Time: O(n^2) Space: O(n^2)
    public static int minPathSumMemo(int[][] arr, int n, int i, int j, int[][] dp) {
        if (i == n - 1) return arr[i][j];
        if (dp[i][j] != -1) return dp[i][j];
        int down = minPathSumMemo(arr, n, i + 1, j, dp);
        int diagRight = minPathSumMemo(arr, n, i + 1, j + 1, dp);
        return dp[i][j] = arr[i][j] + Math.min(down, diagRight);
    }

    // tabulation - Time: O(n^2) Space: O(n^2)
    public static int minPathSumTab(int[][] arr, int n) {
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) dp[n - 1][i] = arr[n - 1][i];
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                dp[i][j] = arr[i][j] + Math.min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        return dp[0][0];
    }

    // space optimization - Time: O(n^2) Space: O(n)
    public static int minPathSumSpaceOpt(int[][] arr, int n) {
        int[] dp = new int[n];
        int[] temp = new int[n];
        for (int i = 0; i < n; i++) dp[i] = arr[n - 1][i];
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                temp[j] = arr[i][j] + Math.min(dp[j], dp[j + 1]);
            }
            dp = temp;
        }
        return dp[0];
    }

    public static void main(String[] args) {
        int[][] arr = {{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}};
        int n = arr.length;
        System.out.println(minPathSum(arr, n, 0, 0));
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) dp[i][j] = -1;
        System.out.println(minPathSumMemo(arr, n, 0, 0, dp));
        System.out.println(minPathSumTab(arr, n));
        System.out.println(minPathSumSpaceOpt(arr, n));
    }
}
