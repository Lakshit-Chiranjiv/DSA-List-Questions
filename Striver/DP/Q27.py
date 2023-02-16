# longest common substring

# tabulation

def lcsTab(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    ansLen = 0
    for i in range(0,m):
        dp[0][i] = 0

    for i in range(0,n):
        dp[i][0] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                ansLen = max(ansLen, dp[i][j])
            else:
                dp[i][j] = 0
    
    return ansLen


s1 = "abcdaf"
s2 = "acbcfx"

print(lcsTab(s1, s2))