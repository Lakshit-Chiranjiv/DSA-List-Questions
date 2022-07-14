package Aman_Bhaiya_DSA_List.Arrays;

import java.util.Arrays;

public class LQ18 {
    public void nextPermutation(int[] nums) {
        int l = nums.length;
        
        int lt = l-2;
        
        while(lt>=0 && nums[lt]>=nums[lt+1]){
            lt--;
        }
        
        if(lt == -1){
            Arrays.sort(nums);
            return;
        }
        
        for(int i = l-1;i>=0;i--){
            if(nums[i] > nums[lt]){
                int p = nums[i];
                nums[i] = nums[lt];
                nums[lt] = p;
                break;
            }
        }
        
        int x = lt+1;
        int y = l-1;
        
        while(x<=y){
            int p = nums[x];
            nums[x] = nums[y];
            nums[y] = p;
            x++;
            y--;
        }
        
    }
}
