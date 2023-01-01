package Striver.Recursion;

public class q14 {
    // print all combination sum of array elements which sum to target where each element can be used any number of times
    
    public static void printSubsequence(int[] arr, int k, int i, String ans) {
        if (i == arr.length) {
            if (k == 0) {
                System.out.println(ans);
            }
            return;
        }
        if (k - arr[i] >= 0) {
            printSubsequence(arr, k - arr[i], i, ans + arr[i] + " ");
        }
        printSubsequence(arr, k, i + 1, ans);
    }

    public static void main(String[] args) {
        int[] arr = { 2, 3, 5, 7 };
        int k = 10;
        printSubsequence(arr, k, 0, "");
    }
}
