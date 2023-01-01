package Striver.Recursion;

public class q11{
    //Print all the subsequences which sum to k
    public static void main(String[] args) {
        int[] arr = {10, 12, 20, 15, -25, 30, 24};
        int k = 25;
        int[] ans = new int[arr.length];
        printSubsequences(arr, 0, ans, 0,0, k);
    }

    private static void printSubsequences(int[] arr, int i, int[] ans, int j, int sum, int k) {
        if(i == arr.length){
            if(sum == k){
                for(int x = 0; x < j; x++){
                    System.out.print(ans[x] + " ");
                }
                System.out.println();
            }
            return;
        }
        ans[j] = arr[i];
        printSubsequences(arr, i + 1, ans, j + 1,sum+arr[i], k);
        printSubsequences(arr, i + 1, ans, j,sum, k);
    }
}