# longest palindromic subsequence length

# recursive solution
def lcs(s1, s2, idx1, idx2):
    if idx1<0 or idx2<0:
        return 0
    
    if s1[idx1] == s2[idx2]:
        return 1 + lcs(s1, s2, idx1-1, idx2-1)
    
    return max(lcs(s1, s2, idx1-1, idx2), lcs(s1, s2, idx1, idx2-1))

def longestPalindromeSubseq(s: str) -> int:
    return lcs(s, s[::-1], len(s)-1, len(s)-1)


# memoization
def lcsMem(s1, s2, idx1, idx2, dp):
    if idx1<0 or idx2<0:
        return 0
    
    if dp[idx1][idx2] != -1:
        return dp[idx1][idx2]
    
    if s1[idx1] == s2[idx2]:
        dp[idx1][idx2] = 1 + lcsMem(s1, s2, idx1-1, idx2-1, dp)
        return dp[idx1][idx2]
    
    dp[idx1][idx2] = max(lcsMem(s1, s2, idx1-1, idx2, dp), lcsMem(s1, s2, idx1, idx2-1, dp))
    return dp[idx1][idx2]

def longestPalindromeSubseqMem(s: str) -> int:
    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    return lcsMem(s, s[::-1], n-1, n-1, dp)

# tabulation
def lcsTab(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(0,m):
        dp[0][i] = 0

    for i in range(0,n):
        dp[i][0] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]

def longestPalindromeSubseqTab(s: str) -> int:
    return lcsTab(s, s[::-1])

# space optimization
def lcsTabOpt(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [0] * (m+1)
    curr = [0] * (m+1)

    for i in range(1,m+1):
        dp[i] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + dp[j-1]
            else:
                curr[j] = max(dp[j], curr[j-1])
        dp = curr
        curr = [0] * (m+1)

    return dp[m]

def longestPalindromeSubseqTabOpt(s: str) -> int:
    return lcsTabOpt(s, s[::-1])

s = "bbbab"
print(longestPalindromeSubseq(s))
print(longestPalindromeSubseqMem(s))
print(longestPalindromeSubseqTab(s))
print(longestPalindromeSubseqTabOpt(s))
