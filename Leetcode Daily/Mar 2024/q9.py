class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if (set(nums1).intersection(set(nums2))):
            return min(set(nums1).intersection(set(nums2)))
        return -1

# 2540. Minimum Common Value
# Time Complexity: O(n)
# Space Complexity: O(n)
# We simply use the intersection method to find the common elements between the two lists. If there are no common elements, we return -1. Otherwise, we return the minimum common element.