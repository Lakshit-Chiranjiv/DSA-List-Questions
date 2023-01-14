package Striver.DP;

public class Q6 {
     // Maximum Sum of Non-Adjacent Elements in a cyclic manner | House Robber 2 problem 

    // recursive solution - Time: O(2^n) Space: O(n)
    public static int maxSum(int[] arr, int n){
        if(n == 0)
            return arr[n];
        if(n < 0)
            return 0;
        int pick = maxSum(arr, n-2) + arr[n];
        int notPick = maxSum(arr, n-1);

        return Math.max(pick, notPick);
    }

    // memoization - Time: O(n) Space: O(n)
    public static int maxSumMemo(int[] arr, int n, int[] dp){
        if(n == 0)
            return dp[n] = arr[n];
        if(n < 0)
            return 0;
        if(dp[n] != -1)
            return dp[n];
        int pick = maxSumMemo(arr, n-2, dp) + arr[n];
        int notPick = maxSumMemo(arr, n-1, dp);

        return dp[n] = Math.max(pick, notPick);
    }

    // tabulation - Time: O(n) Space: O(n)
    public static int maxSumTab(int[] arr, int n){
        int[] dp = new int[n+1];
        dp[0] = arr[0];
        for(int i = 1;i<=n;i++){
            int pick = 0;
            if(i-2 >= 0)
                pick = dp[i-2] + arr[i];
            int notPick = dp[i-1];
            dp[i] = Math.max(pick, notPick);
        }
        return dp[n];
    }

    // space optimization - Time: O(n) Space: O(1)
    public static int maxSumTabOpt(int[] arr, int n){
        int a = arr[0];
        int b = 0;
        for(int i = 1;i<=n;i++){
            int pick = arr[i];
            if(i > 1)
                pick += a;
            int notPick = b;
            int c = Math.max(pick, notPick);
            a = b;
            b = c;
        }
        return b;
    }

    public static int maxSumCyclic(int[] arr, int n){
        if (n == 1) 
            return arr[0];
        int[] arr1 = new int[n-1];
        int[] arr2 = new int[n-1];
        for(int i = 0;i<n-1;i++){
            if(i != n-1)
                arr2[i] = arr[i];

            if(i != 0)
                arr1[i] = arr[i+1];
        }
        int sum1 = maxSumTab(arr1, n-2);
        int sum2 = maxSumTab(arr2, n-2);
        return Math.max(sum1, sum2);
    }

    public static void main(String[] args) {
        int[] arr = {5, 5, 10, 100, 10, 5};
        int n = arr.length-1;
        System.out.println(maxSum(arr, n));
        int[] dp = new int[n+1];
        for(int i = 0;i<=n;i++)
            dp[i] = -1;
        System.out.println(maxSumMemo(arr, n, dp));
        System.out.println(maxSumTab(arr, n));
        System.out.println(maxSumTabOpt(arr, n));
    }
}
