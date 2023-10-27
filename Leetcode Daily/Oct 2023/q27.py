class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for i in range(n)] for i in range(n)]
        mxl = 0
        ans = ""
        for g in range(0,n):
            i = 0
            j = g
            while j < n:
                if g == 0:
                    dp[i][j] = True
                elif g == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                
                if dp[i][j] and g+1 > mxl:
                    mxl = g+1
                    ans = s[i:j+1]
                i += 1
                j += 1

        return ans