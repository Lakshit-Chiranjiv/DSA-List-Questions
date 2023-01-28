package Striver.DP;

public class Q14 {
    // subset sum equal to target
    
    // recursive solution - Time: O(2^n) Space: O(n)
    public boolean subsetSum(int[] arr, int target, int n) {
        if(target == 0) return true;
        if(n == 0) return arr[0] == target;
        boolean notPick = subsetSum(arr, target, n-1);
        boolean pick = false;
        if(target >= arr[n]) pick = subsetSum(arr, target-arr[n], n-1);
        return notPick || pick;
    }

    // memoization - Time: O(n*target) Space: O(n*target)
    public boolean subsetSumMemo(int[] arr, int target, int n, Boolean[][] dp) {
        if(target == 0) return true;
        if(n == 0) return arr[0] == target;
        if(dp[n][target] != null) return dp[n][target];
        boolean notPick = subsetSumMemo(arr, target, n-1, dp);
        boolean pick = false;
        if(target >= arr[n]) pick = subsetSumMemo(arr, target-arr[n], n-1, dp);
        return dp[n][target] = notPick || pick;
    }

    // tabulation - Time: O(n*target) Space: O(n*target)
    public boolean subsetSumTab(int[] arr, int target, int n) {
        boolean[][] dp = new boolean[n+1][target+1];
        for(int i=0; i<=n; i++) dp[i][0] = true;
        dp[0][arr[0]] = true;
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=target; j++) {
                boolean notPick = dp[i-1][j];
                boolean pick = false;
                if(j >= arr[i-1]) pick = dp[i-1][j-arr[i-1]];
                dp[i][j] = notPick || pick;
            }
        }
        return dp[n][target];
    }

    // space optimization - Time: O(n*target) Space: O(target)
    public boolean subsetSumTabOpt(int[] arr, int target, int n) {
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

    public static void main(String[] args) {
        Q14 q = new Q14();
        int[] arr = {1, 5, 11, 5};
        int target = 11;
        int n = arr.length;
        System.out.println(q.subsetSum(arr, target, n-1));
        Boolean[][] dp = new Boolean[n+1][target+1];
        System.out.println(q.subsetSumMemo(arr, target, n, dp));
        System.out.println(q.subsetSumTab(arr, target, n));
        System.out.println(q.subsetSumTabOpt(arr, target, n));
    }
}
