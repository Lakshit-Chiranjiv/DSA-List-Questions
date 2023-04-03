package Striver.DP;

public class Q54{
    // Partition Array for Maximum Sum

    // Recursive solution - Time: O(2^n) Space: O(n)
    public int maxSum(int i, int[] arr, int k){
        if(i >= arr.length) return 0;

        int max = Integer.MIN_VALUE;
        int len = 0;
        int maxVal = Integer.MIN_VALUE;

        for(int j = i; j < Math.min(i + k, arr.length); j++){
            len++;
            maxVal = Math.max(maxVal, arr[j]);
            max = Math.max(max, maxVal * len + maxSum(j + 1, arr, k));
        }

        return max;
    }

    // Memoization - Time: O(n*k) Space: O(n)
    public int maxSumMemo(int i, int[] arr, int k, int[] dp){
        if(i >= arr.length) return 0;

        if(dp[i] != -1) return dp[i];

        int max = Integer.MIN_VALUE;
        int len = 0;
        int maxVal = Integer.MIN_VALUE;

        for(int j = i; j < Math.min(i + k, arr.length); j++){
            len++;
            maxVal = Math.max(maxVal, arr[j]);
            max = Math.max(max, maxVal * len + maxSumMemo(j + 1, arr, k, dp));
        }

        return dp[i] = max;
    }

    // Tabulation - Time: O(n*k) Space: O(n)
    public int maxSumTab(int[] arr, int k){
        int n = arr.length;
        int[] dp = new int[n + 1];

        for(int i = n - 1; i >= 0; i--){
            int max = Integer.MIN_VALUE;
            int len = 0;
            int maxVal = Integer.MIN_VALUE;

            for(int j = i; j < Math.min(i + k, n); j++){
                len++;
                maxVal = Math.max(maxVal, arr[j]);
                max = Math.max(max, maxVal * len + dp[j + 1]);
            }

            dp[i] = max;
        }

        return dp[0];
    }
    
    public static void main(String[] args) {
        Q54 obj = new Q54();
        int[] arr = {1, 15, 7, 9, 2, 5, 10};
        int k = 3;
        System.out.println(obj.maxSum(0, arr, k));
        int[] dp = new int[arr.length];
        for(int i = 0; i < dp.length; i++) dp[i] = -1;
        System.out.println(obj.maxSumMemo(0, arr, k, dp));
        System.out.println(obj.maxSumTab(arr, k));
    }
}