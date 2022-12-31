# Check if string is palindrome or not using recursion

# checking string palindrome using 2 pointer approach recursively
def isPalindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return isPalindrome(s, start + 1, end - 1)

# checking string palindrome using single parameter recursively
def isPalindrome2(s, n):
    if n >= len(s) // 2:
        return True
    if s[n] != s[len(s) - n - 1]:
        return False
    return isPalindrome2(s, n + 1)

s = "abba"
print(isPalindrome(s, 0, len(s) - 1))
print(isPalindrome2(s, 0))