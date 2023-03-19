class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        pref = [0]*n
        pref[0] = nums[0]
        for i in range(1,n):
            pref[i] = pref[i-1]+nums[i]
            
        ans = 0
        for i in pref:
            if i > 0:
                ans += 1
                
        return ans