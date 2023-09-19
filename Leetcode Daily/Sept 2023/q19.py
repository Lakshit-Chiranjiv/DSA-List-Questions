class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        for x in nums:
            p = abs(x) - 1
            if nums[p] < 0:
                return abs(x)
            else:
                nums[p] *= -1
        return -1
