package Aman_Bhaiya_DSA_List.Strings;

import java.util.ArrayList;
import java.util.List;

public class LQ52 {
    // next permutation
    public static List<Integer> nextPermutation(int N, int[] arr){
        List<Integer> list = new ArrayList<>();
        if(N==1){
            list.add(arr[0]);
            return list;
        }
        int i = N-2;
        while(i>=0 && arr[i]>=arr[i+1]){
            i--;
        }
        if(i>=0){
            int j = N-1;
            while(arr[j]<=arr[i]){
                j--;
            }
            swap(arr, i, j);
        }
        reverse(arr, i+1, N-1);
        for(int k=0; k<N; k++){
            list.add(arr[k]);
        }
        return list;
    }

    public static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void reverse(int[] arr, int i, int j){
        while(i<j){
            swap(arr, i, j);
            i++;
            j--;
        }
    }
}
