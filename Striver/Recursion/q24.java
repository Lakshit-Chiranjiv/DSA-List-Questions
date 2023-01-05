package Striver.Recursion;

import java.util.ArrayList;
import java.util.List;

public class q24 {
    // palindrome partitioning of a string
    // return all possible partitions of a string such that each partition is a palindrome
    // eg: "nitin" -> "n i t i n", "n iti n", "nitin"

    public static void main(String[] args) {
        String s = "nitin";
        int n = s.length();
        List<String> temp = new ArrayList<>();
        List<List<String>> ans = new ArrayList<>();
        solvePalindromePartitioning(s, n, temp, ans, 0);
        System.out.println(ans);
    }

    public static void solvePalindromePartitioning(String s, int n, List<String> temp, List<List<String>> ans, int i) {
        if (i == n) {
            ans.add(new ArrayList<>(temp));
            return;
        }
        for (int j = i; j < n; j++) {
            if (isPalindrome(s, i, j)) {
                temp.add(s.substring(i, j + 1));
                solvePalindromePartitioning(s, n, temp, ans, j + 1);
                temp.remove(temp.size() - 1);
            }
        }
    }

    public static boolean isPalindrome(String s, int i, int j) {
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }


}
