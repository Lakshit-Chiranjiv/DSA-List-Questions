package Striver.DP;

import java.util.Arrays;

public class Q45 {
    // longest string chain length

    public int longestStringChain(String[] words) {
        int n = words.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        int max = 1;
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if(isPredecessor(words[j], words[i])){
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
            max = Math.max(max, dp[i]);
        }
        return max;
    }

    public boolean isPredecessor(String s1, String s2){
        if(s1.length() + 1 != s2.length()) return false;
        int i = 0, j = 0;
        while(i < s1.length() && j < s2.length()){
            if(s1.charAt(i) == s2.charAt(j)){
                i++;
                j++;
            }else{
                j++;
            }
        }
        return i == s1.length() && j == s2.length();
    }
}
