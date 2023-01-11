package Aman_Bhaiya_DSA_List.Strings;

public class LQ40 {
    public boolean isPalindrome(String s) {
        String r = "";
        
        for(int i = 0;i<s.length();i++){
            char c = s.charAt(i);
            if((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z'))
                r += Character.toLowerCase(c);
        }
        boolean x = new StringBuilder().append(r).reverse().toString().equals(r);
        return x;
        
    }
}
