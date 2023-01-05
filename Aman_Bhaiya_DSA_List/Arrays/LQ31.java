package Aman_Bhaiya_DSA_List.Arrays;


import java.util.*;
public class LQ31 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][2];
        for(int i=0;i<n;i++){
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }
        //sorting array based on start time
        Arrays.sort(arr, (a,b)->a[0]-b[0]);

        Stack<int[]> st = new Stack<>();
        st.push(arr[0]);
        for(int i=1;i<n;i++){
            int[] top = st.peek();
            if(top[1]<arr[i][0]){
                st.push(arr[i]);
            }
            else if(top[1]<arr[i][1]){
                top[1] = arr[i][1];
                st.pop();
                st.push(top);
            }
        }
        while(!st.isEmpty()){
            int[] top = st.pop();
            System.out.println(top[0]+" "+top[1]);
        }
    }

    // in-place solution
    public static void mergeIntervals(int[][] arr, int n){
        //sorting array based on start time
        Arrays.sort(arr, (a,b)->a[0]-b[0]);

        int index = 0;
        for(int i=1;i<n;i++){
            if(arr[index][1]<arr[i][0]){
                index++;
                arr[index][0] = arr[i][0];
                arr[index][1] = arr[i][1];
            }
            else if(arr[index][1]<arr[i][1]){
                arr[index][1] = arr[i][1];
            }
        }
        for(int i=0;i<=index;i++){
            System.out.println(arr[i][0]+" "+arr[i][1]);
        }
    }
}
