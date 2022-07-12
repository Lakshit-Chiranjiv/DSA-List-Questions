package Aman_Bhaiya_DSA_List.Arrays;


public class LQ12 {
    class Pair{
        int min;
        int max;
    }

    //method 1
    Pair getMinMax(int arr[],int n){
        Pair minmax = new Pair();

        if(n == 1){
            minmax.min = arr[0];
            minmax.max = arr[0];
            return minmax;
        }
        
        minmax.min = arr[0];
        minmax.max = arr[0];

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
            minmax.min = arr[left];
            minmax.max = arr[left];
            return minmax;
        }

        if(left+1 == right){
            minmax.min = Math.min(arr[left], arr[right]);
            minmax.max = Math.max(arr[left], arr[right]);
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

        for(int i = p; i < (n-1); i+=2){
            minmax.max = arr[i] > arr[i+1] ? Math.max(arr[i], minmax.max) : Math.max(arr[i+1], minmax.max);
            minmax.min = arr[i] < arr[i+1] ? Math.min(arr[i], minmax.min) : Math.min(arr[i+1], minmax.min);
        }

        return minmax;
    }

    public static void main(String[] args) {
        LQ12 ob = new LQ12();
        int[] arr = {23,14,14,16,53,242,52,56,252,42,53,2,55,21};
        Pair ans = ob.getMinMax(arr, arr.length);
        System.out.println(ans.min);
        System.out.println(ans.max);
    }

}