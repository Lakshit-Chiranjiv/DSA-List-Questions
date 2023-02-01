package Striver.DP;

public class Q17 {
    // Count number of subsets which sum to target

    // recursive solution - Time: O(2^n) Space: O(n)
    public static int countSubsetSum(int[] arr, int target, int idx) {
        if (target == 0) return 1;
        if (idx == 0){
            if (arr[idx] == target) return 1;
            else return 0;
        }

        int notPick = countSubsetSum(arr, target, idx-1);
        int pick = 0;
        if (target >= arr[idx]) pick = countSubsetSum(arr, target-arr[idx], idx-1);

        return notPick + pick;
    }

    // memoization - Time: O(n*target) Space: O(n*target)
    public static int countSubsetSumMemo(int[] arr, int target, int idx, int[][] dp) {
        if (target == 0) return 1;
        if (idx == 0){
            if (arr[idx] == target) return 1;
            else return 0;
        }

        if (dp[idx][target] != -1) return dp[idx][target];

        int notPick = countSubsetSumMemo(arr, target, idx-1, dp);
        int pick = 0;
        if (target >= arr[idx]) pick = countSubsetSumMemo(arr, target-arr[idx], idx-1, dp);

        return dp[idx][target] = notPick + pick;
    }

    // tabulation - Time: O(n*target) Space: O(n*target)
    public static int countSubsetSumTab(int[] arr, int target) {
        int n = arr.length;
        int[][] dp = new int[n][target+1];

        for (int i = 0; i < n; i++) {
            dp[i][0] = 1;
        }

        if(arr[0] <= target) dp[0][arr[0]] = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= target; j++) {
                int notPick = dp[i-1][j];
                int pick = 0;
                if (j >= arr[i]) pick = dp[i-1][j-arr[i]];

                dp[i][j] = notPick + pick;
            }
        }
        return dp[n-1][target];
    }


    // space optimization - Time: O(n*target) Space: O(target)
    public static int countSubsetSumTabSpaceOpt(int[] arr, int target) {
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
}