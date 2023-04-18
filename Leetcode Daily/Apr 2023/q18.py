class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        ans = ''
        while i < len(word1) and j < len(word2):
            ans += word1[i]+word2[j]
            i += 1
            j += 1

        while i < len(word1):
            ans += word1[i]
            i += 1

        while j < len(word2):
            ans += word2[j]
            j += 1

        return ans
    

# intuition:
# 1. Its a simple string concatenation problem where iterating both strings in parallel is the simplest solution.
# 2. The only thing to watch out for is the case where one string is longer than the other. In that case, we need to append the remaining characters of the longer string to the answer.

# solution:
# 1. Initialize two pointers i and j to 0.
# 2. Initialize an empty string ans.
# 3. While i < len(word1) and j < len(word2), append word1[i] and word2[j] to ans and increment i and j by 1.
# 4. Then for the extra characters case, append the remaining characters of word1 to ans if i < len(word1) and the remaining characters of word2 to ans if j < len(word2) using while loops independently.
# 5. Return ans.

# time complexity: O(n) where n is the length of the longer string between word1 and word2 because we iterate through both strings in parallel and then append the remaining characters of the longer string to ans.
# space complexity: O(1) because we only use constant space to store the pointers i, j apart from the answer string ans.