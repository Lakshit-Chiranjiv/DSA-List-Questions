package Striver.DP;

public class Q16 {
    // Partition a set into two subsets such that the difference of subset sums is minimum

    // recursive solution - Time: O(2^n) Space: O(n)
    public int minDiff(int[] nums) {
        int sum = 0;
        for(int i: nums) sum += i;
        return findMinDiff(nums, sum, nums.length-1);
    }

    public int findMinDiff(int[] arr, int target, int n){
        if(n == 0) return Math.abs(target-2*arr[0]);
        int notPick = findMinDiff(arr, target, n-1);
        int pick = findMinDiff(arr, target-2*arr[n], n-1);
        return Math.min(notPick, pick);
    }

    // memoization - Time: O(n*target) Space: O(n*target)
    public int minDiffMemo(int[] nums) {
        int sum = 0;
        for(int i: nums) sum += i;
        Integer[][] dp = new Integer[nums.length][sum+1];
        return findMinDiffMemo(nums, sum, nums.length-1, dp);
    }

    public int findMinDiffMemo(int[] arr, int target, int n, Integer[][] dp){
        if(n == 0) return Math.abs(target-2*arr[0]);
        if(dp[n][target] != null) return dp[n][target];
        int notPick = findMinDiffMemo(arr, target, n-1, dp);
        int pick = findMinDiffMemo(arr, target-2*arr[n], n-1, dp);
        return dp[n][target] = Math.min(notPick, pick);
    }

    // tabulation - Time: O(n*target) Space: O(n*target)
    public int minDiffTab(int[] nums) {
        int sum = 0;
        for(int i: nums) sum += i;
        int[][] dp = new int[nums.length+1][sum+1];
        for(int i=0; i<=nums.length; i++) dp[i][0] = 0;
        for(int i=1; i<=nums.length; i++) {
            for(int j=1; j<=sum; j++) {
                int notPick = dp[i-1][j];
                int pick = Integer.MAX_VALUE;
                if(j >= 2*nums[i-1]) pick = dp[i-1][j-2*nums[i-1]];
                dp[i][j] = Math.min(notPick, pick);
            }
        }
        return dp[nums.length][sum];
    }

    // space optimization - Time: O(n*target) Space: O(target)
    public int minDiffTabOpt(int[] nums) {
        int sum = 0;
        for(int i: nums) sum += i;
        int[] dp = new int[sum+1];
        for(int i=1; i<=nums.length; i++) {
            for(int j=sum; j>=0; j--) {
                int notPick = dp[j];
                int pick = Integer.MAX_VALUE;
                if(j >= 2*nums[i-1]) pick = dp[j-2*nums[i-1]];
                dp[j] = Math.min(notPick, pick);
            }
        }
        return dp[sum];
    }
}
