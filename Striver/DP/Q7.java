package Striver.DP;

import java.util.Arrays;

public class Q7 {
    // Ninja's Training Problem
    // Ninja can train in 3 ways and can't train the same training 2 days in a row
    // each training has a profit associated with it for each day
    // find the max profit that ninja can earn in n days
    // given Nx3 matrix where N is the number of days and 3 is the number of trainings

    // recursive solution - Time: O(3^n) Space: O(n)
    public static int maxProfit(int[][] arr, int n, int prev) {
        if (n == 0){
            int max = 0;
            for (int i = 0; i < 3; i++) {
                if (i != prev)
                    max = Math.max(max, arr[0][i]);
            }
            return max;
        }
        int max = 0;
        for (int i = 0; i < 3; i++) {
            if (i != prev)
                max = Math.max(max, arr[n][i] + maxProfit(arr, n - 1, i));
        }
        return max;
    }

    // memoization - Time: O(n) Space: O(n)
    public static int maxProfit(int[][] arr, int n, int prev, int[][] dp) {
        
        if (dp[n][prev] != -1)
            return dp[n][prev];
        
        if (n == 0){
            int max = 0;
            for (int i = 0; i < 3; i++) {
                if (i != prev)
                    max = Math.max(max, arr[0][i]);
            }
            return dp[n][prev] = max;
        }

        int max = 0;
        for (int i = 0; i < 3; i++) {
            if (i != prev)
                max = Math.max(max, arr[n][i] + maxProfit(arr, n - 1, i, dp));
        }
        return dp[n][prev] = max;
    }

    // tabulation - Time: O(n) Space: O(n)
    public static int maxProfit(int[][] arr, int n) {
        int[][] dp = new int[n + 1][4];
        dp[0][0] = Math.max(arr[0][1], arr[0][2]);
        dp[0][1] = Math.max(arr[0][0], arr[0][2]);
        dp[0][2] = Math.max(arr[0][0], arr[0][1]);
        dp[0][3] = Math.max(dp[0][0], Math.max(dp[0][1], dp[0][2]));
        for (int i = 1; i < n; i++) {
            for (int prev = 0; prev < 4; prev++) {
                int max = 0;
                for (int j = 0; j < 3; j++) {
                    if (j != prev)
                        max = Math.max(max, arr[i][j] + dp[i - 1][j]);
                }
                dp[i][prev] = max;
            }
        }
        return dp[n - 1][3];
    }

    // space optimization - Time: O(n) Space: O(1)
    public static int maxProfit2(int[][] arr, int n) {
        int[] prev = new int[4];
        prev[0] = Math.max(arr[0][1], arr[0][2]);
        prev[1] = Math.max(arr[0][0], arr[0][2]);
        prev[2] = Math.max(arr[0][0], arr[0][1]);
        prev[3] = Math.max(prev[0], Math.max(prev[1], prev[2]));

        for (int i = 1; i < n; i++) {
            int[] curr = new int[4];
            for (int prevIdx = 0; prevIdx < 4; prevIdx++) {
                int max = 0;
                for (int j = 0; j < 3; j++) {
                    if (j != prevIdx)
                        max = Math.max(max, arr[i][j] + prev[j]);
                }
                curr[prevIdx] = max;
            }
            prev = curr;
        }
        return prev[3];
    }

    public static void main(String[] args) {
        int[][] arr = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int n = arr.length;
        System.out.println(maxProfit(arr, n - 1, 3));
        int[][] dp = new int[n + 1][4];
        for (int[] row : dp)
            Arrays.fill(row, -1);
        System.out.println(maxProfit(arr, n - 1, 3, dp));
        System.out.println(maxProfit(arr, n));
        System.out.println(maxProfit2(arr, n));
    }
}
