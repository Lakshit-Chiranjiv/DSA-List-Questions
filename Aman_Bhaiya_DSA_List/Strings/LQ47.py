class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        mxl = 0
        curr = 0
        for i in range(len(s)):
            if mp.get(s[i],-1) == -1 or mp.get(s[i],-1) < (i - curr):
                mp[s[i]] = i
                curr += 1
                mxl = max(curr,mxl)
            else:
                curr = i - mp[s[i]]
                mp[s[i]] = i
        return mxl