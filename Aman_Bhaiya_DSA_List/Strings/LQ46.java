package Aman_Bhaiya_DSA_List.Strings;

import java.util.HashMap;
import java.util.Map;

public class LQ46 {
    public static void main(String[] args){
        Map <Character, Integer> mp = new HashMap<>();
        String inputString = "koosckk";
        for(char ch: inputString.toCharArray()){
            mp.put(ch, mp.getOrDefault(ch, 0)+1);
        }
        
        for(Map.Entry<Character, Integer> entry: mp.entrySet()){
            if(entry.getValue() > 1){
                System.out.println(entry.getKey() + " " + entry.getValue());
            }
        }
    }
}
