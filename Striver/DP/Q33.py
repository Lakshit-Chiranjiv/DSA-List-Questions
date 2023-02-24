# edit distance
# minimum number of operations to convert word1 to word2
# allowed operations:
# insert a character
# delete a character
# replace a character

# recursive solution
def minDistance(word1, word2, i, j):
    if i < 0:
        return j+1
    if j < 0:
        return i+1
    
    if word1[i] == word2[j]:
        return minDistance(word1, word2, i-1, j-1)
    insert = minDistance(word1, word2, i, j-1)
    delete = minDistance(word1, word2, i-1, j)
    replace = minDistance(word1, word2, i-1, j-1)
    return 1 + min(insert, delete, replace)

# memoization
def minDistanceMem(word1, word2, i, j, dp):
    if i < 0:
        return j+1
    if j < 0:
        return i+1
    if dp[i][j] != -1:
        return dp[i][j]
    
    if word1[i] == word2[j]:
        dp[i][j] = minDistanceMem(word1, word2, i-1, j-1, dp)
    else:
        insert = minDistanceMem(word1, word2, i, j-1, dp)
        delete = minDistanceMem(word1, word2, i-1, j, dp)
        replace = minDistanceMem(word1, word2, i-1, j-1, dp)
        dp[i][j] = 1 + min(insert, delete, replace)
    return dp[i][j]

# tabulation
def minDistanceTab(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                insert = dp[i][j-1]
                delete = dp[i-1][j]
                replace = dp[i-1][j-1]
                dp[i][j] = 1 + min(insert, delete, replace)

    return dp[n][m]

# space optimization
def minDistanceOpt(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [0 for i in range(m+1)]
    curr = [0 for i in range(m+1)]

    for i in range(m+1):
        dp[i] = i

    for i in range(1, n+1):
        curr[0] = i
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                curr[j] = dp[j-1]
            else:
                insert = curr[j-1]
                delete = dp[j]
                replace = dp[j-1]
                curr[j] = 1 + min(insert, delete, replace)
        dp = curr.copy()

    return dp[m]

s1 = "horse"
s2 = "ros"
print(minDistance(s1, s2, len(s1)-1, len(s2)-1))
dp = [[-1 for i in range(len(s2))] for j in range(len(s1))]
print(minDistanceMem(s1, s2, len(s1)-1, len(s2)-1, dp))
print(minDistanceTab(s1, s2))
print(minDistanceOpt(s1, s2))