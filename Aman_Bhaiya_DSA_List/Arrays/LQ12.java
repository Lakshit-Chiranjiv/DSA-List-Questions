package Aman_Bhaiya_DSA_List.Arrays;

public class LQ12 {
    private class Pair{
        int min;
        int max;
    }

    //method 1
    Pair getMinMax(int arr[],int n){
        Pair minmax = new Pair();

        if(n == 1){
            minmax.min = arr[0];
            minmax.max = arr[0];
        }

        for(int i = 0;i < n;i++){
            minmax.max = Math.max(minmax.max, arr[i]);
            minmax.min = Math.min(minmax.min, arr[i]);
        }

        return minmax;
    }
}
