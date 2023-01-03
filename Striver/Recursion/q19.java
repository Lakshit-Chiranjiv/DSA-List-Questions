package Striver.Recursion;

import java.util.ArrayList;
import java.util.List;

public class q19 {
    // return all permutations of a string/array - recursion swapping approach

    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5};
        List<List<Integer>> ans = new ArrayList<>();
        permute(arr, 0, ans);
        System.out.println(ans);
    }

    public static void permute(int arr[], int idx, List<List<Integer>> ans) {
        if (idx == arr.length) {
            List<Integer> temp = new ArrayList<>();
            for (int i : arr) {
                temp.add(i);
            }
            ans.add(temp);
            return;
        }
        for (int i = idx; i < arr.length; i++) {
            swap(arr, idx, i);
            permute(arr, idx + 1, ans);
            swap(arr, idx, i);
        }
    }

    public static void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
