class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        @cache
        def lcs(s1, s2, idx1, idx2):
            if idx1<0 or idx2<0:
                return 0
            
            if s1[idx1] == s2[idx2]:
                return 1 + lcs(s1, s2, idx1-1, idx2-1)
            
            return max(lcs(s1, s2, idx1-1, idx2), lcs(s1, s2, idx1, idx2-1))

        return lcs(s, s[::-1], n-1, n-1)
    
# intution:
# 1. The longest palindromic subsequence is actually the longest common subsequence of the string and its reverse.
# 2. The longest common subsequence is a classic dynamic programming problem. The recurrence relation goes like this:
# 3. We take two indices, idx1 and idx2, and compare the characters at those indices in the two strings. If they are equal, we add 1 to the result of the function call with idx1 and idx2 decremented by 1. If they are not equal, we take the maximum of the function call with idx1 decremented by 1 and idx2 unchanged, and the function call with idx1 unchanged and idx2 decremented by 1.
# 4. The base case is when either of the indices is less than 0. In that case, we return 0.
# 5. We can memoize the function call using the functools.cache decorator. This will make the function run in O(n^2) time and O(n^2) space.
# 6. For longest palindromic subsequence, we can just call the lcs function with the string and its reverse as the first two arguments, and the length of the string minus 1 as the last two arguments.

# solution:
# 1. Create a recursive lcs function that takes four arguments: s1, s2, idx1, and idx2.
# 2. If either of the indices is less than 0, return 0.
# 3. If the characters at the indices in the two strings are equal, return 1 plus the result of the function call with idx1 and idx2 decremented by 1.
# 4. Otherwise, return the maximum of the function call with idx1 decremented by 1 and idx2 unchanged, and the function call with idx1 unchanged and idx2 decremented by 1.
# 5. Create a variable n and set it equal to the length of the string.
# 6. Return the result of calling the lcs function with the string and its reverse as the first two arguments, and n minus 1 as the last two arguments.

# complexity:
# 1. Time: O(n^2) because we are memoizing the function call.
# 2. Space: O(n^2) + internal recursion stack space because we are memoizing the function call.