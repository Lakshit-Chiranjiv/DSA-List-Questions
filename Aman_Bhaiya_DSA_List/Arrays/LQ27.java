package Aman_Bhaiya_DSA_List.Arrays;

import java.util.*;

public class LQ27 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        int n = nums.length;

        for(int i = 0; i < n-2; i++){
            if(i == 0 || (i > 0 && nums[i]!=nums[i-1])){
                int l = i+1;
                int r = n-1;
                int sum = 0 - nums[i];
                while(l < r){
                    if(nums[l] + nums[r] == sum){
                        ArrayList<Integer> arr = new ArrayList<>(
                            Arrays.asList(nums[i],nums[l],nums[r])
                        );
                        ans.add(arr);

                        while(l < r && nums[l] == nums[l+1]) l++;
                        while(l < r && nums[r] == nums[r-1]) r--;

                        l++;
                        r--;
                    }
                    else if(nums[l]+nums[r] < sum) l++;
                    else r--;
                }
            }
        }

        return ans;
    }
}
