package Striver.DP;

import java.util.Arrays;

public class Q47{
    // count number of longest increasing subsequence
    public int LISCount(int[] arr, int n){
        int[] dp = new int[n];
        int[] cnt = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(cnt, 1);
        int max = 1;
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if(arr[i] > arr[j] && dp[i] < dp[j]+1){
                    dp[i] = dp[j]+1;
                    cnt[i] = cnt[j];
                }
                else if(arr[i] > arr[j] && dp[i] == dp[j]+1){
                    cnt[i] += cnt[j];
                }    
                
            }
            max = Math.max(max, dp[i]);
        }
        int ans = 0;
        for(int i = 0; i < n; i++){
            if(dp[i] == max) ans += cnt[i];
        }
        return ans;
    }
}