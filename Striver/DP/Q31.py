# minimum common supersequence

# recursive solution
def lcs(s1, s2, idx1, idx2):
    if idx1<0 or idx2<0:
        return 0
    
    if s1[idx1] == s2[idx2]:
        return 1 + lcs(s1, s2, idx1-1, idx2-1)
    
    return max(lcs(s1, s2, idx1-1, idx2), lcs(s1, s2, idx1, idx2-1))

def mcs(s1, s2):
    n = len(s1)
    m = len(s2)
    return n+m-lcs(s1, s2, n-1, m-1)


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

def mcsMem(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1] * m for _ in range(n)]
    return n+m-lcsMem(s1, s2, n-1, m-1, dp)

# tabulation
def lcsTab(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]

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

    #print mcs 
    i = n
    j = m
    ans = ""
    while i>0 and j>0:
        if s1[i-1] == s2[j-1]:
            ans += s1[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                ans += s1[i-1]
                i -= 1
            else:
                ans += s2[j-1]
                j -= 1
    while i>0:
        ans += s1[i-1]
        i -= 1
    while j>0:
        ans += s2[j-1]
        j -= 1
    print(ans[::-1])
    
    return dp[n][m]

def mcsTab(s1, s2):
    n = len(s1)
    m = len(s2)
    return n+m-lcsTab(s1, s2)

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

def mcsTabOpt(s1, s2):
    n = len(s1)
    m = len(s2)
    return n+m-lcsTabOpt(s1, s2)

s1 = "AGGTAB"
s2 = "GXTXAYB"

print(mcs(s1, s2))
print(mcsMem(s1, s2))
print(mcsTab(s1, s2))
print(mcsTabOpt(s1, s2))
