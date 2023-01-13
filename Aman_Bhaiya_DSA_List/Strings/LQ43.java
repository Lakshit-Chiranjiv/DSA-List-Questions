package Aman_Bhaiya_DSA_List.Strings;

public class LQ43 {
    public String removeConsecutiveCharacter(String S){
        String ans = S.charAt(0)+"";
        for(int i = 1; i < S.length(); i++){
            char c = S.charAt(i);
            char d = S.charAt(i-1);
            if(c != d)
                ans += c;
        }
        
        return ans;
    }

    public static void main(String[] args) {
        LQ43 obj = new LQ43();
        String S = "aabccba";
        System.out.println(obj.removeConsecutiveCharacter(S));
    }
}