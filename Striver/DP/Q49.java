package Striver.DP;

public class Q49{
    // matrix chain multiplication

    // tabulation solution - Time: O(n^3), Space: O(n^2)

    public static int matrixChainMultiplication(int[] arr){
        int n = arr.length;
        int[][] dp = new int[n][n];

        for(int i=1; i<n; i++)
            dp[i][i] = 0;

        for(int i = n-1; i>=1; i--){
            for(int j = i+1; j<n; j++){
                dp[i][j] = Integer.MAX_VALUE;
                for(int k = i; k<j; k++){
                    int temp = dp[i][k] + dp[k+1][j] + arr[i]*arr[k+1]*arr[j+1];
                    dp[i][j] = Math.min(dp[i][j], temp);
                }
            }
        }
        return dp[1][n-1];
    }

    public static void main(String[] args) {
        int[] arr = {40, 20, 30, 10, 30};
        System.out.println(matrixChainMultiplication(arr));
    }
}