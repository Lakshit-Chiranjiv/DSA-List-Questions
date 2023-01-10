package Aman_Bhaiya_DSA_List.Arrays;

import java.util.HashMap;

public class LQ35 {
    // longest subarray length with sum divisible by k

    public static void main(String[] args) {
        int[] arr = { 2, 7, 6, 1, 4, 5 };
        int k = 3;
        int n = arr.length;
        System.out.println(longestSubarray(arr, n, k));
    }

    public static int longestSubarray(int[] arr, int n, int k) {
        int[] mod = new int[k];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
            mod[((sum % k) + k) % k]++;
        }
        int ans = 0;
        for (int i = 0; i < k; i++) {
            if (i == 0 || mod[i] > 1) {
                ans = Math.max(ans, mod[i]);
            }
        }
        return ans;
    }

    public static int longestSubarray2(int[] arr,int n, int k){
        int mxlen = 0;
        for(int i=0;i<n;i++){
            int sum = 0;
            for(int j=i;j<n;j++){
                sum += arr[j];
                if(sum%k==0){
                    mxlen = Math.max(mxlen, j-i+1);
                }
            }
        }

        return mxlen;
    }

    public static int longestSubarray3(int[] arr, int n, int k){
        HashMap<Integer, Integer> map = new HashMap<>();
        int sum = 0;
        int mxlen = 0;
        int mod_arr[] = new int[n];
        for(int i=0;i<n;i++){
            sum += arr[i];
            mod_arr[i] = ((sum%k)+k)%k;

            if(mod_arr[i]==0){
                mxlen = i+1;
            }
            else if(map.containsKey(mod_arr[i])){
                mxlen = Math.max(mxlen, i-map.get(mod_arr[i]));
            }
            else{
                map.put(mod_arr[i], i);
            }

        }
        return mxlen;
    }

    public static int longestSubarray4(int[] arr, int n, int k){
        HashMap<Integer, Integer> map = new HashMap<>();
        int sum = 0;
        int mxlen = 0;
        for(int i = 0; i < n; i++){
            sum += arr[i];
            int mod = ((sum%k)+k)%k;
            if(mod==0){
                mxlen = i+1;
            }
            else if(map.containsKey(mod)){
                mxlen = Math.max(mxlen, i-map.get(mod));
            }
            else{
                map.put(mod, i);
            }
        }

        return mxlen;

    }


}
