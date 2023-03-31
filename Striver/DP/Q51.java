package Striver.DP;

public class Q51{
    // burst balloons

    // recursive solution - Time: O(3^n) Space: O(n)
    public int maxCoins(int i, int j, int[] nums) {
        if(i > j) return 0;
        int max = Integer.MIN_VALUE;

        for(int ind = i; ind <= j; ind++){
            int cost = nums[i-1] * nums[ind] * nums[j+1] + maxCoins(i, ind-1, nums) + maxCoins(ind+1, j, nums);
            max = Math.max(max, cost);
        }

        return max;
    }

    // memoization - Time: O(n^3) Space: O(n^2)
    public int maxCoinsMemo(int i, int j, int[] nums, int[][] dp) {
        if(i > j) return 0;
        if(dp[i][j] != 0) return dp[i][j];
        int max = Integer.MIN_VALUE;

        for(int ind = i; ind <= j; ind++){
            int cost = nums[i-1] * nums[ind] * nums[j+1] + maxCoinsMemo(i, ind-1, nums, dp) + maxCoinsMemo(ind+1, j, nums, dp);
            max = Math.max(max, cost);
        }

        return dp[i][j] = max;
    }

    // tabulation - Time: O(n^3) Space: O(n^2)
    public int maxCoinsTab(int[] nums){
        int n = nums.length;
        int[][] dp = new int[n+2][n+2];

        int[] arr = new int[n+2];
        arr[0] = arr[n+1] = 1;
        for(int i = 1; i <= n; i++) arr[i] = nums[i-1];

        for(int i = n; i >= 1; i--){
            for(int j = i; j <= n; j++){

                if(i > j) continue;

                for(int k = i; k <= j; k++){
                    int cost = arr[i-1] * arr[k] * arr[j+1] + dp[i][k-1] + dp[k+1][j];
                    dp[i][j] = Math.max(dp[i][j], cost);
                }
            }
        }

        return dp[1][n];
    }

    public static void main(String[] args) {
        int[] nums = {3,1,5,8};
        Q51 q = new Q51();
        int[] newNums = new int[nums.length+2];
        newNums[0] = newNums[nums.length+1] = 1;
        for(int i = 1; i <= nums.length; i++) newNums[i] = nums[i-1];
        System.out.println(q.maxCoins(1, nums.length, newNums));
        System.out.println(q.maxCoinsMemo(1, nums.length, newNums, new int[nums.length+2][nums.length+2]));
        System.out.println(q.maxCoinsTab(nums));
    }
}