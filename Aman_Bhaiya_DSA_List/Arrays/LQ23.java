public class LQ23 {
    public int[] productExceptSelf(int[] nums) {
        int out[] = new int[nums.length];
        out[0] = nums[0];
        for(int i = 1; i < nums.length; i++){
            out[i] = out[i-1]*nums[i];
        }
        
        int rp = 1;
        for(int i = nums.length - 1; i > 0; i--){
            out[i] = out[i-1] * rp;
            rp *= nums[i];
        }
        out[0] = rp;
        return out;
    }
}
