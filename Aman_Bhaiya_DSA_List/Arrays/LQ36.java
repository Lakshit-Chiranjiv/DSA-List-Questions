package Aman_Bhaiya_DSA_List.Arrays;

public class LQ36 {
    // print all possible combinations of r elements in a n-size array

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5 };
        int r = 3;
        int n = arr.length;
        printCombination(arr, n, r);
    }

    public static void printCombination(int[] arr, int n, int r) {
        int[] data = new int[r];
        combinationUtil(arr, data, 0, n - 1, 0, r);
    }

    public static void combinationUtil(int[] arr, int[] data, int start, int end, int index, int r) {
        if (index == r) {
            for (int j = 0; j < r; j++) {
                System.out.print(data[j] + " ");
            }
            System.out.println();
            return;
        }

        for (int i = start; i <= end && end - i + 1 >= r - index; i++) {
            data[index] = arr[i];
            combinationUtil(arr, data, i + 1, end, index + 1, r);
        }
    }
}
