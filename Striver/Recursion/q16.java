package Striver.Recursion;

import java.util.Arrays;

public class q16 {
    // print the sum of all the subsets of an array in ascending order

    public static void main(String[] args) {
        int[] arr = { 5, 3, 2 };
        int[] ans = new int[1 << arr.length];
        int idx = 0;
        subsetSum(arr, 0, 0, ans, idx);
        Arrays.sort(ans);
        for (int i : ans) {
            System.out.print(i + " ");
        }
    }

    private static void subsetSum(int[] arr, int idx, int sum, int[] ans, int ansIdx) {
        if (idx == arr.length) {
            ans[ansIdx] = sum;
            return;
        }

        //pick
        subsetSum(arr, idx + 1, sum + arr[idx], ans, ansIdx + 1);
        
        //not pick
        subsetSum(arr, idx + 1, sum, ans, ansIdx);
    }
}
