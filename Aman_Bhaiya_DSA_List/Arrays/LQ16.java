package Aman_Bhaiya_DSA_List.Arrays;

import java.util.Arrays;

public class LQ16 {
    public int findMinDiff(int arr[], int n, int m) {    
        if(m==0 || n==0)
            return 0;

        if (n < m)
            return -1;

        int minDiff = Integer.MAX_VALUE;

        Arrays.sort(arr);
        int left = 0;
        int right = m-1;
        for(int i = 0; i < n-m+1; i++){
            int diff = arr[right] - arr[left];
            if(diff < minDiff){
                minDiff = diff;
            }
            left++;
            right++;
        }
        
        return minDiff;
    }
}