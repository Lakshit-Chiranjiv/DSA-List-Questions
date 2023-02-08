class Solution:
    def jumpHelper(self,nums,idx,dp):
        if idx == len(nums)-1:
            return 0
        if idx >= len(nums):
            return 999999

        if dp[idx] != -1:
            return dp[idx]
        if nums[idx] == 0:
            return 999999
        mn = float('inf')
        for i in range(1,nums[idx]+1):
            x = 1 + self.jumpHelper(nums,idx+i,dp)
            mn = min(x,mn)
        dp[idx] = mn
        return dp[idx]

    
    def jump(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums)+1)]
        return self.jumpHelper(nums,0,dp)