package Aman_Bhaiya_DSA_List.Arrays;

public class LQ13 {
    //method 1
    void reverseArray(int[] arr){
        int start = 0;
        int end = arr.length - 1;

        while(start <= end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    void printArray(int[] arr){
        for(int i = 0;i < arr.length; i++){
            System.out.print(arr[i]+",");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        LQ13 ob = new LQ13();
        int[] arr = {23,14,14,16,53,242,52,56,252,42,53,2,55,21};
        ob.printArray(arr);
        ob.reverseArray(arr);
        ob.printArray(arr);
    }
}
