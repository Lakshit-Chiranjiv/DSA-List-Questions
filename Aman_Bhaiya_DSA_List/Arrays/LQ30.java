package Aman_Bhaiya_DSA_List.Arrays;

import java.util.PriorityQueue;

public class LQ30 {
    public static int kthSmallest(int[] arr, int l, int r, int k) 
    { 
        //Your code here
        PriorityQueue<Integer> pQueue = new PriorityQueue<Integer>();
        for(int i : arr){
            pQueue.add(i);
        }
        
        for(int i = 0; i < k-1; i++){
            int s = pQueue.poll();
        }
        
        int ans = pQueue.poll();
        return ans;
    }     
}
