package Aman_Bhaiya_DSA_List.Arrays;

public class LQ14 {
    public int maxSubArray(int[] nums) {    
        int mx = nums[0];
        int currMax = nums[0];
        for(int i = 1; i < nums.length; i++){
            currMax = Math.max(currMax+nums[i],nums[i]);
            mx = Math.max(mx,currMax);
        }
        
        return mx;
    }
}
