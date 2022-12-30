package Aman_Bhaiya_DSA_List.Arrays;

import java.util.Arrays;

public class LQ21 {
    //kth largest element in an array in O(n) time and O(1) space
    public static void main(String[] args) {
        int[] arr = {7, 10, 4, 3, 20, 15};
        int k = 3;
        System.out.println(kthLargest(arr, k));
    }

    //O(nlogn) time and O(1) space
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length-k];
    }

    //O(n) time and O(1) space
    public static int kthLargest(int[] arr, int k) {
        int n = arr.length;
        int l = 0, r = n - 1;
        while (l <= r) {
            int p = partition(arr, l, r);
            if (p == n - k) {
                return arr[p];
            } else if (p > n - k) {
                r = p - 1;
            } else {
                l = p + 1;
            }
        }
        return -1;
    }

    public static int partition(int[] arr, int l, int r) {
        int pivot = arr[r];
        int i = l - 1;
        for (int j = l; j < r; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, r);
        return i + 1;
    }

    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
}
