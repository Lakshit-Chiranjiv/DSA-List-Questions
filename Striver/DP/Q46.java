package Striver.DP;

import java.util.Arrays;

public class Q46 {
    // longest bitonic subsequence

    public int longestBitonicSubsquence(int[] arr, int n){
        int[] dp1 = new int[n];
        Arrays.fill(dp1, 1);
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if(arr[i] > arr[j]){
                    dp1[i] = Math.max(dp1[i], dp1[j]+1);
                }
            }
        }

        int[] dp2 = new int[n];
        Arrays.fill(dp2, 1);
        for(int i = n-2; i >= 0; i--){
            for(int j = n-1; j > i; j--){
                if(arr[i] > arr[j]){
                    dp2[i] = Math.max(dp2[i], dp2[j]+1);
                }
            }
        }

        int max = 1;
        for(int i = 0; i < n; i++){
            max = Math.max(max, dp1[i] + dp2[i] - 1);
        }
        return max;
    }
}
