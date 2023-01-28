class Solution:
    def countPS(self,string):
        n = len(string)
        dp = [[0 for i in range(n)] for j in range(n)]
        mod = 1000000007

        for gap in range(n):
            i = 0
            for j in range(gap,n):
                if gap == 0:
                    dp[i][j] = 1
                elif gap == 1:
                    if string[i] == string[j]:
                        dp[i][j] = 3
                    else:
                        dp[i][j] = 2
                else:
                    if string[i] == string[j]:
                        dp[i][j] = (dp[i][j-1] + dp[i+1][j] + 1)%mod
                    else:
                        dp[i][j] = (dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1] + mod)%mod
                i += 1

        return dp[0][n-1]