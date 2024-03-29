package Neetcode.ArraysHashing;

public class Q2 {
    public boolean isAnagram(String s, String t) {
        int[] occ = new int[26];
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            int idx = ((int)c) - 97;
            occ[idx]++;
        }
        for(int i = 0; i < t.length(); i++){
            char c = t.charAt(i);
            int idx = ((int)c) - 97;
            occ[idx]--;
        }
        for(int i = 0; i < 26; i++){
            if(occ[i] != 0)
                return false;
        }
        return true;
    }
}
