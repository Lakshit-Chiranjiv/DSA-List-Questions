# print the longest common subsequence using tabulation method

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

    
    i = n
    j = m
    ans = []
    while i>0 and j>0:
        if s1[i-1] == s2[j-1]:
            ans.append(s1[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    ans.reverse()
    print(''.join(ans))
    
    return dp[n][m]

s1 = "abcdaf"
s2 = "acbcfx"
print(lcsTab(s1, s2))