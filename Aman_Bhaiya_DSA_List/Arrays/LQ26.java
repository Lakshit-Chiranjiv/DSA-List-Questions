package Aman_Bhaiya_DSA_List.Arrays;

public class LQ26 {
    public boolean pairInSortedRotated(int arr[], int n, int x) {
        int i = -1;
        int s = 0, e = n - 1;
        while(s <= e) {
            int mid = (s + e) / 2;
            if(arr[mid] > arr[mid + 1]) {
                i = mid;
                break;
            }
            if(arr[mid] < arr[s]) {
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }

        if(i == -1)
            i = n - 1;
        
        int l = (i + 1) % n;
        int r = i;
        while (l != r) {
            if (arr[l] + arr[r] == x) {
                return true;
            }
            if (arr[l] + arr[r] < x) {
                l = (l + 1) % n;
            } else {
                r = (n + r - 1) % n;
            }
        }
        return false;
    }
}
