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

    //method 2
    Pair getMinMax2(int arr[],int left, int right){
        Pair minmax = new Pair();
        Pair mmleft = new Pair();
        Pair mmright = new Pair();
        int mid;

        if(left == right){
            minmax.min = arr[0];
            minmax.max = arr[0];
            return minmax;
        }

        if(left+1 == right){
            minmax.min = Math.min(arr[0], arr[1]);
            minmax.max = Math.max(arr[0], arr[1]);
            return minmax;
        }

        mid = (left + right)/ 2;
        mmleft = getMinMax2(arr, left, mid);
        mmright = getMinMax2(arr, mid+1, right);

        minmax.max = Math.max(mmleft.max,mmright.max);
        minmax.min = Math.min(mmleft.min,mmright.min);

        return minmax;
    }

    //method 3
    Pair getMinMax3(int arr[],int n){
        Pair minmax = new Pair();
        int p;

        if(n%2 == 0){
            p = 2;
            minmax.max = Math.max(arr[0],arr[1]);
            minmax.min = Math.min(arr[0],arr[1]);
        }
        else{
            p = 1;
            minmax.max = arr[0];
            minmax.min = arr[0];
        }

        for(int i = p; i < n-1; i++){
            minmax.max = arr[i] > arr[i+1] ? Math.max(arr[i], minmax.max) : Math.max(arr[i+1], minmax.max);
            minmax.max = arr[i] < arr[i+1] ? Math.min(arr[i], minmax.min) : Math.min(arr[i+1], minmax.min);
        }

        return minmax;
    }
}
