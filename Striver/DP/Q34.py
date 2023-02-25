# wildcard string matching
# ? - matches with any single character
# * - matches with any sequence of characters or empty string

# s is the string with ? and *
# p is the normal string

#recursive solution
def isMatch(s, p, i, j):
    if i < 0 and j < 0:
        return True
    if i < 0 and j >= 0:
        return False
    if j < 0 and i >= 0:
        for k in range(i+1):
            if s[k] != '*':
                return False
        return True
    
    if s[i] == p[j] or s[i] == '?':
        return isMatch(s, p, i-1, j-1)
    
    if s[i] == '*':
        return isMatch(s, p, i-1, j) or isMatch(s, p, i, j-1)
    
    return False


# memoization solution
def isMatchMem(s, p, i, j, dp):
    if i < 0 and j < 0:
        return True
    if i < 0 and j >= 0:
        return False
    if j < 0 and i >= 0:
        for k in range(i+1):
            if s[k] != '*':
                return False
        return True
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if s[i] == p[j] or s[i] == '?':
        dp[i][j] = isMatchMem(s, p, i-1, j-1, dp)
        return dp[i][j]
    
    if s[i] == '*':
        dp[i][j] = isMatchMem(s, p, i-1, j, dp) or isMatchMem(s, p, i, j-1, dp)
        return dp[i][j]
    
    dp[i][j] = False
    return dp[i][j]


# tabulation solution
def isMatchTab(s, p):
    n = len(s)
    m = len(p)
    dp = [[False for i in range(m+1)] for j in range(n+1)]
    dp[0][0] = True

    for j in range(1,m+1):
        dp[0][j] = False

    for i in range(1,n+1):
        flag = True
        for k in range(1,i+1):
            if s[k-1] != '*':
                flag = False
                break
        dp[i][0] = flag

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1] == p[j-1] or s[i-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif s[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j] = False

    return dp[n][m]


# space optimization solution
def isMatchSpace(s, p):
    n = len(s)
    m = len(p)
    dp = [False for i in range(m+1)]
    curr = [False for i in range(m+1)]
    dp[0] = True

    # for j in range(1,m+1):
    #     dp[j] = False


    for i in range(1,n+1):
        flag = True
        for k in range(1,i+1):
            if s[k-1] != '*':
                flag = False
                break
        curr[0] = flag
        for j in range(1,m+1):
            if s[i-1] == p[j-1] or s[i-1] == '?':
                curr[j] = dp[j-1]
            elif s[i-1] == '*':
                curr[j] = curr[j-1] or dp[j]
            else:
                curr[j] = False
        dp = curr.copy()

    return dp[m]


s = "b*c*"
p = "backing"

print(isMatch(s, p, len(s)-1, len(p)-1))
dp = [[-1 for i in range(len(p))] for j in range(len(s))]
print(isMatchMem(s, p, len(s)-1, len(p)-1, dp))
print(isMatchTab(s, p))
print(isMatchSpace(s, p))
