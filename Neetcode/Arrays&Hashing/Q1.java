package Neetcode.Arrays&Hashing;

import java.util.*;

public class Q1 {
    // contains duplicate

    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set=new HashSet<>();
        for(int elements: nums){
            if(set.contains(elements))
                return true;
            else
                set.add(elements);
        }
        return false;
    }
}
