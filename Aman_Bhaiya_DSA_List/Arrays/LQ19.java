package Aman_Bhaiya_DSA_List.Arrays;

class Solution {
    public int maxProfit(int[] prices) {
        int mp = 0;

        int[] furtherMax = new int[prices.length];
        furtherMax[prices.length-1] = prices[prices.length-1];
        for(int i = prices.length-2;i>=0;i--)
            furtherMax[i] = Math.max(prices[i],furtherMax[i+1]);
            
        for(int i = 0;i<prices.length;i++){
            mp = Math.max(mp,(furtherMax[i]-prices[i]));
        }
        
        return mp;
    }
}