# longest string chain

def longestStrChain(words):
    words.sort(key=len)
    n = len(words)
    dp = [1]*n
    mx = 1
    for i in range(1, n):
        for j in range(i):
            if len(words[i]) - len(words[j]) == 1:
                if isPredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
                    mx = max(mx, dp[i])

    return mx

def isPredecessor(s1, s2):
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == len(s1) and j <= len(s2)

words = ["a","b","ba","bca","bda","bdca"]
print(longestStrChain(words))