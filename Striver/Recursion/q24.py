# palindrome partitioning of a string
# return all possible partitions of a string such that each partition is a palindrome
# eg: "nitin" -> "n i t i n", "n iti n", "nitin"

def isPalindrome(s):
    return s == s[::-1]

def palindromePartitioning(s, i, n, path, result):
    if i >= n:
        result.append(path)
        return
    for j in range(i, n):
        if isPalindrome(s[i:j+1]):
            palindromePartitioning(s, j+1, n, path + [s[i:j+1]], result)

s = "nitin"
result = []
palindromePartitioning(s, 0, len(s), [], result)
print(result)