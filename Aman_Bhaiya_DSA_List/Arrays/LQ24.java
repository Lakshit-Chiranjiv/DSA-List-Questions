public class LQ24 {
    public int maxProduct(int[] nums) {
        int mx = nums[0];
        int mn = nums[0];
        int ans = nums[0];

        for(int i = 1; i < nums.length; i++){
            if(nums[i] < 0){
                int temp = mx;
                mx = mn;
                mn = temp;
            }

            mx = Math.max(nums[i],mx*nums[i]);
            mn = Math.min(nums[i],mn*nums[i]);
            ans = Math.max(ans,mx);
        }
        return ans;
    }
}
