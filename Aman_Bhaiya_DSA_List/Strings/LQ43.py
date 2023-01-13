class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        ans = S[0]
        for i in range(1,len(S)):
            if S[i-1] != S[i]:
                ans += S[i]
        return ans