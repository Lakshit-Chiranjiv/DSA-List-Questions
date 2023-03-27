package Striver.DP;

import java.util.Arrays;

public class Q48{
    // matrix chain multiplication

    // recursive solution - Time: O(2^n) | Space: O(n)
    public static int solve(int[] arr, int i, int j){
        if(i == j) return 0;
        int min = Integer.MAX_VALUE;
        for(int k = i; k < j; k++){
            int steps = solve(arr, i, k) + solve(arr, k+1, j) + arr[i-1]*arr[k]*arr[j];
            min = Math.min(min, steps);
        }
        return min;
    }

    // memoization - Time: O(n^3) | Space: O(n^2)
    public static int solve(int[] arr, int i, int j, int[][] dp){
        if(i == j) return 0;
        if(dp[i][j] != -1) return dp[i][j];
        int min = Integer.MAX_VALUE;
        for(int k = i; k < j; k++){
            int steps = solve(arr, i, k, dp) + solve(arr, k+1, j, dp) + arr[i-1]*arr[k]*arr[j];
            min = Math.min(min, steps);
        }
        return dp[i][j] = min;
    }

    public static void main(String[] args){
        int[] arr = {40, 20, 30, 10, 30};
        int n = arr.length;
        System.out.println(solve(arr, 1, n-1));
        int[][] dp = new int[n][n];
        for(int[] row: dp) Arrays.fill(row, -1);
        System.out.println(solve(arr, 1, n-1, dp));
    }
}