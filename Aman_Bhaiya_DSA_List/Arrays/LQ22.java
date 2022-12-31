import java.util.ArrayList;

public class LQ22 {
    public int trap(int[] height) {
        int n = height.length;
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> right = new ArrayList<>();
        int mn, lmx = height[0], rmx = height[n-1], total = 0;
        
        left.add(lmx);
        for(int i=1; i < n; i++){
            lmx = Math.max(lmx,height[i]);
            left.add(lmx);
        }

        right.add(rmx);
        for(int i = (n-2); i>=0; i--){
            rmx = Math.max(rmx,height[i]);
            right.add(rmx);
        }

        for(int i = 0; i < n; i++){
            mn = Math.min(left.get(i),right.get(n-i-1));
            total = total + (mn - height[i]);
        }

        return total;
    }
}