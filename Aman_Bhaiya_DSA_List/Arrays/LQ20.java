package Aman_Bhaiya_DSA_List.Arrays;

import java.util.HashSet;

public class LQ20 {
    public int[] repeatedNumber(final int[] A) {
        HashSet<Integer> set=new HashSet<>();
       int repeated=0, notContained=0;
       for(int i=0;i<A.length;i++){
           if(set.contains(A[i]))
               repeated=A[i];
           else
               set.add(A[i]);
       }
       for(int i=1;i<=A.length;i++){
           if(!set.contains(i)){
               notContained=i;
               break;
           }
       }
       return new int[]{repeated,notContained};
   }
}
