package Aman_Bhaiya_DSA_List.Strings;

import java.util.*;
public class LQ47{
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> mp = new HashMap<>();
        int curr = 0, mxl = 0;
        for(int i = 0; i < s.length(); i++){
            if(mp.getOrDefault(s.charAt(i),-1) == -1 || mp.getOrDefault(s.charAt(i),-1) < (i - curr)){
                mp.put(s.charAt(i),i);
                curr += 1;
                mxl = Math.max(curr,mxl);
            }
            else{
                curr = (i - mp.get(s.charAt(i)));
                mp.put(s.charAt(i),i);
            }
        }

        return mxl;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        LQ47 obj = new LQ47();
        System.out.println(obj.lengthOfLongestSubstring(s));
        sc.close();
    }
}