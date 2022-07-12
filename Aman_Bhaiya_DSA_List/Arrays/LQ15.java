package Aman_Bhaiya_DSA_List.Arrays;

import java.util.*;

public class LQ15 {
    //method 1
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(map.getOrDefault(nums[i],0) > 0)
                return true;
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        }
        
        return false;
    }

    //method 2
    public boolean containsDuplicate2(int[] nums) {
        Set<Integer> set=new HashSet<>();
        for(int elements: nums){
            if(set.contains(elements))
                return true;
            else
                set.add(elements);
        }
        return false;
    }
}