package Striver.Recursion;

import java.util.ArrayList;
import java.util.List;

public class q26 {
    // kth permutation sequence for a set of n numbers

    public static void main(String[] args) {
        int n = 3;
        int k = 3;
        String ans = "";
        List<Integer> nums = new ArrayList<>();
        int fact = 1;
        for (int i = 1; i < n; i++) {
            nums.add(i);
            fact *= i;
        }
        nums.add(n);
        k--;

        while (true) {
            ans += nums.get(k / fact);
            nums.remove(k / fact);
            if (nums.size() == 0)
                break;
            k = k % fact;
            fact = fact / nums.size();
        }
    }
}
