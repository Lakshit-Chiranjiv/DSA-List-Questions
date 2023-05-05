class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = 'aeiou'
        c = 0
        n = len(s)
        for i in range(k):
            if s[i] in v:
                c += 1
        mx = c
        for i in range(k,n):
            if s[i-k] in v:
                c -= 1
            if s[i] in v:
                c += 1
            mx = max(mx,c)

        return mx
    
# intuition:
# 1. We will use a sliding window of size k to find the maximum number of vowels in a substring of size k.
# 2. At each step, we will add the vowel count of the current character and subtract the vowel count of the first character of the previous window.
# 3. We will keep track of the maximum vowel count and return it in the end.

# solution:
# 1. Initialize a variable to store the vowel count of the current window.
# 2. Iterate over the first k characters of the string and add the vowel count of each character to the variable.
# 3. Initialize a variable to store the maximum vowel count and store the vowel count of the current window in it.
# 4. Iterate over the remaining characters of the string. Subtract the vowel count of the first character of the previous window from the variable. Add the vowel count of the current character to the variable.
# 5. Update the maximum vowel count if the vowel count of the current window is greater than it.
# 6. Return the maximum vowel count.

# Time Complexity: O(n) where n is the length of the string. We iterate over the string once and perform constant time operations at each step.

# Space Complexity: O(1) as we use constant extra space.