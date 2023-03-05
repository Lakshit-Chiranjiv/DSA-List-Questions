package Striver.DP;

public class Q41{
    // longest increasing subsequence length

    // recursive solution - Time: O(2^n) Space: O(n)
    public int LIS(int[] arr, int n, int idx, int prev_idx){
        if(idx == n) return 0;

        int lis_len = LIS(arr,n,idx+1,prev_idx)+0;
        if(prev_idx == -1 || arr[idx] > arr[prev_idx]){
            lis_len = Math.max(lis_len, LIS(arr,n,idx+1,idx)+1);
        }

        return lis_len;
    }

    // memoization - Time: O(n^2) Space: O(n^2)
    public int LISMem(int[] arr, int n, int idx, int prev_idx, int[][] dp){
        if(idx == n) return 0;

        if(dp[idx][prev_idx+1] != -1) return dp[idx][prev_idx+1];

        int lis_len = LISMem(arr,n,idx+1,prev_idx,dp)+0;
        if(prev_idx == -1 || arr[idx] > arr[prev_idx]){
            lis_len = Math.max(lis_len, LISMem(arr,n,idx+1,idx,dp)+1);
        }

        return dp[idx][prev_idx+1] = lis_len;
    }

    public static void main(String[] args) {
        int[] arr = {10,9,2,5,3,7,101,18};
        int n = arr.length;

        Q41 obj = new Q41();
        System.out.println(obj.LIS(arr,n,0,-1));
        System.out.println(obj.LISMem(arr,n,0,-1,new int[n][n+1]));
    }
}