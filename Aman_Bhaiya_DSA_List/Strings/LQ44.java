package Aman_Bhaiya_DSA_List.Strings;

public class LQ44 {
    public String longestCommonPrefix(String[] strs) {
        int smallest_str_size = strs[0].length();
        String smallest_str = strs[0];
        for(int i = 1; i < strs.length; i++){
            if(strs[i].length() < smallest_str_size){
                smallest_str_size = strs[i].length();
                smallest_str = strs[i];
            }
        }

        for(int i = 0; i < strs.length; i++){
            if(strs[i].substring(0,smallest_str_size).equals(smallest_str)){
                continue;
            }
            else{
                smallest_str_size -= 1;
                if(smallest_str_size < 0)
                    return "";
                smallest_str = smallest_str.substring(0,smallest_str_size);
                i = -1;
            }
        }
        
        return smallest_str;
        
    }

    public static void main(String[] args) {
        LQ44 obj = new LQ44();
        String[] strs = {"flower","flow","flight"};
        System.out.println(obj.longestCommonPrefix(strs));
    }
}
