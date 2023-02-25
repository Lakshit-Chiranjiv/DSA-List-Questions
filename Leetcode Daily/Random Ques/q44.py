class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s,p = p,s
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