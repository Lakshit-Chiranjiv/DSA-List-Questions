package Striver.DP;

import java.util.Arrays;

public class Q42{
    // longest increasing subsequence

    // tabulation - Time: O(n^2), Space: O(n)
    public int lengthOfLISTab(int[] arr, int n){
        int[][] dp = new int[n+1][n+1];
        for(int ind = n-1; ind >= 0; ind--){
            for(int prev_ind = ind-1; prev_ind >= -1; prev_ind--){
                int length = 0 + dp[ind+1][prev_ind+1];
                if(prev_ind == -1 || arr[ind] > arr[prev_ind]){
                    length = Math.max(length, 1 + dp[ind+1][ind+1]);
                }
                dp[ind][prev_ind+1] = length;
            }
        }
        return dp[0][0];
    }

    // space optimization - Time: O(n^2), Space: O(n)
    public int lengthOfLISSpOpt(int[] arr, int n){
        int[] next = new int[n+1];
        int[] curr = new int[n+1];
        for(int ind = n-1; ind >= 0; ind--){
            for(int prev_ind = ind-1; prev_ind >= -1; prev_ind--){
                int length = 0 + next[prev_ind+1];
                if(prev_ind == -1 || arr[ind] > arr[prev_ind]){
                    length = Math.max(length, 1 + next[ind+1]);
                }
                curr[prev_ind+1] = length;
            }
        }
        return next[0];
    }

    // optimized solution - Time: O(n^2), Space: O(n)
    public int lengthOfLISOptimized(int[] arr, int n){
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        int max = 1;
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if(arr[i] > arr[j]){
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
            max = Math.max(max, dp[i]);
        }
        return max;
    }

    // optimized solution and printing the LIS - Time: O(n^2), Space: O(n)
    public int lengthOfLISOptimizedPrint(int[] arr, int n){
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        int hash[] = new int[n];
        for(int i = 0; i < n; i++) hash[i] = i;
        int max = 1;
        int last_idx = 0;
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if(arr[i] > arr[j] && dp[i] < dp[j]+1){
                    dp[i] = dp[j]+1;
                    hash[i] = j;
                }

            }
            if(max < dp[i]){
                max = dp[i];
                last_idx = i;
            }
        }

        int[] lis = new int[max];
        int idx = max-1;
        while(last_idx != hash[last_idx]){
            lis[idx--] = arr[last_idx];
            last_idx = hash[last_idx];
        }
        lis[idx] = arr[last_idx];
        System.out.println(Arrays.toString(lis));
        return max;
    }

    public static void main(String[] args) {
        int[] arr = {10,9,2,5,3,7,101,18};
        int n = arr.length;

        Q42 obj = new Q42();
        System.out.println(obj.lengthOfLISTab(arr,n));
        System.out.println(obj.lengthOfLISSpOpt(arr,n));
        System.out.println(obj.lengthOfLISOptimized(arr,n));
        System.out.println(obj.lengthOfLISOptimizedPrint(arr,n));
    }
}