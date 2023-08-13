class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def solve(i):
            if i >= n:
                return True
            ans = False
            if i < n-1 and nums[i] == nums[i+1]:
                ans = solve(i+2)
            if i < n-2:
                if nums[i] == nums[i+1] == nums[i+2] or nums[i] + 1 == nums[i+1] == nums[i+2] - 1:
                    ans = ans or solve(i+3)

            return ans

        return solve(0)