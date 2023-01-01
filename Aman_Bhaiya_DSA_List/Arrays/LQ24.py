class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = nums[0]
        mn = nums[0]
        ans = nums[0]

        for i in nums[1:]:
            if i < 0:
                mx, mn = mn, mx
            mx = max(i,mx*i)
            mn = min(i,mn*i)
            ans = max(ans,mx)
        return ans