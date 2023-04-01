class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1

        return -1
    
# intuition:
# 1. Its a sorted array and the best search algo for sorted array is binary search.
# 2. Simply find the mid and check if its the target, if not, then reduce the search space by half depending on the target and mid value.

# solution:
# 1. Initialize l and r to 0 and n-1 respectively.
# 2. While l <= r, find the mid by (l+r)//2.
# 3. If nums[mid] == target, return mid.
# 4. If nums[mid] > target, then reduce the search space by half by setting r = mid-1.
# 5. If nums[mid] < target, then reduce the search space by half by setting l = mid+1.
# 6. If the target is not found, return -1 after the while loop.

# Time complexity: O(logn) where n is the length of the array nums as we are reducing the search space by half at every step.
# Space complexity: O(1) as we are not using any extra space.