package Striver.Recursion;

public class q10 {
    // print all the subsequence of an array using recursion
    public static void printSubsequence(int[] arr, int index, String ans) {
        if (index == arr.length) {
            System.out.println(ans);
            return;
        }
        printSubsequence(arr, index + 1, ans + arr[index] + " ");
        printSubsequence(arr, index + 1, ans);
    }

    // print all the subsequence of a string using recursion
    public static void printSubsequence(String str, int index, String ans) {
        if (index == str.length()) {
            System.out.println(ans);
            return;
        }
        printSubsequence(str, index + 1, ans + str.charAt(index));
        printSubsequence(str, index + 1, ans);
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 };
        printSubsequence(arr, 0, "");
        String str = "abc";
        printSubsequence(str, 0, "");
    }
}
