package Aman_Bhaiya_DSA_List.Arrays;

public class LQ17 {
    public int rotatedSearch(int[] nums, int target) {
        int bi = -1;
        for(int i=0;i<nums.length-1;i++){
            if(nums[i]>nums[i+1]){
                bi = i;
                break;
            }
        }
        
        int s=0,e=bi;
        int m;
        while(s<=e){
            m = (s+e)/2;
            if(nums[m] == target){
                return m;
            }
            else if(nums[m] < target){
                s = m+1;
            }
            else{
                e = m-1;
            }
        }
        s=bi+1;
        e=nums.length-1;
        while(s<=e){
            m = (s+e)/2;
            if(nums[m] == target){
                return m;
            }
            else if(nums[m] < target){
                s = m+1;
            }
            else{
                e = m-1;
            }
        }
        
        return -1;
    }
}
