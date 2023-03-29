package Striver.DP;

import java.util.Arrays;

public class Q50{
    // Minimum Cost to Cut the Stick

    // recursive solution - Time: O(2^n) Space: O(n)
    public static int minCost(int[] arr, int i, int j){
        if(i > j) return 0;
        int min = Integer.MAX_VALUE;
        for(int k = i; k <= j; k++){
            int temp = minCost(arr, i, k-1) + minCost(arr, k+1, j) + arr[j+1] - arr[i-1];
            min = Math.min(min, temp);
        }

        return min;
    }

    // memoization - Time: O(n^3) Space: O(n^2)
    public static int minCostMemo(int[] arr, int i, int j, int[][] dp){
        if(i > j) return 0;
        if(dp[i][j] != 0) return dp[i][j];
        int min = Integer.MAX_VALUE;
        for(int k = i; k <= j; k++){
            int temp = minCostMemo(arr, i, k-1, dp) + minCostMemo(arr, k+1, j, dp) + arr[j+1] - arr[i-1];
            min = Math.min(min, temp);
        }

        return dp[i][j] = min;
    }

    // tabulation - Time: O(n^3) Space: O(n^2)
    public static int minCostTab(int[] arr, int n){
        int c = arr.length;
        int[][] dp = new int[c+2][c+2];

        for(int i = c; i >= 1; i--){
            for(int j = 1; j <= c; j++){
                if(i > j) continue;
                int min = Integer.MAX_VALUE;
                for(int k = i; k <= j; k++){
                    int temp = dp[i][k-1] + dp[k+1][j] + arr[j+1] - arr[i-1];
                    min = Math.min(min, temp);
                }
                dp[i][j] = min;
            }
        }

        return dp[1][c];
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 4, 5, 8};
        int c = arr.length;
        int n = 12;
        int[] arr2 = new int[c+2];
        arr2[0] = 0;
        arr2[c+1] = n;
        for(int i = 1; i <= c; i++){
            arr2[i] = arr[i-1];
        }
        Arrays.sort(arr2);
        System.out.println(minCost(arr2, 1, c));
        System.out.println(minCostMemo(arr2, 1, c, new int[c+2][c+2]));
        System.out.println(minCostTab(arr2, n));
    }

}