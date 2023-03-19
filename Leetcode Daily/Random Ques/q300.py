class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        mx = 1
        for ind in range(1, n):
            for prev_ind in range(ind):
                if nums[ind] > nums[prev_ind]:
                    dp[ind] = max(dp[ind], 1 + dp[prev_ind])
            mx = max(mx, dp[ind])

        return mx