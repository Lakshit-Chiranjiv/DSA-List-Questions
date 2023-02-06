package Striver.DP;

public class Q21{
    // target sum by assigning + or - to each element of array
    // count number of ways to assign + or - to each element of array such that sum of array is equal to target

    // this problem can be broken down into partition array into two subsets such that difference of sum of both subsets is equal to a specific difference
    // + elements can be considered as one subset and - elements can be considered as another subset
    // now we have to find number of ways to partition array into two subsets such that difference of sum of both subsets is equal to target

    //will work for all arr[i] > 0

    // recursive solution - Time: O(2^n) Space: O(n)
    public static int CountWaysToSumTarget(int[] arr, int idx, int target) {
        if (target == 0) return 1;
        if (idx == 0){
            if (arr[idx] == target) return 1;
            else return 0;
        }

        int notPick = CountWaysToSumTarget(arr, target, idx-1);
        int pick = 0;
        if (target >= arr[idx]) pick = CountWaysToSumTarget(arr, target-arr[idx], idx-1);

        return notPick + pick;
    }

    public static int countPartition(int[] arr, int n, int diff){
        int sum = 0;
        for(int i=0; i<n; i++)
            sum += arr[i];
        int s2 = (sum - diff)/2;
        return CountWaysToSumTarget(arr, n, s2);
    }

    // memoization - Time: O(n*target) Space: O(n*target)
    public static int CountWaysToSumTargetMemo(int[] arr, int target, int idx, int[][] dp) {
        if (target == 0) return 1;
        if (idx == 0){
            if (arr[idx] == target) return 1;
            else return 0;
        }

        if (dp[idx][target] != -1) return dp[idx][target];

        int notPick = CountWaysToSumTargetMemo(arr, target, idx-1, dp);
        int pick = 0;
        if (target >= arr[idx]) pick = CountWaysToSumTargetMemo(arr, target-arr[idx], idx-1, dp);

        return dp[idx][target] = notPick + pick;
    }

    public static int countPartitionMemo(int[] arr, int n, int diff, int[][] dp){
        int sum = 0;
        for(int i=0; i<n; i++)
            sum += arr[i];
        int s2 = (sum - diff)/2;
        return CountWaysToSumTargetMemo(arr, n, s2, dp);
    }

    // tabulation - Time: O(n*target) Space: O(n*target)
    public static int CountWaysToSumTargetTab(int[] arr, int target) {
        int n = arr.length;
        int[][] dp = new int[n][target+1];

        dp[0][0] = 1;
        if(arr[0] <= target) dp[0][arr[0]] = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= target; j++) {
                int pick = 0;
                if (j >= arr[i]) pick = dp[i-1][j-arr[i]];

                dp[i][j] = dp[i-1][j] + pick;
            }
        }
        return dp[n-1][target];
    }

    public static int countPartitionTab(int[] arr, int n, int diff){
        int sum = 0;
        for(int i=0; i<n; i++)
            sum += arr[i];
        int s2 = (sum - diff)/2;
        return CountWaysToSumTargetTab(arr, s2);
    }

    // space optimization - Time: O(n*target) Space: O(target)
    public static int CountWaysToSumTargetTabSpaceOpt(int[] arr, int target) {
        int n = arr.length;
        int[] dp = new int[target+1];
        int[] curr = new int[target+1];
        dp[0] = 1;
        curr[0] = 1;
        if(arr[0] <= target) dp[arr[0]] = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= target; j++) {
                int notPick = dp[j];
                int pick = 0;
                if (j >= arr[i]) pick = dp[j-arr[i]];

                curr[j] = notPick + pick;
            }
            dp = curr;
        }
        return dp[target];
    }

    public static int countPartitionTabSpaceOpt(int[] arr, int n, int diff){
        int sum = 0;
        for(int i=0; i<n; i++)
            sum += arr[i];
        int s2 = (sum - diff)/2;
        return CountWaysToSumTargetTabSpaceOpt(arr, s2);
    }

    public static void main(String[] args) {
        int[] arr = {1, 1, 2, 3};
        int n = arr.length;
        int diff = 1;
        System.out.println(countPartition(arr, n, diff));
        System.out.println(countPartitionMemo(arr, n, diff, new int[n][diff+1]));
        System.out.println(countPartitionTab(arr, n, diff));
        System.out.println(countPartitionTabSpaceOpt(arr, n, diff));
    }
}