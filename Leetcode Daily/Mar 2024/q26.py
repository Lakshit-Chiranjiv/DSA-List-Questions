class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains_1 = False
        for i in range(n):
            if nums[i] == 1:
                contains_1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        if not contains_1:
            return 1
        for i in range(n): 
            value = abs(nums[i])
            if value == n:
                nums[0] = - abs(nums[0])
            else:
                nums[value] = - abs(nums[value])
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n 
        return n + 1
    
# 41. First Missing Positive
# Time Complexity: O(n)
# Space Complexity: O(1)
    
# We first check if 1 is present in the list. If not, we return 1. We then iterate through the list and mark the element at the index of the absolute value of the current element as negative. This way we mark the element as visited once. Now, if we encounter any positive element, it denotes that the current element value whose absolute value has led to this index location with negative value has not occured. We return this element. If we do not find any positive element, we return n. If the element at index 0 is positive, we return n+1. Finally, we return n+1.