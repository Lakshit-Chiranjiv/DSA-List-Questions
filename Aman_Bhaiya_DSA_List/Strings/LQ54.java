package Aman_Bhaiya_DSA_List.Strings;

public class LQ54 {
    // Smallest window in a string containing all the characters of another string

    public static void main(String[] args) {
        String str = "this is a test string";
        String pat = "tist";
        System.out.println(smallestWindow(str, pat));
    }

    public static String smallestWindow(String str, String pat) {
        int[] fs = new int[256];
        int[] fp = new int[256];

        for (int i = 0; i < pat.length(); i++) {
            fp[pat.charAt(i)]++;
        }

        int count = 0;
        int start = 0;
        int minLen = Integer.MAX_VALUE;
        int startIndex = -1;

        for (int i = 0; i < str.length(); i++) {
            fs[str.charAt(i)]++;

            if (fp[str.charAt(i)] != 0 && fs[str.charAt(i)] <= fp[str.charAt(i)]) {
                count++;
            }

            if (count == pat.length()) {
                while (fs[str.charAt(start)] > fp[str.charAt(start)] || fp[str.charAt(start)] == 0) {
                    if (fs[str.charAt(start)] > fp[str.charAt(start)]) {
                        fs[str.charAt(start)]--;
                    }
                    start++;
                }

                int len = i - start + 1;
                if (minLen > len) {
                    minLen = len;
                    startIndex = start;
                }
            }
        }

        if (startIndex == -1) {
            return "-1";
        }

        return str.substring(startIndex, startIndex + minLen);
    }
}
