package Striver.Recursion;

public class q13 {
    // print the count of subsequences which sums to k
    public static int printSubsequence(int[] arr, int k, int i, String ans) {
        if (i == arr.length) {
            if (k == 0) {
                System.out.println(ans);
                return 1;
            }
            return 0;
        }
        int count = 0;
        count += printSubsequence(arr, k - arr[i], i + 1, ans + arr[i] + " ");
        count += printSubsequence(arr, k, i + 1, ans);
        return count;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        int k = 10;
        System.out.println(printSubsequence(arr, k, 0, ""));
    }
}
