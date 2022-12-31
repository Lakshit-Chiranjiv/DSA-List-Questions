package Striver.Recursion;

public class q8 {
    // Check if string is palindrome or not using recursion
    
    //2 pointer approach recursively
    public static boolean isPalindrome(String str, int start, int end) {
        if (start >= end)
            return true;
        if (str.charAt(start) != str.charAt(end))
            return false;
        return isPalindrome(str, start + 1, end - 1);
    }

    //single parameter approach recursively
    public static boolean isPalindrome2(String str) {
        if (str.length() == 0 || str.length() == 1)
            return true;
        if (str.charAt(0) != str.charAt(str.length() - 1))
            return false;
        return isPalindrome2(str.substring(1, str.length() - 1));
    }

    //single parameter approach recursively
    public static boolean isPalindrome3(String str, int start) {
        if (start >= str.length() / 2)
            return true;
        if (str.charAt(start) != str.charAt(str.length() - 1 - start))
            return false;
        return isPalindrome3(str, start + 1);
    }

    public static void main(String[] args) {
        String str = "abba";
        System.out.println(isPalindrome(str, 0, str.length() - 1));
    }
    
}
