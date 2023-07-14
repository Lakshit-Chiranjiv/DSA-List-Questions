class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mp = {}
        mp[arr[0]] = 1
        ans = 1
        for i in arr[1:]:
            if mp.get(i-difference,0) == 0:
                mp[i] = 1
            else:
                mp[i] = mp[i-difference]+1
            ans = max(ans,mp[i])
        return ans