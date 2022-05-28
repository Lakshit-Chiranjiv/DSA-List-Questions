// 268. Missing Number
public class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int s = (n*(n+1))/2;
        int sm  = 0;
        for(int x:nums){
            sm += x;
        }
        
        return s-sm;
    }
}