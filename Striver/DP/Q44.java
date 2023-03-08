package Striver.DP;

import java.util.Arrays;
public class Q44{
    // longest divisible subset

    // optimized solution with printing the LDS - Time: O(n^2), Space: O(n)
    public int lengthOfLDSOptimizedPrint(int[] arr, int n){
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        Arrays.sort(arr);
        int hash[] = new int[n];
        for(int i = 0; i < n; i++) hash[i] = i;
        int max = 1;
        int last_idx = 0;
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if(arr[i] % arr[j] == 0 && dp[i] < dp[j]+1){
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
        Q44 q = new Q44();
        int[] arr = {1, 2, 3, 4, 9, 8, 7, 6};
        int n = arr.length;
        System.out.println(q.lengthOfLDSOptimizedPrint(arr, n));
    }
}