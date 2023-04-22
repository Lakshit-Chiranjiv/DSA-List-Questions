class Solution:
    def minInsertions(self, s: str) -> int:

        @cache
        def lcs(s1, s2, idx1, idx2):
            if idx1<0 or idx2<0:
                return 0
            
            if s1[idx1] == s2[idx2]:
                return 1 + lcs(s1, s2, idx1-1, idx2-1)
            
            return max(lcs(s1, s2, idx1-1, idx2), lcs(s1, s2, idx1, idx2-1))

        def longestPalindromeSubseq(s: str) -> int:
            return lcs(s, s[::-1], len(s)-1, len(s)-1)

        return len(s) - longestPalindromeSubseq(s)
    
# intuition:
# 1. We are allowed to insert any number of characters at any position.
# 2. So, if we find the longest palindromic subsequence, we can be sure about how many characters are already making up the palindrome part.
# 3. The remaining characters need to be inserted to make the whole string a palindrome.
# 4. The number of characters to be inserted is the difference between the length of the string and the length of the longest palindromic subsequence.
# 5. To find the longest palindromic subsequence, we can use the longest common subsequence algorithm with the string and its reverse.

# solution:
# 1. Define a function lcs(s1, s2, idx1, idx2) to find the longest common subsequence of s1 and s2.
# 2. If idx1 < 0 or idx2 < 0, return 0.
# 3. If s1[idx1] == s2[idx2], return 1 + lcs(s1, s2, idx1 - 1, idx2 - 1).
# 4. Else, return max(lcs(s1, s2, idx1 - 1, idx2), lcs(s1, s2, idx1, idx2 - 1)).
# 5. Define a function longestPalindromeSubseq(s) to find the longest palindromic subsequence of s.
# 6. Return lcs(s, s[::-1], len(s) - 1, len(s) - 1) where s[::-1] is the reverse of s.
# 7. Finally our answer is len(s) - longestPalindromeSubseq(s) where s is the input string.

# Time complexity: O(n^2) where n is the length of the input string as we are using the longest common subsequence algorithm to find the longest palindromic subsequence.

# Space complexity: O(n^2) where n is the length of the input string as we are using a 2D dp array to store the results of the longest common subsequence algorithm.