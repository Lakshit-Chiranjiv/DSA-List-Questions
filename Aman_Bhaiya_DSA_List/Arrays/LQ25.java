package Aman_Bhaiya_DSA_List.Arrays;

public class LQ25 {

    //Time Complexity: O(logn)
    public int findMin(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = n-1;
        int mid;

        if(n == 1)
            return nums[0];

        if(n == 2)
            return Math.min(nums[0],nums[1]);


        while(left <= right){
            mid = (left+right)/2;
            if(mid != 0 && nums[mid-1] > nums[mid])
                return nums[mid];
            else if(nums[mid] <= nums[right])
                right = mid - 1;
            else if(nums[mid] > nums[right])
                left = mid + 1;
        }
        
        return nums[0];
    }

    //Time Complexity: O(n)
    public int findMin2(int[] nums) {
        for(int i=0;i<nums.length-1;i++){
            if(nums[i]>nums[i+1]){
                return nums[i+1];
            }
        }
        return nums[0];
    }
}
