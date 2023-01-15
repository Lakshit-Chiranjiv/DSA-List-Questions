package Aman_Bhaiya_DSA_List.Strings;

public class LQ48 {
    public int characterReplacement(String s, int k) {

        int lo = 1;
        int hi = s.length() + 1;

        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;

            if (canMakeValidSubstring(s, mid, k)) {
                lo = mid;
            } else {
                hi = mid;
            }
        }

        return lo;
    }

    private Boolean canMakeValidSubstring(
            String s,
            int substringLength,
            int k) {

        int[] freqMap = new int[26];
        int maxFrequency = 0;
        int start = 0;
        for (int end = 0; end < s.length(); end += 1) {
            freqMap[s.charAt(end) - 'A'] += 1;

            if (end + 1 - start > substringLength) {
                freqMap[s.charAt(start) - 'A'] -= 1;
                start += 1;
            }
            maxFrequency = Math.max(maxFrequency, freqMap[s.charAt(end) - 'A']);
            if (substringLength - maxFrequency <= k) {
                return true;
            }
        }
        return false;
    }
}

