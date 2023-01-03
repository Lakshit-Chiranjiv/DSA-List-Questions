package Striver.Recursion;

import java.util.ArrayList;
import java.util.List;

public class q18 {
    // print all permutations of a string/array

    public static void main(String[] args) {
        String str = "abc";
        char[] arr = str.toCharArray();
        boolean[] elementsMap = new boolean[arr.length];
        List<Character> perm = new ArrayList<>();
        List<List<Character>> ans = new ArrayList<>();
        allPermutations(arr, elementsMap, perm, ans);
    }

    public static void allPermutations(char[] arr, boolean[] elementsMap, List<Character> perm, List<List<Character>> ans) {
        if (perm.size() == arr.length) {
            ans.add(new ArrayList<>(perm));
            return;
        }

        for (int i = 0; i < arr.length; i++) {
            if (elementsMap[i]) continue;

            elementsMap[i] = true;
            perm.add(arr[i]);
            allPermutations(arr, elementsMap, perm, ans);
            elementsMap[i] = false;
            perm.remove(perm.size() - 1);
        }
    }
}
