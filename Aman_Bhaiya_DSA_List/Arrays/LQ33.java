package Aman_Bhaiya_DSA_List.Arrays;

import java.util.Collection;
import java.util.Collections;
import java.util.List;

class LQ33{
    //print largest number by arranging elements of array

    public static void printLargest(List<String> arr){
        Collections.sort(arr, (X, Y) -> (Y + X).compareTo(X + Y));
        for(String s:arr){
            System.out.print(s);
        }
    }

    public static void main(String[] args) {
        List<String> arr = List.of("54", "546", "548", "60");
        printLargest(arr);
    }
}