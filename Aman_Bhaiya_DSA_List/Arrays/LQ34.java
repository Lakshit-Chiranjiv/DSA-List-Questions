package Aman_Bhaiya_DSA_List.Arrays;

public class LQ34 {
    public static Boolean checkBit(int[] arr, int n){
        int bit_value = arr[n >> 5] & (1 << (n & 31));
        return bit_value != 0;
    }

    public static void setBit(int[] arr, int n){
        arr[n >> 5] |= (1 << (n & 31));
    }

    public static void main(String args[]){
        int a = 5;
        int b = 32;
        int array_size = (int)Math.ceil((double)Math.abs(b-a)/32);
        int[] arr = new int[array_size];

        for(int i=a; i<=b; i++){
            if(i%2 == 0 || i%5 == 0){
                setBit(arr, i-a);
            }
        }

        for(int i=a; i<=b; i++){
            if(checkBit(arr, i-a)){
                System.out.print(i + " ");
            }
        }

    }
}
