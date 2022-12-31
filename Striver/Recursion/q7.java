package Striver.Recursion;

public class q7 {
    // Reverse an array using recursion
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        reverse(arr, 0, arr.length - 1);
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }

    //reversing array by 2 pointer method recusively
    public static void reverse(int[] arr, int start, int end) {
        if (start >= end) {
            return;
        }
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        reverse(arr, start + 1, end - 1);
    }

    //reversing array by passing single parameter recusively
    public static void reverse2(int[] arr, int start) {
        if (start >= arr.length / 2) {
            return;
        }
        int temp = arr[start];
        arr[start] = arr[arr.length - 1 - start];
        arr[arr.length - 1 - start] = temp;
        reverse2(arr, start + 1);
    }
}
