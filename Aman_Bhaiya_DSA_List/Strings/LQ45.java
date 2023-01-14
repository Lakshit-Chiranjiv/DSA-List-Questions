package Aman_Bhaiya_DSA_List.Strings;

public class LQ45 {
    public static void main(String[] args) {
        String[] keypad_alphabets = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        int[] alpha_key_values = {2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9};
        String inputString = "bsve";
        String outputString = "";
        for (int i = 0; i < inputString.length(); i++) {
            char ch = inputString.charAt(i);
            int index = ch - 'a';
            int key = alpha_key_values[index];
            String possibleAlphabets = keypad_alphabets[key];
            char possibleChar = possibleAlphabets.charAt(0);
            while(possibleChar <= ch){
                outputString += key+"";
                possibleChar++;
            }
        }
        System.out.println(outputString);
    }
}
