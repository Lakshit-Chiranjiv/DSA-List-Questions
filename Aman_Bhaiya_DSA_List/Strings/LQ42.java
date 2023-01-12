package Aman_Bhaiya_DSA_List.Strings;

import java.util.Stack;

public class LQ42 {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(c == '(' || c == '{' || c == '[')
                st.push(c);
                
            else{
                if(c == ')'){
                    if(st.empty() || st.pop() != '(')
                        return false;
                }
                if(c == '}'){
                    if(st.empty() || st.pop() != '{')
                        return false;
                }
                if(c == ']'){
                    if(st.empty() || st.pop() != '[')
                        return false;
                }
            }
        }
        
        return st.empty();
    }
}
