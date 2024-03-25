class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        c = 0
        for n in nums:
            if abs(n) >= len(nums):
                c += 1
                continue
            if nums[abs(n)] > 0:
                nums[abs(n)] *= -1
            else:
                ans.append(abs(n))
        if c > 1:
            ans.append(len(nums))
        return ans
    
# 442. Find All Duplicates in an Array
# Time Complexity: O(n)
# Space Complexity: O(1)
    
# We iterate through the list and multiply the element at the index of the absolute value of the current element by -1. This way we mark the element as visited once. Now, if we encounter any negative element, it denotes that the current element value whose absolute value has led to this index location with negative value has occured twice. We append this element to the answer list. We also maintain a separate counter to check if the element n has occured twice or more. If it has, we append n to the answer list. Finally, we return the answer list.