package Striver.Recursion;

import java.util.ArrayList;
import java.util.List;

public class q17 {
    // return all possible subsets of an array with no duplicates

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 };
        List<List<Integer>> ans = new ArrayList<>();
        allSubsets(arr, 0, new ArrayList<>(), ans);
    }

    public static void allSubsets(int[] arr, int idx, List<Integer> subset, List<List<Integer>> ans) {
        ans.add(new ArrayList<>(subset));

        for (int i = idx; i < arr.length; i++) {

            if(i > idx && arr[i] == arr[i-1]) continue;

            subset.add(arr[i]);
            allSubsets(arr, i + 1, subset, ans);
            subset.remove(subset.size() - 1);
        }
    }
}
