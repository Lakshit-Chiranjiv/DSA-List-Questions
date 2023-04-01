# evalute boolean expression to true

# recursive solution
def countWays(s, i, j, isTrue):
    if i > j: return 0
    if i == j:
        if isTrue:
            return 1 if s[i] == 'T' else 0
        else:
            return 1 if s[i] == 'F' else 0

    ans = 0
    for k in range(i+1, j, 2):
        lt = countWays(s, i, k-1, True)
        lf = countWays(s, i, k-1, False)
        rt = countWays(s, k+1, j, True)
        rf = countWays(s, k+1, j, False)

        if s[k] == '&':
            if isTrue:
                ans += lt*rt
            else:
                ans += lt*rf + lf*rt + lf*rf
        elif s[k] == '|':
            if isTrue:
                ans += lt*rt + lt*rf + lf*rt
            else:
                ans += lf*rf
        elif s[k] == '^':
            if isTrue:
                ans += lt*rf + lf*rt
            else:
                ans += lt*rt + lf*rf

    return ans

# memoization solution
def countWaysMemo(s, i, j, isTrue, memo):
    if i > j: return 0
    if i == j:
        if isTrue:
            return 1 if s[i] == 'T' else 0
        else:
            return 1 if s[i] == 'F' else 0

    if memo[i][j][isTrue] != -1: return memo[i][j][isTrue]

    ans = 0
    for k in range(i+1, j, 2):
        lt = countWaysMemo(s, i, k-1, True, memo)
        lf = countWaysMemo(s, i, k-1, False, memo)
        rt = countWaysMemo(s, k+1, j, True, memo)
        rf = countWaysMemo(s, k+1, j, False, memo)

        if s[k] == '&':
            if isTrue:
                ans += lt*rt
            else:
                ans += lt*rf + lf*rt + lf*rf
        elif s[k] == '|':
            if isTrue:
                ans += lt*rt + lt*rf + lf*rt
            else:
                ans += lf*rf
        elif s[k] == '^':
            if isTrue:
                ans += lt*rf + lf*rt
            else:
                ans += lt*rt + lf*rf

    memo[i][j][isTrue] = ans
    return ans

# tabulation solution
def countWaysTab(s):
    n = len(s)
    dp = [[[0]*2 for _ in range(n)] for _ in range(n)]

    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if i > j: continue
            if i == j:
                dp[i][j][0] = 1 if s[i] == 'F' else 0
                dp[i][j][1] = 1 if s[i] == 'T' else 0
                continue

            for k in range(i+1, j, 2):
                lt = dp[i][k-1][1]
                lf = dp[i][k-1][0]
                rt = dp[k+1][j][1]
                rf = dp[k+1][j][0]

                if s[k] == '&':
                    dp[i][j][1] += lt*rt
                    dp[i][j][0] += lt*rf + lf*rt + lf*rf
                elif s[k] == '|':
                    dp[i][j][1] += lt*rt + lt*rf + lf*rt
                    dp[i][j][0] += lf*rf
                elif s[k] == '^':
                    dp[i][j][1] += lt*rf + lf*rt
                    dp[i][j][0] += lt*rt + lf*rf
    return dp[0][n-1][1]

s = "T|T&F^T"
n = len(s)
memo = [[[-1]*2 for _ in range(n)] for _ in range(n)]
print(countWays(s, 0, n-1, True))
print(countWaysMemo(s, 0, n-1, True, memo))
print(countWaysTab(s))