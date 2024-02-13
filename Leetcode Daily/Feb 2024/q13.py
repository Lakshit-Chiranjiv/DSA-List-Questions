class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        return ""


# Time complexity: O(n * m)
# Space complexity: O(1)
    
# We iterate through the list of words and check if the word is a palindrome. If it is, we return the word. If no word is a palindrome, we return an empty string.