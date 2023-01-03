package Striver.Recursion;

import java.util.*;

public class q15 {
    // print all combination sum of array elements which sum to target where each element can be used only once in a combination and answer set should not contain duplicate combinations

    public static void main(String[] args) {
        int[] arr = { 10, 1, 2, 7, 6, 1, 5 };
        int target = 8;
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(arr);
        combinationSum2(arr, target, 0, ans, new ArrayList<>());

        for (List<Integer> list : ans) {
            System.out.println(list);
        }
    }

    private static void combinationSum2(int[] arr, int target, int idx, List<List<Integer>> ans, List<Integer> ds) {
        if (target == 0) {
            ans.add(new ArrayList<>(ds));
            return;
        }

        for (int i = idx; i < arr.length; i++) {
            if (i > idx && arr[i] == arr[i - 1]) {
                continue;
            }
            if (arr[i] <= target) {
                ds.add(arr[i]);
                combinationSum2(arr, target - arr[i], i + 1, ans, ds);
                ds.remove(ds.size() - 1);
            }
        }
    }

    


}
