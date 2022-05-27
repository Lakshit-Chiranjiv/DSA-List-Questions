// Even and Odd
class GFG {
    static void reArrange(int[] arr, int N) {
        // code here
        int nextEven = 0;
        int nextOdd = 1;
        
        for(int i = 0; i < N-1; i++){
            if(i%2 == 0 && arr[i]%2 != 0){
                if(arr[nextOdd]%2 == 0){
                    int tmp = arr[i];
                    arr[i] = arr[nextOdd];
                    arr[nextOdd] = tmp;
                }
                else
                    i--;
                nextOdd += 2;
            }
            else if(i%2 != 0 && arr[i]%2 == 0){
                if(arr[nextEven]%2 != 0){
                    int tmp = arr[i];
                    arr[i] = arr[nextEven];
                    arr[nextEven] = tmp;
                }
                else
                    i--;
                nextEven += 2;
            }
        }
        
    }
};