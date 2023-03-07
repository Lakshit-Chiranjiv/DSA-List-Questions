package Striver.DP;
import java.util.*;

public class Q43 {
    // longest increasing subsequence

    // binary search - Time: O(nlogn), Space: O(n)
    public int lengthOFLISBinSearch(int[] arr, int n){
        ArrayList<Integer> list = new ArrayList<>();
        list.add(arr[0]);
        for(int i = 1; i < n; i++){
            if(arr[i] > list.get(list.size()-1)){
                list.add(arr[i]);
            }else{
                int ind = Collections.binarySearch(list, arr[i]);
                if(ind < 0) ind = -ind-1;
                list.set(ind, arr[i]);
            }
        }
        return list.size();
    }
}
