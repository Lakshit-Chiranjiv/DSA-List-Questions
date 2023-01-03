package Aman_Bhaiya_DSA_List.Arrays;

public class LQ28{
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length -1;
        int mxw = (r-l) * Math.min(height[l],height[r]);
        while(l < r){
            mxw = Math.max(mxw,((r-l) * Math.min(height[l],height[r])));
            if(height[l]<= height[r])
                l++;
            else
                r--;
        }
        
        return mxw;
    }
}