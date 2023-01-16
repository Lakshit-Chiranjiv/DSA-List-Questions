package Aman_Bhaiya_DSA_List.Strings;
import java.util.*;
public class LQ49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList<>();
        Map<String,List<String>> mp = new HashMap<>();
        
        for(int i = 0; i < strs.length; i++){
            char temp[] = strs[i].toCharArray();
            Arrays.sort(temp);
            String sorted_str = new String(temp);
            if(mp.getOrDefault(sorted_str, new ArrayList<String>()).size() == 0)
                mp.put(sorted_str, new ArrayList<String>(Arrays.asList(strs[i])));
            else
                mp.get(sorted_str).add(strs[i]);
        }

        for(Map.Entry<String,List<String>> mpEl : mp.entrySet()){
            ans.add(mpEl.getValue());
        }

        return ans;
    }
}
