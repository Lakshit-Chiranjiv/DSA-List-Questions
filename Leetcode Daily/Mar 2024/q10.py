class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

# 349. Intersection of Two Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)
    
# We use the intersection method to find the common elements between the two lists. We then convert the set to a list and return it.