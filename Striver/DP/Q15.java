package Striver.DP;

public class Q15{
    // Partition equal subset sum

    // recursive solution - Time: O(2^n) Space: O(n)
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for(int i: nums) sum += i;
        if(sum%2 != 0) return false;
        return subsetSum(nums, sum/2, 0);
    }

    public boolean subsetSum(int[] arr, int target, int n){
        if(target == 0) return true;
        if(n == 0) return arr[0] == target;
        boolean notPick = subsetSum(arr, target, n-1);
        boolean pick = false;
        if(target >= arr[n]) pick = subsetSum(arr, target-arr[n], n-1);
        return notPick || pick;
    }

    // memoization - Time: O(n*target) Space: O(n*target)
    public boolean canPartitionMemo(int[] nums) {
        int sum = 0;
        for(int i: nums) sum += i;
        if(sum%2 != 0) return false;
        Boolean[][] dp = new Boolean[nums.length][sum/2+1];
        return subsetSumMemo(nums, sum/2, nums.length-1, dp);
    }

    public boolean subsetSumMemo(int[] arr, int target, int n, Boolean[][] dp){
        if(target == 0) return true;
        if(n == 0) return arr[0] == target;
        if(dp[n][target] != null) return dp[n][target];
        boolean notPick = subsetSumMemo(arr, target, n-1, dp);
        boolean pick = false;
        if(target >= arr[n]) pick = subsetSumMemo(arr, target-arr[n], n-1, dp);
        return dp[n][target] = notPick || pick;
    }

    // tabulation - Time: O(n*target) Space: O(n*target)
    public boolean canPartitionTab(int[] nums) {
        int sum = 0;
        for(int i: nums) sum += i;
        if(sum%2 != 0) return false;
        boolean[][] dp = new boolean[nums.length+1][sum/2+1];
        for(int i=0; i<=nums.length; i++) dp[i][0] = true;
        dp[0][nums[0]] = true;
        for(int i=1; i<=nums.length; i++) {
            for(int j=1; j<=sum/2; j++) {
                boolean notPick = dp[i-1][j];
                boolean pick = false;
                if(j >= nums[i-1]) pick = dp[i-1][j-nums[i-1]];
                dp[i][j] = notPick || pick;
            }
        }
        return dp[nums.length][sum/2];
    }

    // space optimization - Time: O(n*target) Space: O(target)
    public boolean canPartitionSpaceOpt(int[] arr) {
        int sum = 0;
        for(int i: arr) sum += i;
        if(sum%2 != 0) return false;
        int target = sum/2;
        int n = arr.length;
        boolean[] dp = new boolean[target+1];
        boolean[] curr = new boolean[target+1];
        dp[0] = true;
        curr[0] = true;
        dp[arr[0]] = true;
        for(int i=1; i<=n; i++) {
            for(int j=1; j <= target; j++) {
                boolean notPick = dp[j];
                boolean pick = false;
                if(j >= arr[i-1]) pick = dp[j-arr[i-1]];
                curr[j] = notPick || pick;
            }
            dp = curr;
        }
        return dp[target];
    }
}