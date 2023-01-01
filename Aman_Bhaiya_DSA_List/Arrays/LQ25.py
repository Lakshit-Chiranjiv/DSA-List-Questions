class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left <= right:
            mid = (left+right)//2
            if mid != 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] <= nums[right]:
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[0]