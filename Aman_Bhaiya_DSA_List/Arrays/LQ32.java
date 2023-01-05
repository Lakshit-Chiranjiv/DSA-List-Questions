package Aman_Bhaiya_DSA_List.Arrays;

public class LQ32 {

    // minimum merge operations to make an array palindrome

    public static void main(String[] args) {
        int[] arr = {1, 4, 5, 9, 1};
        int n = arr.length;
        int i = 0;
        int j = n-1;
        int count = 0;
        while(i<j){
            if(arr[i]==arr[j]){
                i++;
                j--;
            }
            else if(arr[i]<arr[j]){
                arr[i+1] += arr[i];
                i++;
                count++;
            }
            else{
                arr[j-1] += arr[j];
                j--;
                count++;
            }
        }
        System.out.println(count);
    }

    //recursive solution
    public static int minMerge(int[] arr, int i, int j){
        if(i>=j){
            return 0;
        }
        if(arr[i]==arr[j]){
            return minMerge(arr, i+1, j-1);
        }
        else if(arr[i]<arr[j]){
            arr[i+1] += arr[i];
            return 1 + minMerge(arr, i+1, j);
        }
        else{
            arr[j-1] += arr[j];
            return 1 + minMerge(arr, i, j-1);
        }
    }
    
}
