package Striver.Recursion;

public class q12 {
    // Print a single subsequence which sums to k
    public static boolean printSubsequence(int[] arr, int k, int i, String ans) {
        if (i == arr.length) {
            if (k == 0) {
                System.out.println(ans);
                return true;
            }
            return false;
        }
        if(printSubsequence(arr, k - arr[i], i + 1, ans + arr[i] + " ")==true) return true;
        if(printSubsequence(arr, k, i + 1, ans)==true) return true;
        return false;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        int k = 10;
        printSubsequence(arr, k, 0, "");
    }
}
