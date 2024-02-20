class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return ((len(nums)*(len(nums)+1))//2) - sum(nums)

# 268. Missing Number
# Time complexity: O(n)
# Space complexity: O(1)
    
# Approach: Sum of n natural numbers - sum of given numbers